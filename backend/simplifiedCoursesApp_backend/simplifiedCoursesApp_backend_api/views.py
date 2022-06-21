from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CourseModel  # , TestModel
from .serializers import *


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
#
#
# class TestModelListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]
#
#     # 1. List all
#     @extend_schema(request=None, responses=TestModelSerializer)
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the testModel items for given requested user
#         '''
#         testModels = TestModel.objects.filter(user=request.user.id)
#         serializer = TestModelSerializer(testModels, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the TestModel with given testModel data
#         '''
#         data = {
#             'task': request.data.get('task'),
#             'completed': request.data.get('completed'),
#             'user': request.user.id
#         }
#         serializer = TestModelSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TestModelDetailApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_object(self, testmodel_id, user_id):
#         '''
#         Helper method to get the object with given testmodel_id, and user_id
#         '''
#         try:
#             return TestModel.objects.get(id=testmodel_id, user=user_id)
#         except TestModel.DoesNotExist:
#             return None
#
#     # 3. Retrieve
#     def get(self, request, testmodel_id, *args, **kwargs):
#         '''
#         Retrieves the TestModel with given testmodel_id
#         '''
#         testmodel_instance = self.get_object(testmodel_id, request.user.id)
#         if not testmodel_instance:
#             return Response(
#                 {"res": "Object with testmodel id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         serializer = TestModelSerializer(testmodel_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     # 4. Update
#     def put(self, request, testmodel_id, *args, **kwargs):
#         '''
#         Updates the tedstmodel item with given testmodel_id if exists
#         '''
#         testmodel_instance = self.get_object(testmodel_id, request.user.id)
#         if not testmodel_instance:
#             return Response(
#                 {"res": "Object with testmodel id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'task': request.data.get('task'),
#             'completed': request.data.get('completed'),
#             'user': request.user.id
#         }
#         serializer = TestModelSerializer(instance=testmodel_instance, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # 5. Delete
#     def delete(self, request, testmodel_id, *args, **kwargs):
#         '''
#         Deletes the testmodel item with given testmodel_id if exists
#         '''
#         testmodel_instance = self.get_object(testmodel_id, request.user.id)
#         if not testmodel_instance:
#             return Response(
#                 {"res": "Object with testmodel id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         testmodel_instance.delete()
#         return Response(
#             {"res": "Object deleted!"},
#             status=status.HTTP_200_OK
#         )
