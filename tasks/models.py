from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from micro.models import TimeStampModel
from micro import image_paths
from micro_profile.models import Address
from phonenumber_field.modelfields import PhoneNumberField
from mptt.models import MPTTModel, TreeForeignKey



UserModel = get_user_model()


class Category(MPTTModel, TimeStampModel):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=image_paths.category_image_path, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, 
                                related_name='children', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_childrens(self):
        pass

class Task(TimeStampModel):

    SIZE_CHOICES = (
        ('s', _('Small')), # 1 hrs
        ('m', _('Medium')), # 2-4 hrs
        ('l', _('Large')), # 5+ hrs
    )

    VEHICLE_CHOICES = (
        ('b', _('Bicycle')),
        ('m', _('Motorcycle')),
        ('c', _('Car')),
        ('v', _('Van')),
        ('t', _('Truck')),
    )

    STATUS_CHOICES = (
        ('a', _('Active')),
        ('h', _('Has Deal')),
        ('d', _('Done')),
    )

    tasker = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='tasker')
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='client')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address')
    category = TreeForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='s')
    vehicle_requirement = models.CharField(max_length=1, choices=VEHICLE_CHOICES, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(validators=[
                            MinValueValidator(1, _("Enter value greater than or equal 1 day")), 
                            MaxValueValidator(30, _("Enter value less than or equal 30 days"))])
    client_phone = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return "Task (%s)"% self.id

    @property
    def has_deal(self):
        return True if self.deals else False
    
    @property
    def has_deal_accepted(self):
        return True if TaskDeal.objects.filter(task=self, is_accepted=True) else False



class TaskDeal(TimeStampModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='deals')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return "Task Deal (%s) on Task (%s)"% (self.id, self.task.id)
