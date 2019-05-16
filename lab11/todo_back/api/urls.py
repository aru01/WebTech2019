from django.urls import path

from . import views

urlpatterns = [
    path('task_lists/', views.list),
    path('task_lists/<int:pk>/', views.list_id),
    path('task_lists/<int:pk>/tasks/', views.task),
    path('tasks/<int:pk>', views.task_detail)
]
