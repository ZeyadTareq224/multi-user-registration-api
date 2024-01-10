from djoser.serializers import UserSerializer
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentCreateSerializer, TeacherCreateSerializer  
from .models import User, Student
from django.db import IntegrityError


class StudentRegistrationViewSet(viewsets.ViewSet):
    serializer_class = StudentCreateSerializer
    queryset = Student.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                student = serializer.save()
                response_data = {
                    'message': 'User and Student created successfully',
                    'student_id': student.student_id,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {'error': 'Email already exists. Please use a different email.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherRegistrationViewSet(viewsets.ViewSet):
    serializer_class = TeacherCreateSerializer
    queryset = Student.objects.all()
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                teacher = serializer.save()
                response_data = {
                    'message': 'User and teacher created successfully',
                    'bio': teacher.bio,  # You can customize the response data as needed
                    # Add any other required data to return upon successful creation
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {'error': 'Email already exists. Please use a different email.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)