from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from recipes.models import Recipe
import os


def delete_cover(instance):
    try:
        os.remove(instance.cover.path)
    except (ValueError, FileNotFoundError):
        pass


@receiver(pre_delete, sender=Recipe)
def recipe_cover_delete(sender, instance, *args, **kwargs):
    old_instance = Recipe.objects.filter(pk=instance.pk)
    delete_cover(old_instance)


@receiver(pre_save, sender=Recipe)
def recipe_cover_update(sender, instance, *args, **kwargs):
    old_instance = Recipe.objects.filter(pk=instance.pk)
    is_new_cover = old_instance != instance.cover

    if is_new_cover:
        delete_cover(old_instance)