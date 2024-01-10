from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from .models import Student, Teacher, User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id']  # Add other fields as needed

class StudentCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    user_type = serializers.CharField()  # Adjust the user_type field accordingly
    student = StudentSerializer()

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        
        user = User.objects.create_user(**validated_data)
        
        # Customize 'user_type' handling according to your requirements
        
        student = Student.objects.create(user=user, **student_data)
        return student
    
    def validate(self, data):
        if not data['user_type']:
            raise serializers.ValidationError("Please Provide a User Type: (student).")
        
        if data['user_type'] != 'student':
            raise serializers.ValidationError("User Type must be (student) for student user registration.")
        
        return data
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['bio']

class TeacherCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    user_type = serializers.CharField()  # Adjust the user_type field accordingly
    teacher = TeacherSerializer()

    def create(self, validated_data):
        teacher_data = validated_data.pop('teacher')
        
        user = User.objects.create_user(**validated_data)
        
        # Customize 'user_type' handling according to your requirements
        
        teacher = Teacher.objects.create(user=user, **teacher_data)
        return teacher
    
    def validate(self, data):
        if not data['user_type']:
            raise serializers.ValidationError("Please Provide a User Type: (teacher).")
        
        if data['user_type'] != 'teacher':
            raise serializers.ValidationError("User Type must be (teacer) for teacher user registration.")
        
        return data
