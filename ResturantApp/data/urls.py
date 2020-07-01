from django.urls import path

from . import views

urlpatterns = [
    path('Home/', views.home , name='homepage'),
    path('del/<int:id>/', views.delete_student , name='deleted'),
    path('add_std/', views.add_student , name='add_s'),
    path('add_pro/', views.add_professor, name='add_p'),
    path('add_cla/', views.add_Class, name='add_c'),
    path('edit_std/<int:id>/', views.edit_student, name='edit_s'),

]