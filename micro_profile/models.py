from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from micro.models import TimeStampModel
from . import profile_choices
from micro.image_paths import profile_image_path
from phonenumber_field.modelfields import PhoneNumberField


UserModel = get_user_model()


class Address(TimeStampModel):
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, default='Egypt')
    city = models.CharField(max_length=2, choices=profile_choices.GOVERNORATE_CHOICES, default='ca')
    building_number = models.IntegerField(default=0)
    primary = models.BooleanField(default=False)

    def __str__(self):
        return "Address (%s)"% self.id


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    skills = models.ManyToManyField('tasks.Category', related_name='skills')
    addresses = models.ManyToManyField(Address, related_name='addresses')
    profile_picture = models.ImageField(upload_to=profile_image_path, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True, error_messages={
                                    'unique': _("A phone number already exists."), })
    transportation = models.CharField(
        max_length=1, choices=profile_choices.TRANSPORTATION_CHOICES, null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=profile_choices.GENDER_CHOICES, null=True, blank=True)
    id_number = models.IntegerField(validators=[MaxLengthValidator(14)], blank=True, null=True)
    accept_terms = models.BooleanField(default=False)
    is_tasker = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
