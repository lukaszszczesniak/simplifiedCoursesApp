import json

from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseModel, LearnableComponentModel, ArticleRenderedDto, CourseRenderedDto
from .serializers import *
import jsonpickle

class ArticleModelListApiView(APIView):
    @extend_schema(responses=ArticleDtoSerializer(many=True))
    def get(self, request, *args, **kwargs):
        articles_models = ArticleModel.objects
        response_serializer = ArticleDtoSerializer(articles_models, many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=ArticleFormDtoSerializer, responses={status.HTTP_201_CREATED: ArticleDtoSerializer})
    def post(self, request, *args, **kwargs):
        request_serializer = ArticleFormDtoSerializer(data=request.data)
        if request_serializer.is_valid():
            article_model_serializer = ArticleModelSerializer(data=request_serializer.data)
            if article_model_serializer.is_valid():
                article_model_serializer.save()
                response_serializer = ArticleDtoSerializer(data=article_model_serializer.data)
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_201_CREATED)
                return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(article_model_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleModelDetailsApiView(APIView):
    @extend_schema(responses={status.HTTP_200_OK: ArticleDtoSerializer, status.HTTP_400_BAD_REQUEST: str})
    def get(self, request, article_id, *args, **kwargs):
        article_model = None
        try:
            article_model = ArticleModel.objects.get(id=article_id)
        except:
            return Response("Article with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        response_serializer = ArticleDtoSerializer(article_model)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=ArticleFormDtoSerializer, responses=ArticleDtoSerializer)
    def put(self, request, article_id, *args, **kwargs):
        article_model = None
        try:
            article_model = ArticleModel.objects.get(id=article_id)
        except:
            return Response("Article with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        request_serializer = ArticleFormDtoSerializer(data=request.data)
        if request_serializer.is_valid():
            article_model_serializer = ArticleModelSerializer(instance=article_model, data=request_serializer.data,
                                                              partial=True)
            if article_model_serializer.is_valid():
                article_model_serializer.save()
                response_serializer = ArticleDtoSerializer(data=article_model_serializer.data)
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(article_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={status.HTTP_200_OK: str, status.HTTP_400_BAD_REQUEST: str})
    def delete(self, request, article_id, *args, **kwargs):
        article_model = None
        try:
            article_model = ArticleModel.objects.get(id=article_id)
        except:
            return Response("Article with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        article_model.delete()
        return Response("Article deleted", status=status.HTTP_200_OK)


class CourseModelListApiView(APIView):
    @extend_schema(responses=CourseDtoSerializer(many=True))
    def get(self, request, *args, **kwargs):
        courses_models = CourseModel.objects
        serializer = CourseModelSerializer(courses_models, many=True)
        response_serializer = CourseDtoSerializer(serializer.data, many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CourseFormDtoSerializer, responses={status.HTTP_201_CREATED: CourseDtoSerializer})
    def post(self, request, *args, **kwargs):
        request_serializer = CourseFormDtoSerializer(data=request.data)
        if request_serializer.is_valid():
            course_model_serializer = CourseModelSerializer(data=request_serializer.data)
            if course_model_serializer.is_valid():
                course_model_serializer.save()
                response_serializer = CourseDtoSerializer(data=course_model_serializer.data)
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_201_CREATED)
                return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(course_model_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseModelDetailApiView(APIView):
    @extend_schema(responses={status.HTTP_200_OK: CourseDtoSerializer, status.HTTP_400_BAD_REQUEST: str})
    def get(self, request, course_id, *args, **kwargs):
        course_model = None
        try:
            course_model = CourseModel.objects.get(id=course_id)
        except:
            return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        response_serializer = CourseDtoSerializer(course_model)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CourseFormDtoSerializer, responses=CourseDtoSerializer)
    def put(self, request, course_id, *args, **kwargs):
        course_model = None
        try:
            course_model = CourseModel.objects.get(id=course_id)
        except:
            return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        request_serializer = CourseFormDtoSerializer(data=request.data)
        if request_serializer.is_valid():
            course_model_serializer = CourseModelSerializer(instance=course_model, data=request_serializer.data,
                                                            partial=True)
            if course_model_serializer.is_valid():
                course_model_serializer.save()
                response_serializer = CourseDtoSerializer(data=course_model_serializer.data)
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(course_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={status.HTTP_200_OK: str, status.HTTP_400_BAD_REQUEST: str})
    def delete(self, request, course_id, *args, **kwargs):
        course_model = None
        try:
            course_model = CourseModel.objects.get(id=course_id)
        except:
            return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        course_model.delete()
        return Response("Course deleted", status=status.HTTP_200_OK)


class CourseSubcomponentsListApiView(APIView):
    @staticmethod
    def courseHasLearnableComponentModelQuerySetToResponseSerializer(
            subcomponents_relations: QuerySet) -> SubcomponentDtoSerializer:
        subcomponents_relations = sorted(subcomponents_relations,
                                         key=lambda courseHasLearnableComponentModel:
                                         courseHasLearnableComponentModel.order)
        all_data = []
        for subcomponent_relation in subcomponents_relations:
            single_data = {
                'id': subcomponent_relation.engaged_learnable_component_id
            }
            try:
                subcomponent_relation.engaged_learnable_component.coursemodel
                single_data['type'] = ComponentType.COURSE
            except:
                try:
                    subcomponent_relation.engaged_learnable_component.articlemodel
                    single_data['type'] = ComponentType.ARTICLE
                except:
                    raise Exception
            all_data.append(single_data)
        response_serializer = SubcomponentDtoSerializer(data=all_data, many=True)
        return response_serializer

    @extend_schema(responses=SubcomponentDtoSerializer(many=True))
    def get(self, request, course_id, *args, **kwargs):
        try:
            course_model = CourseModel.objects.get(id=course_id)
        except:
            return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)

        subcomponents_relations = CourseHasLearnableComponentModel.objects.filter(engaging_course=course_id)
        response_serializer = self.courseHasLearnableComponentModelQuerySetToResponseSerializer(subcomponents_relations)
        if response_serializer.is_valid():
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(request=SubcomponentFormSerializer,
                   responses={status.HTTP_200_OK: SubcomponentDtoSerializer(many=True),
                              status.HTTP_400_BAD_REQUEST: None})
    def post(self, request, course_id, *args, **kwargs):
        request_serializer = SubcomponentFormSerializer(data=request.data)
        if request_serializer.is_valid():
            subcomponent_id = request_serializer.data['subcomponent_id']
            try:
                course_model = CourseModel.objects.get(id=course_id)
            except:
                return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)
            try:
                subcomponent = LearnableComponentModel.objects.get(id=subcomponent_id)
            except:
                return Response("Component with given ID not found", status=status.HTTP_400_BAD_REQUEST)
            if subcomponent_id == course_id:
                return Response("Component cannot have itself!", status=status.HTTP_400_BAD_REQUEST)
            try:
                CourseHasLearnableComponentModel.objects.get(engaging_course_id=course_id,
                                                             engaged_learnable_component_id=subcomponent_id)
                return Response("Cannot duplicate child", status.HTTP_400_BAD_REQUEST)
            except:
                all_order_numbers = CourseHasLearnableComponentModel.objects.filter(
                    engaging_course_id=course_id).values_list('order', flat=True)
                last_order_number = 0
                if len(all_order_numbers) != 0:
                    last_order_number = max(all_order_numbers)
                data = {
                    'engaging_course': course_id,
                    'engaged_learnable_component': subcomponent_id,
                    'order': last_order_number + 1
                }
                course_has_learnable_component_serializer = CourseHasLearnableComponentSerializer(data=data)
                if course_has_learnable_component_serializer.is_valid():
                    course_has_learnable_component_serializer.save()
                    subcomponents_relations = CourseHasLearnableComponentModel.objects.filter(engaging_course=course_id)
                    response_serializer = self.courseHasLearnableComponentModelQuerySetToResponseSerializer(
                        subcomponents_relations)
                    if response_serializer.is_valid():
                        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
                    return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response(course_has_learnable_component_serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseSubcomponentsDetailApiView(APIView):
    @staticmethod
    def courseHasLearnableComponentModelQuerySetToResponseSerializer(
            subcomponents_relations: QuerySet) -> SubcomponentDtoSerializer:
        subcomponents_relations = sorted(subcomponents_relations,
                                         key=lambda courseHasLearnableComponentModel:
                                         courseHasLearnableComponentModel.order)
        all_data = []
        for subcomponent_relation in subcomponents_relations:
            single_data = {
                'id': subcomponent_relation.engaged_learnable_component_id
            }
            try:
                subcomponent_relation.engaged_learnable_component.coursemodel
                single_data['type'] = ComponentType.COURSE
            except:
                try:
                    subcomponent_relation.engaged_learnable_component.articlemodel
                    single_data['type'] = ComponentType.ARTICLE
                except:
                    raise Exception
            all_data.append(single_data)
        response_serializer = SubcomponentDtoSerializer(data=all_data, many=True)
        return response_serializer

    def delete(self, request, course_id, subcomponent_id, *args, **kwargs):
        try:
            course_model = CourseModel.objects.get(id=course_id)
        except:
            return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        try:
            relation = CourseHasLearnableComponentModel.objects.get(engaging_course_id=course_id,
                                                                    engaged_learnable_component_id=subcomponent_id)
            relation.delete()
            subcomponents_relations = CourseHasLearnableComponentModel.objects.filter(engaging_course=course_id)
            response_serializer = self.courseHasLearnableComponentModelQuerySetToResponseSerializer(
                subcomponents_relations)
            if response_serializer.is_valid():
                return Response(response_serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response("Subcomponent with given ID not found", status.HTTP_400_BAD_REQUEST)


class CourseViewView(APIView):

    def get(self, request, course_id, *args, **kwargs):
        course_model = None
        try:
            course_model = CourseModel.objects.get(id=course_id)
        except:
            return Response("Course with given ID not found", status=status.HTTP_400_BAD_REQUEST)
        rendered_course = self.render_course(course_model)
        pickler = jsonpickle.pickler.Pickler(make_refs=False, unpicklable=False)
        return Response(pickler.flatten(obj=rendered_course), status=status.HTTP_200_OK, content_type="application/json")


    def render_course(self, learnable_component: LearnableComponentModel):
        try:
            course_model: CourseModel = learnable_component.coursemodel
            subcomponents = []
            for courseHasLearnableComponentModel in course_model.coursehaslearnablecomponentmodel_set.all():
                subcomponents.append(self.render_course(courseHasLearnableComponentModel.engaged_learnable_component))
            return CourseRenderedDto(
                course_model.id,
                course_model.name,
                course_model.description,
                subcomponents
            )
        except:
            try:
                article_model: ArticleModel = learnable_component.articlemodel
                return ArticleRenderedDto(
                    article_model.id,
                    article_model.name,
                    article_model.contents
                )
            except:
                raise Exception("Invalid type od learnable component")
