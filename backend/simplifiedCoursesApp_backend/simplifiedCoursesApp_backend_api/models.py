from django.db import models
from django.contrib.auth.models import User

#
# class TestModel(models.Model):
#     task = models.CharField(max_length=180)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
#     completed = models.BooleanField(default=False, blank=True)
#     updated = models.DateTimeField(auto_now=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#
#     def __str__(self):
#         return self.task


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
