from django.db import models
from django.utils.translation import gettext_lazy as gtl

from .family import Family
from .genus import Genus
from .theory import TheoryBlock

class Language(models.Model):
    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"
    
    class TenseSystem(models.TextChoices):
        f = "fut / non-fut",    gtl("fut / non-fut")
        p = "pst / non-pst",    gtl("pst / non-pst")
        t = "3 part",           gtl("Трёхчастная") 
        n = "no tenses",        gtl("Нет времён")
        __empty__ =             gtl("(Unknown)")
    
    class TenseMarker(models.TextChoices):
        m = "Mrph",     gtl("Морфологич.")
        a = "Anlt",     gtl("Аналитич.")
        b = "M + A",    gtl("Возможны оба") 
        n = "---",      gtl("Ни одного")
        __empty__ =     gtl("(Unknown)")

    class CombOptionState(models.TextChoices):
        Y = "YES",       gtl("Подтвержд. да")
        N = "not found", gtl("Кажется нет")
        Q = "?",         gtl("Непонятно")
        T = "---",       gtl("Невозможно") 
        __empty__ =      gtl("(Unknown)")

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    
    tense_system = models.CharField(max_length=15, choices=TenseSystem, blank=True)
    fut = models.CharField(max_length=5, choices=TenseMarker, blank=True)
    pst = models.CharField(max_length=5, choices=TenseMarker, blank=True)

    mm = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    am = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    ma = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    aa = models.CharField(max_length=10, choices=CombOptionState, blank=True)

    main_comment = models.TextField(blank=True)
    
    theory_blocks = models.ManyToManyField(TheoryBlock, related_name="languages")

    def __str__(self) -> str:
        return self.name
