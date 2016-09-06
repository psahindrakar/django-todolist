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


class Company(models.Model):
    COMPANY_STATUS = (
        (CompanyStatusEnum.pending_info.value, CompanyStatusEnum.pending_info.value),
        (CompanyStatusEnum.inactive.value, CompanyStatusEnum.inactive.value),
        (CompanyStatusEnum.active.value, CompanyStatusEnum.active.value)
    )

    name = models.CharField(max_length=45)
    website = models.CharField(max_length=150)
    # status = EnumField(values=('Pending Info', 'Inactive', 'Active'))
    status = models.CharField(max_length=25, choices=COMPANY_STATUS, default=CompanyStatusEnum.pending_info.value)

    def __str__(self):
        return self.name
