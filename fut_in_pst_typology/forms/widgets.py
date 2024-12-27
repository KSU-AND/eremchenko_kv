from django.forms import Select, Textarea


intable_select_widget = Select(attrs={"class": "select-in-table", 
                                      "onChange": "postIntableSelect(this);"}) 
main_comment_widget = Textarea(attrs={"class": "comment main", 
                                      "onblur": "postMainComment(this);",
                                      "placeholder": "Главный комментарий",
                                      "rows":""})
comment_widget = Textarea(attrs={"class": "comment",
                                 "onblur": "postComment(this);",
                                 "placeholder": "Комментарий",
                                 "rows":""})
