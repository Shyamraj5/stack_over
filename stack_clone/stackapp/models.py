from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="qust_images",null=True)
    date=models.DateField(auto_now_add=True)




class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    upvote=models.ManyToManyField(User,related_name="user")

    