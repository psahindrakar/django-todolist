from rest_framework import serializers
from .models import Company
from usertasks.serializers import CompanyUserSerializer

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    See: http://tomchristie.github.io/rest-framework-2-docs/api-guide/serializers
    """
    def __init__(self, *args, **kwargs):
        # Do not pass the custom fields received in kwargs to super class
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(self.fields)
            required = set(fields)
            to_remove = allowed - required
            if to_remove != allowed:  
                for field_name in to_remove:
                    self.fields.pop(field_name)
                

class DynamicCompanySerializer(DynamicFieldsModelSerializer):
    # You can add extra fields to a ModelSerializer or override the default fields by declaring fields on the class, just as you would for a Serializer class.
    users = CompanyUserSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        # You can set the exclude attribute to a list of fields to be excluded from the serializer.
        # exclude = ('users',)
        # You can also set the fields attribute to the special value '__all__' to indicate that all fields in the model should be used.
        # If fields is not defined, by default it is considered __all__
        # fields = '__all__'
        # The default ModelSerializer uses primary keys for relationships, but you can also easily generate nested representations using the depth option:
        # depth = 1


class CompanySerializer(serializers.ModelSerializer):
    users = CompanyUserSerializer(many=True, read_only=True)
    # users = serializers.StringRelatedField(many=True)
    # users = serializers.HyperlinkedIdentityField('users', view_name='companyuses', lookup_field='username')

    class Meta:
        model = Company