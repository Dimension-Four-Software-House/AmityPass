from django.db import models

# Create your models here.

class Class(models.Model):
    PERIOD1 = 1
    PERIOD2 = 2
    PERIOD3 = 3
    PERIOD4 = 4
    PERIOD5 = 5
    PERIOD6 = 6
    PERIOD7 = 7
    PERIOD8 = 8
    PERIOD_CHOICES= [
        (PERIOD1, 'Period 1'),
        (PERIOD2, 'Period 2'),
        (PERIOD3, 'Period 3'),
        (PERIOD4, 'Period 4'),
        (PERIOD5, 'Period 5'),
        (PERIOD6, 'Period 6'),
        (PERIOD7, 'Period 7'),
        (PERIOD8, 'Period 8'),
    ]
    class_name = models.CharField(max_length=80, null=True, blank=True)
    teacher_name = models.CharField(max_length=70, null=True, blank=True)
    period = models.PositiveIntegerField(
        default=PERIOD1,
        choices=PERIOD_CHOICES
        )
    def __str__(self):
        return self.class_name
    class Meta:
        verbose_name_plural = "Classes"
class Assignment(models.Model):
    teacher = models.ForeignKey(
        'Class',
        on_delete=models.CASCADE
    )

#models.CharField(
#    max_length=2,
#    choices=PERIOD_CHOICES,
#    default=PERIOD1,
#    blank=True
#)
