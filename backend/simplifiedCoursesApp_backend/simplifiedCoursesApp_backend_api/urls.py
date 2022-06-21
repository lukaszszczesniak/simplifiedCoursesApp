from django.urls import re_path as url
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (
    # TestModelListApiView,
    # TestModelDetailApiView,
    CourseModelListApiView,
    ArticleModelListApiView,
    ArticleModelDetailsApiView,
    CourseModelDetailApiView
)

urlpatterns = [
    # path('testmodels/', TestModelListApiView.as_view()),
    # path('testmodels/<int:testmodel_id>/', TestModelDetailApiView.as_view()),
    path('courses/', CourseModelListApiView.as_view()),
    path('courses/<int:course_id>/', CourseModelDetailApiView.as_view()),
    path('articles/', ArticleModelListApiView.as_view()),
    path('articles/<int:article_id>/', ArticleModelDetailsApiView.as_view()),
    # OpenAPI 3 documentation with Swagger UI:
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(template_name="swagger-ui.html", url_name="schema"), name="swagger-ui",)
]

