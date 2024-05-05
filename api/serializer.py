from rest_framework import serializers

from api.models import Tool, Category

class ToolSerializer(serializers.ModelSerializer):
    category = serializers.CharField() 
    class Meta:
        model = Tool
        fields = "__all__"

    def create(self, validated_data):
        category_name = validated_data.pop("category")
        category_instance, _ = Category.objects.get_or_create(name=category_name)
        return Tool.objects.create(**validated_data, category=category_instance)

    def update(self, instance, validated_data):
        instance.link = validated_data.get("link", instance.link)
        instance.description = validated_data.get("description", instance.link_description)
        category_name = validated_data.pop("category")
        category_instance, _ = Category.objects.get_or_create(name=category_name)
        instance.category = category_instance
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"

