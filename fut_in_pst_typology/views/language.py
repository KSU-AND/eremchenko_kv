from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from ..models.language import Language
from ..models.area import Area
from ..models.genus import Genus
from ..models.family import Family
from ..models.comment import Comment
from ..models.comment_image import CommentImage
from ..models.source import Source
from ..forms.area_form import AreaForm
from ..forms.tense_marker_form import FutForm, PstForm
from ..forms.tense_system_form import TenseSystemForm
from ..forms.combinations_form import MMForm, MAForm, AMForm, AAForm
from ..forms.main_comment_form import MainCommentForm
from ..forms.comment_form import CommentForm
from ..forms.theory_form import TheoryBlocksForm
from ..forms.progress_form import ProgressForm
from ..forms.source_form import SourceForm


class LanguageView(View):
    def get(self, request, code):

        current_language = Language.objects.select_related("area", "genus", "family").get(code=code)
        comments = Comment.objects.filter(lang=current_language).order_by("id")
        sources = Source.objects.filter(lang=current_language).order_by("source")

        context = {
            "user": request.user,
            "cur_lang": current_language,
            "languages": Language.objects.order_by("name").all(),
            "areas": Area.objects.order_by("name").all(),
            "genuses": Genus.objects.order_by("name").all(),
            "families": Family.objects.order_by("name").all(),
            "theory_blocks": current_language.theory_blocks.all(),
            "forms":{
                "area": AreaForm(instance=current_language),
                "ts": TenseSystemForm(instance=current_language),
                "fut": FutForm(instance=current_language),
                "pst": PstForm(instance=current_language),
                "mm": MMForm(instance=current_language),
                "ma": MAForm(instance=current_language),
                "am": AMForm(instance=current_language),
                "aa": AAForm(instance=current_language),
                "main_comment": MainCommentForm(instance=current_language),
                "progress": ProgressForm(instance=current_language),
                "comments": [{"c": c,
                              "form": CommentForm(instance=c, prefix=str(c.id)),
                              "images": CommentImage.objects.filter(comment=c),
                              } for c in comments],
                "theory_blocks": TheoryBlocksForm(instance=current_language),
                "sources": [{"source": s,
                             "form": SourceForm(instance=s, prefix=str(s.id))
                            } for s in  sources],
            },
        }
        return render(request, "language.html", context)

    def post(self, request, code):
        current_language = Language.objects.get(code=code)

        if request.POST.get("area") is not None:
            area_form = AreaForm(request.POST, instance=current_language)
            if area_form.is_valid(): area_form.save()
            else:
                current_language.area = None
                current_language.save()
            return HttpResponse(status=200)
        if request.POST.get("pst") is not None:
            pst_form = PstForm(request.POST, instance=current_language)
            pst_form.save()
            return HttpResponse(status=200)
        if request.POST.get("fut") is not None:
            fut_form = FutForm(request.POST, instance=current_language)
            fut_form.save()
            return HttpResponse(status=200)
        if request.POST.get("tense_system") is not None:
            tense_system_form = TenseSystemForm(request.POST, instance=current_language)
            tense_system_form.save()
            return HttpResponse(status=200)
        if request.POST.get("mm") is not None:
            mm_form = MMForm(request.POST, instance=current_language)
            mm_form.save()
            return HttpResponse(status=200)
        if request.POST.get("ma") is not None:
            ma_form = MAForm(request.POST, instance=current_language)
            ma_form.save()
            return HttpResponse(status=200)
        if request.POST.get("am") is not None:
            am_form = AMForm(request.POST, instance=current_language)
            am_form.save()
            return HttpResponse(status=200)
        if request.POST.get("aa") is not None:
            aa_form = AAForm(request.POST, instance=current_language)
            aa_form.save()
            return HttpResponse(status=200)
        if request.POST.get("main_comment") is not None:
            main_comment_form = MainCommentForm(request.POST, instance=current_language)
            main_comment_form.save()
            return HttpResponse(status=200)
        if request.POST.get("progress") is not None:
            progress_form = ProgressForm(request.POST, instance=current_language)
            progress_form.save()
            return HttpResponse(status=200)
        if request.POST.get("add_comment") is not None:
            new_comment = Comment.objects.create(lang=current_language, user=request.user)
            new_comment_form = CommentForm(instance=new_comment, prefix=str(new_comment.id))
            return render(request, "comment_form.html", {"user": request.user,
                                                         "comment":{"c": new_comment,
                                                                    "form": new_comment_form,
                                                                    "images": []}})
        if request.POST.get("add_image") is not None:
            if request.FILES:
                comment_ids = [k for k in request.FILES.keys() if k.endswith("comment")]
                comment_id = int(comment_ids[0].split('-')[0])
                comment = Comment.objects.get(id=comment_id)
                CommentImage.objects.create(image=request.FILES[comment_ids[0]],
                                            comment=comment)
            else:
                comment_ids = [k for k in request.POST.keys() if k.endswith("comment")]
                comment_id = int(comment_ids[0].split('-')[0])
                comment = Comment.objects.get(id=comment_id)
            comment_form = CommentForm(instance=comment, prefix=str(comment.id))
            images = CommentImage.objects.filter(comment=comment)
            return render(request, "comment_form.html", {"user": request.user,
                                                         "comment":{"c": comment,
                                                                    "form": comment_form,
                                                                    "images": images}
                                                                    })
        if request.POST.get("delete_image") is not None:
            comment_image_to_delete = CommentImage.objects.get(id=request.POST.get("delete_image"))
            comment_image_to_delete.delete()
            return HttpResponse(status=200)
        
        if request.POST.get("comment_was_edited") is not None:
            comment_ids = [k.split('-')[0] for k in request.POST.keys() 
                           if not k.startswith("csrf") and k.endswith("comment")]
            for comment_id in comment_ids:
                comment = Comment.objects.get(id=int(comment_id))
                form = CommentForm(request.POST, prefix=comment_id, instance=comment)
                form.save() if form.is_valid() else comment.delete()
            return HttpResponse(status=200)
        
        if request.POST.get("add_source") is not None:
            new_source = Source.objects.create(lang=current_language)
            new_source_form = SourceForm(instance=new_source, prefix=str(new_source.id))
            return render(request, 
                          "block/source_form.html", 
                          {"user": request.user, 
                           "source": {"form": new_source_form}})
        if request.POST.get("source_was_edited") is not None:
            source_ids = [k.split('-')[0] for k in request.POST.keys() 
                           if not k.startswith("csrf") and k.endswith("source")]
            for source_id in source_ids:
                source = Source.objects.get(id=int(source_id))
                form = SourceForm(request.POST, prefix=source_id, instance=source)
                form.save() if form.is_valid() else source.delete()
            return HttpResponse(status=200)
        
        if request.POST.get("theory_blocks") is not None:
            post = dict(request.POST)
            post["theory_blocks"] = [i for i in post["theory_blocks"] if i]
            if post["theory_blocks"]:
                theory_blocks_form = TheoryBlocksForm(post, instance=current_language)
                theory_blocks_form.save()
                return render(request, "block/theory_blocks.html", {"theory_blocks": current_language.theory_blocks.all()})
            else:
                theory_blocks = current_language.theory_blocks.all()
                for tb in theory_blocks:
                    current_language.theory_blocks.remove(tb)
                return render(request, "block/theory_blocks.html")