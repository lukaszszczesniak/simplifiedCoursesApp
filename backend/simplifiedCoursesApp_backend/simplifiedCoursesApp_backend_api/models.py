from enum import Enum
from django.db import models
from django.contrib.auth.models import User


class LearnableComponentModel(models.Model):
    name = models.CharField(max_length=127)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class CourseModel(LearnableComponentModel):
    description = models.CharField(max_length=255, blank=True)


class ArticleModel(LearnableComponentModel):
    contents = models.TextField()


class CourseHasLearnableComponentModel(models.Model):
    engaging_course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    engaged_learnable_component = models.ForeignKey(LearnableComponentModel, on_delete=models.CASCADE, related_name='+')
    order = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['engaging_course', 'engaged_learnable_component'],
                name='course_has_component'),
            models.UniqueConstraint(
                fields=['engaging_course', 'order'],
                name='course_has_component_order')
        ]


class ComponentType(Enum):
    COURSE = 1
    ARTICLE = 2


class ArticleRenderedDto:
    def __init__(self, article_id: int, name: str, contents: str):
        self.article_id = article_id
        self.name = name
        self.contents = contents


class CourseRenderedDto:
    def __init__(self, course_id: int,name: str, description: str, subcomponents):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.subcomponents = subcomponents
