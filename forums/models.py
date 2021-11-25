from django.db import models
import datetime

# remove the pesky microsecond provided which is an eyesore.
now = datetime.datetime.now().replace(microsecond=0)

class Posts(models.Model):
    title=models.CharField(max_length=200,default="topic-title")
    description=models.CharField(max_length=1000,blank=True)
    postedUser = models.CharField(max_length=100,default="Anonymous")
    date_created=models.DateTimeField(default=now, null=True)

    def __str__(self):
        return str(self.title)

    
class Discussion(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    commentTitle=models.CharField(max_length=200,default="topic-title")
    comments = models.CharField(max_length=1000)
    commentUser = models.CharField(max_length=100,default="Anonymous")
    date_created=models.DateTimeField(default=now, null=True)

    def __str__(self):
        return str(self.commentTitle)