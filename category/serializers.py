from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    parent_id = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'parent_id', 'status')

    def get_parent(self, obj):
        if obj.parent is not None:
            id_parent = obj.parent_id
            parent = Category.objects.filter(pk=id_parent).first()
            parent = parent.name
        else:
            parent = False
        return parent

    def get_parent_id(self, obj):
        if obj.parent is not None:
            id_parent = obj.parent_id
            parent = id_parent
        else:
            parent = False
        return parent