#import dependencies as dependencies
from django.db import models, migrations
import datetime
from django.utils import timezone

# Create your models here.



class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   #print(question_text)

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Member(models.Model):
    #id = models.IntegerField(primary_key=True)
    age = models.IntegerField(default=0)
    a1_1 = models.IntegerField(default=0)
    a1_2 = models.IntegerField(default=0)
    a1_3 = models.IntegerField(default=0)
    a1_4 = models.IntegerField(default=0)
    a1_5 = models.IntegerField(default=0)
    a1_6 = models.IntegerField(default=0)
    a1_7 = models.IntegerField(default=0)
    a1_8 = models.IntegerField(default=0)
    a1_9 = models.IntegerField(default=0)
    a1_10 = models.IntegerField(default=0)
    a1_11 = models.IntegerField(default=0)
    a1_12 = models.IntegerField(default=0)
    a1_13 = models.IntegerField(default=0)
    a1_14 = models.IntegerField(default=0)
    a1_15 = models.IntegerField(default=0)
    a1_16 = models.IntegerField(default=0)
    a1_17 = models.IntegerField(default=0)
    a1_18 = models.IntegerField(default=0)
    a1_19 = models.IntegerField(default=0)
    a1_20 = models.IntegerField(default=0)
    a1_21 = models.IntegerField(default=0)
    a1_22 = models.IntegerField(default=0)
    a1_23 = models.IntegerField(default=0)
    a1_24 = models.IntegerField(default=0)
    a1_25 = models.IntegerField(default=0)
    a1_26 = models.IntegerField(default=0)
    a1_27 = models.IntegerField(default=0)
    a1_28 = models.IntegerField(default=0)
    a1_29 = models.IntegerField(default=0)
    a1_30 = models.IntegerField(default=0)
    a1_31 = models.IntegerField(default=0)
    a1_32 = models.IntegerField(default=0)
    a1_33 = models.IntegerField(default=0)
    a1_34 = models.IntegerField(default=0)
    a1_35 = models.IntegerField(default=0)
    a1_36 = models.IntegerField(default=0)
    a1_text = models.TextField(max_length=200)
    a2_1 = models.IntegerField(default=0)
    a2_2 = models.IntegerField(default=0)
    a3_1 = models.IntegerField(default=0)
    a3_2 = models.IntegerField(default=0)
    a3_3 = models.IntegerField(default=0)
    a3_4 = models.IntegerField(default=0)
    a3_text = models.TextField(max_length=200)

    def __str__(self):
        return '<Member1:id=' + str(self.id) + ',(' + str(self.age) + '),(' + str(self.a1_text) + ')>'

'''
class Member2(models.Model):
    a1_text = models.TextField(max_length=200)
    a2_1 = models.IntegerField(default=0)
    a2_2 = models.IntegerField(default=0)
    a3_1 = models.IntegerField(default=0)
    a3_2 = models.IntegerField(default=0)
    a3_3 = models.IntegerField(default=0)
    a3_4 = models.IntegerField(default=0)
    a3_5 = models.TextField(max_length=200)

    def __str__(self):
        return '<Member2:id=' + str(self.id) + '>'
'''