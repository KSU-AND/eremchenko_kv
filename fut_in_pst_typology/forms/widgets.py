from django.forms import Select, Textarea, CheckboxSelectMultiple


intable_select_widget = Select(attrs={"class": "select-in-table", 
                                      "onChange": "postIntableSelect(this);"}) 
main_comment_widget = Textarea(attrs={"class": "comment main", 
                                      "onblur": "postMainComment(this);",
                                      "placeholder": "Комментарий",
                                      "spellcheck": "false",
                                      "rows":""})
comment_widget = Textarea(attrs={"class": "comment",
                                 "onblur": "postComment(this);",
                                 "placeholder": "Комментарий",
                                 "spellcheck": "false",
                                 "rows":""})
textarea_hidden_widget = Textarea(attrs={"name": "theory", 
                                         "style": "display: none;"})
source_widget = Textarea(attrs={"class": "comment source",
                                 "onblur": "postSource(this);",
                                "placeholder": "Ссылка на грамматику",
                                "spellcheck": "false",
                                "rows": "1"})

checkbox_select_widget = CheckboxSelectMultiple(attrs={"class": "checkBoxed",}) 
