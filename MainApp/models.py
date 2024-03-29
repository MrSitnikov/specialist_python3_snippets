from django.contrib.auth.models import User
from django.db import models

LANGS = (
    ("py", "Python"),
    ("js", "JavaScript"),
    ("cpp", "C++"),
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                            blank=True, null=True)
    

class Comment(models.Model):
   text = models.TextField(max_length=5000)
   creation_date = models.DateTimeField(auto_now=True)
   author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                              blank=True, null=True)
   snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE,
                               blank=True, null=True)
