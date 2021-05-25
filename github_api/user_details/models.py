from django.db import models
from djongo import models

# Create your models here.

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Owner(BaseClass):
    login = models.CharField(max_length=200)
    id = models.BigIntegerField(unique=True, primary_key=True)
    node_id = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)
    gravatar_id = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    html_url = models.CharField(max_length=200)
    followers_url = models.CharField(max_length=200)
    following_url = models.CharField(max_length=200)
    gists_url = models.CharField(max_length=200)
    starred_url = models.CharField(max_length=200)
    subscriptions_url = models.CharField(max_length=200)
    organizations_url = models.CharField(max_length=200)
    repos_url = models.CharField(max_length=200)
    events_url = models.CharField(max_length=200)
    received_events_url = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    site_admin = models.CharField(max_length=200)


class ReposDetail(BaseClass):
    repo = models.JSONField()
    # owner = models.ForeignKey(
    #     'User',
    #     on_delete=models.CASCADE,
    # )
    # owner = models.EmbeddedField(
    #     model_container=Owner
    # )