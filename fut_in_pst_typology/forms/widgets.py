from django.forms import Select, Textarea


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
theory_outline_widget = Textarea(attrs={"id": "theory_outline",
                                        "style": "display: none;",
                                        })
theory_text_widget = Textarea(attrs={"id": "theory_text",
                                     "style": "display: none;",
                                     })
