# church/serializers.py
from rest_framework import serializers

from .models import Member
from rest_framework.reverse import reverse
class MemberListSerializer(serializers.ModelSerializer):
    
    absolute_url = serializers.SerializerMethodField()
    
    class Meta:

        model = Member

        fields = ['id', 'name', 'surname', 'absolute_url']

    def get_absolute_url(self, obj):
        return reverse('member_detail', args=(obj.pk,))

class MemberDetailSerializer(serializers.ModelSerializer):
    
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()

    class Meta:

        model = Member

        fields = ['id', 'name', 'surname', 'position', 'address', 'age', 'update', 'delete']

    def get_update(self, obj):
        return reverse('member_update', args=(obj.pk,))
   
    def get_delete(self, obj):
        return reverse('member_delete', args=(obj.pk,))