from django.db import models
import datetime
import uuid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class OrderDetails(models.Model):
    class OrderStatus(models.TextChoices):
        INPROGRESS  = 'PRGS', _('InProgress')
        ACCEPTED    = 'ACPT', _('Accepted')
        DELIVERED   = 'DELV', _('Delivered')
        CANCELLED   = 'CANC', _('Cancelled')

    class PaymentMethod(models.TextChoices):
        PAYONDELIVERY       = 'POD', _('PayOnDelivery')
        CREDIT_DEBITCARD    = 'CC/DC', _('Credit/DebitCard')
        NETBANKING          = 'NETBNK', _('NetBanking')
        UPI                 = 'UPI', _('UPI')
        EMI                 = 'EMI', _('EMI')
    
    def present_or_future_date(value):
        if value < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        return value
        
    uid               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    product           = models.ForeignKey(Products, on_delete=models.PROTECT)
    customer          = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    expected_delivery = models.DateField(validators=[present_or_future_date])
    bill_paid         = models.BooleanField(default=False)
    order_active      = models.BooleanField(default=True)
    order_status      = models.CharField(
                            max_length=4,
                            choices=OrderStatus.choices,
                            default=OrderStatus.INPROGRESS,
                            )
    payment_method    = models.CharField(
                            max_length=6,
                            choices=PaymentMethod.choices,
                            default=PaymentMethod.PAYONDELIVERY,
                            )
    order_amount      = models.IntegerField()
    
