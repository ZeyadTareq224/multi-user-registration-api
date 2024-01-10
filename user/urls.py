from rest_framework.routers import DefaultRouter
from user.views import StudentRegistrationViewSet, TeacherRegistrationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('registration/student', StudentRegistrationViewSet)
router.register('registration/teacher', TeacherRegistrationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken'))
]
