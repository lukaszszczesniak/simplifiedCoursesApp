from rest_framework import serializers
from .models import CourseModel, ArticleModel, ComponentType, CourseHasLearnableComponentModel
from rest_enumfield import EnumField

#ORM models serializers
class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ["id", "name", "updated", "description"]


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ["id", "name", "updated", "contents"]


class CourseHasLearnableComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseHasLearnableComponentModel
        fields = ["engaging_course", "engaged_learnable_component", "order"]

#DTO serializers
class CourseFormDtoSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=127)
    description = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)


class CourseDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=127)
    description = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    updated = serializers.DateTimeField()


class ArticleFormDtoSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=127)
    contents = serializers.CharField(min_length=3, max_length=10000)


class ArticleDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    contents = serializers.CharField()
    updated = serializers.DateTimeField()


class SubcomponentDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = EnumField(choices=ComponentType)


class SubcomponentFormSerializer(serializers.Serializer):
    subcomponent_id = serializers.IntegerField()
