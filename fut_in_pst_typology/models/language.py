from django.db import models
from django.utils.translation import gettext_lazy as gtl

from .area import Area
from .genus import Genus
from .family import Family
from .theory import TheoryBlock

class Language(models.Model):
    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"
    
    class TenseSystem(models.TextChoices):
        fut = "fut / non-fut",    gtl("fut / non-fut")
        prs = "prs / non-prs",    gtl("prs / non-prs")
        pst = "pst / non-pst",    gtl("pst / non-pst")
        thr = "3 part",           gtl("Трёхчастная") 
        no = "no tenses",         gtl("Нет времён")
        __empty__ =               gtl("(Unknown)")
    
    class TenseMarker(models.TextChoices):
        m = "Mrph",     gtl("Морфологич.")
        a = "Anlt",     gtl("Аналитич.")
        b = "M + A",    gtl("Возможны оба") 
        c = "Clitic",   gtl("Клитика")
        n = "---",      gtl("Ни одного")
        __empty__ =     gtl("(Unknown)")

    class CombOptionState(models.TextChoices):
        Y = "YES",       gtl("Подтвержд. да")
        N = "not found", gtl("Кажется нет")
        Q = "?",         gtl("Непонятно")
        T = "---",       gtl("Невозможно") 
        __empty__ =      gtl("(Unknown)")
        
    class Status(models.TextChoices):
        DONE = "DN",    gtl("Закончен")
        CHECK = "CH",   gtl("Проверить")
        INPROG = "IP",  gtl("Начат") 
        NOTIN = "NI",   gtl("Нет в Базе") 
        __empty__ =     gtl("Не начат")

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)
    
    tense_system = models.CharField(max_length=15, choices=TenseSystem, blank=True)
    fut = models.CharField(max_length=6, choices=TenseMarker, blank=True)
    pst = models.CharField(max_length=6, choices=TenseMarker, blank=True)

    mm = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    am = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    ma = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    aa = models.CharField(max_length=10, choices=CombOptionState, blank=True)

    main_comment = models.TextField(blank=True)
    progress = models.CharField(max_length=2, choices=Status, blank=True)
    
    theory_blocks = models.ManyToManyField(TheoryBlock, related_name="languages", blank=True)

    def __str__(self) -> str:
        return self.name
