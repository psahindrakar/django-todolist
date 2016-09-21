from django.db import models
from enum import Enum

# https://docs.djangoproject.com/en/dev/howto/custom-model-fields/#howto-custom-model-fields
# class EnumField(models.Field):
#     """
#     A field class that maps to MySQL's ENUM type.

#     Usage:

#     class Card(models.Model):
#         suit = EnumField(values=('Clubs', 'Diamonds', 'Spades', 'Hearts'))

#     c = Card()
#     c.suit = 'Clubs'
#     c.save()
#     """

#     def __init__(self, values, *args, **kwargs):
#         self.values = values
#         if self.values:
#             kwargs['choices'] = [(v, v) for v in self.values]
#             kwargs['default'] = self.values[0]
#             super(EnumField, self).__init__(*args, **kwargs)
#         else:
#             raise AttributeError('EnumField requires `values` attribute.')

#     def db_type(self):
#         return "enum({0})".format(','.join("'%s'" % v for v in self.values) )

class CompanyStatusEnum(Enum):
    pending_info = 'Pending Info'
    inactive = 'Inactive'
    active = 'Active'
    

def company_file_storage_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/company_{0}/{1}'.format(instance.id, filename)


class Company(models.Model):
    COMPANY_STATUS = (
        (CompanyStatusEnum.pending_info.value, CompanyStatusEnum.pending_info.value),
        (CompanyStatusEnum.inactive.value, CompanyStatusEnum.inactive.value),
        (CompanyStatusEnum.active.value, CompanyStatusEnum.active.value)
    )

    name = models.CharField(max_length=45)
    website = models.CharField(max_length=150)
    status = models.CharField(max_length=25, choices=COMPANY_STATUS, default=CompanyStatusEnum.pending_info.value)
    # https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.FileField
    insurance_file = models.FileField(blank=True, default='', upload_to=company_file_storage_path)
    
    def __str__(self):
        return self.name