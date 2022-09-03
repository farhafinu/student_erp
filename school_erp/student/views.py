from django.shortcuts import render

# Create your views here.

def student_home(request):
    return render(request,'student/home.html')
def student_marks(request):
    return render(request,'student/marks.html')
def student_exam(request):
    return render(request,'student/exam.html')   
