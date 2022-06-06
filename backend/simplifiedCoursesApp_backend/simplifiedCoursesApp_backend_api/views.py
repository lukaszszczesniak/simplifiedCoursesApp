from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import TestModel
from .serializers import TestModelSerializer


class TestModelListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the testModel items for given requested user
        '''
        testModels = TestModel.objects.filter(user=request.user.id)
        serializer = TestModelSerializer(testModels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the TestModel with given testModel data
        '''
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = TestModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestModelDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, testmodel_id, user_id):
        '''
        Helper method to get the object with given testmodel_id, and user_id
        '''
        try:
            return TestModel.objects.get(id=testmodel_id, user=user_id)
        except TestModel.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, testmodel_id, *args, **kwargs):
        '''
        Retrieves the TestModel with given testmodel_id
        '''
        testmodel_instance = self.get_object(testmodel_id, request.user.id)
        if not testmodel_instance:
            return Response(
                {"res": "Object with testmodel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TestModelSerializer(testmodel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, testmodel_id, *args, **kwargs):
        '''
        Updates the tedstmodel item with given testmodel_id if exists
        '''
        testmodel_instance = self.get_object(testmodel_id, request.user.id)
        if not testmodel_instance:
            return Response(
                {"res": "Object with testmodel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = TestModelSerializer(instance=testmodel_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, testmodel_id, *args, **kwargs):
        '''
        Deletes the testmodel item with given testmodel_id if exists
        '''
        testmodel_instance = self.get_object(testmodel_id, request.user.id)
        if not testmodel_instance:
            return Response(
                {"res": "Object with testmodel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        testmodel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
