from django.conf import settings
from django.db import models


class UserOwnedModelManager(models.Manager):

    def filter_for_user(self, user):
        return super(UserOwnedModelManager, self).get_queryset().filter(user = user)

    def get_for_user(self, user, *args, **kwargs):
        if 'user' in kwargs:
            kwargs.pop('user')
        return super(UserOwnedModelManager, self).get_queryset().get(user = user, *args, **kwargs)


class UserOwnedModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False)

    objects = UserOwnedModelManager()

    class Meta:
        abstract = True