
from django.urls import path
from.import views
urlpatterns = [
    path('home', views.student_home,name='home'),
    path('marks',views.student_marks,name='marks'),
    path('exam',views.student_exam,name='exam')
]