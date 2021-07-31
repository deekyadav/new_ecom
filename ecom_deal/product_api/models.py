from django.db import models
import uuid
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.

class Products(models.Model):
    uid             =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial_number   =   models.CharField(unique = True, max_length=20, validators=
                                [RegexValidator(regex='^.{20}$', message='Serial number \
                                length has to be 20', code='nomatch')])
    title           =   models.CharField(max_length=100)
    current_stock   =   models.IntegerField()
    product_info    =   models.CharField(max_length=250)
    categories      =   models.CharField(max_length=100)
    batch           =   models.IntegerField(unique = True)
    product_status  =   models.BooleanField(default=True)
    product_image   =   models.ImageField()
    current_price   =   models.IntegerField()
    publish_on      =   models.DateTimeField(default=timezone.now)