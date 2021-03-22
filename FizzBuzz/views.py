from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from FizzBuzz.models import FizzBuzz
from FizzBuzz.serializers import FizzBuzzSerializer


class CheckCountView(APIView):
    # Application automatically creates first object with id=1.
    # This object is used in future for new parameters.
    def get(self, request, count, *args, **kwargs):
        # It is assumed that the game will from 1, and only positive integers will be used.
        if(count <= 0):
            return Response({'result': 'invalid input'}, status=status.HTTP_400_BAD_REQUEST)
        result = self.check_count(count)
        return Response({'result': result}, status=status.HTTP_200_OK)

    def check_count(self, count=None):
        # This function takes count as an argunemt from the user.
        # Function will use last stored database values of Fizz and Buzz.
        # It will evaluate count against database values and returns output.
        try:
            obj = FizzBuzz.objects.get(id=1)
        except:
            obj = FizzBuzz.objects.create(id=1)
            obj.save()
        fizz_name = obj.fizz_name
        buzz_name = obj.buzz_name
        fizz_count = obj.fizz_count
        buzz_count = obj.buzz_count
        if(count % fizz_count == 0 and count % buzz_count == 0):
            return f'{fizz_name}{buzz_name}'
        if(count % fizz_count == 0):
            return fizz_name
        if(count % buzz_count == 0):
            return buzz_name
        return count


class ChangeParamsView(APIView):
    def patch(self, request, format=None, *args, **kwards):
        # Default fields of an object are created automatically when object is created.
        # If user try to use change url at first then following code will create
        # an object with default parameters.
        try:
            try:
                obj = FizzBuzz.objects.get(id=1)
            except:
                obj = FizzBuzz.objects.create(id=1)
                obj.save()

            serializer = FizzBuzzSerializer(
                obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({'result': 'success'}, status=status.HTTP_200_OK)
        except:
            return Response({'result': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)
