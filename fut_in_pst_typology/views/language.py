from django.shortcuts import render
from django.http import HttpResponse

from ..models.language import Language
from ..models.comment import Comment
from ..models.comment_image import CommentImage
from ..forms.tense_marker_form import FutForm, PstForm
from ..forms.tense_system_form import TenseSystemForm
from ..forms.combinations_form import MMForm, MAForm, AMForm, AAForm
from ..forms.main_comment_form import MainCommentForm
from ..forms.comment_form import CommentForm
from ..forms.comment_image_form import CommentImageForm


def language_page(request):
    cur_lang_code = request.GET.get("code")
    cur_lang_obj = Language.objects.get(code=cur_lang_code)

    comments = Comment.objects.filter(lang=cur_lang_obj)

    if request.method == 'POST':
        if request.POST.get("pst") is not None:
            pst_form = PstForm(request.POST, instance=cur_lang_obj)
            pst_form.save()
            return HttpResponse(status=200)
        if request.POST.get("fut") is not None:
            fut_form = FutForm(request.POST, instance=cur_lang_obj)
            fut_form.save()
            return HttpResponse(status=200)
        if request.POST.get("tense_system") is not None:
            tense_system_form = TenseSystemForm(request.POST, instance=cur_lang_obj)
            tense_system_form.save()
            return HttpResponse(status=200)
        if request.POST.get("mm") is not None:
            mm_form = MMForm(request.POST, instance=cur_lang_obj)
            mm_form.save()
            return HttpResponse(status=200)
        if request.POST.get("ma") is not None:
            ma_form = MAForm(request.POST, instance=cur_lang_obj)
            ma_form.save()
            return HttpResponse(status=200)
        if request.POST.get("am") is not None:
            am_form = AMForm(request.POST, instance=cur_lang_obj)
            am_form.save()
            return HttpResponse(status=200)
        if request.POST.get("aa") is not None:
            aa_form = AAForm(request.POST, instance=cur_lang_obj)
            aa_form.save()
            return HttpResponse(status=200)
        if request.POST.get("main_comment") is not None:
            main_comment_form = MainCommentForm(request.POST, instance=cur_lang_obj)
            main_comment_form.save()
            return HttpResponse(status=200)
        if request.POST.get("add_comment") is not None:
            new_comment = Comment.objects.create(lang=cur_lang_obj)
            new_comment_form = CommentForm(instance=new_comment, prefix=str(new_comment.id))
            return render(request, "comment_form.html", {"comment":{"c": new_comment,
                                                                    "form": new_comment_form,
                                                                    "images": []}
                                                                    })
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
            return render(request, "comment_form.html", {"comment":{"c": comment,
                                                                    "form": comment_form,
                                                                    "images": images}
                                                                    })
        if request.POST.get("comment_was_edited") is not None:
            comment_ids = [k.split('-')[0] for k in request.POST.keys() 
                           if not k.startswith("csrf") and k.endswith("comment")]
            for comment_id in comment_ids:
                comment = Comment.objects.get(id=int(comment_id))
                form = CommentForm(request.POST, prefix=comment_id, instance=comment)
                form.save() if form.is_valid() else comment.delete()
            return HttpResponse(status=200)
            
    
    context = {
        "user": request.user,
        "cur_lang": cur_lang_obj,
        "lang_list": Language.objects.all(),
        "forms":{
            "ts": TenseSystemForm(instance=cur_lang_obj),
            "fut": FutForm(instance=cur_lang_obj),
            "pst": PstForm(instance=cur_lang_obj),
            "mm": MMForm(instance=cur_lang_obj),
            "ma": MAForm(instance=cur_lang_obj),
            "am": AMForm(instance=cur_lang_obj),
            "aa": AAForm(instance=cur_lang_obj),
            "main_comment": MainCommentForm(instance=cur_lang_obj),
            "comments": [{"c": c,
                          "form": CommentForm(instance=c, prefix=str(c.id)),
                          "images": CommentImage.objects.filter(comment=c),
                          } for c in comments],
        },
    }
    return render(request, "language.html", context)
