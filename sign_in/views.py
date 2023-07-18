from django.shortcuts import render
from .forms import CreateLogForm
from .models import Student, Logs, Bathroom

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def student(request):   
    form = CreateLogForm()

    if request.method == 'POST':
        form = CreateLogForm(request.POST)
    #     print(form)
    #     # student_id = request.POST.get('student_id')
    #     # form.fields['student_id'].choices = [student_id, student_id]
    #     stu = Student.objects.filter(student_id=form['student_id'])
    #     print(stu)
    #     if form.is_valid():
    #         form.save()
        # log = Logs(data['student_id'])
        #add to admin page
    else:
        form = CreateLogForm()

    return render(request, 'pages/student_login.html', {'form': form})

def logs(request):
    return render(request, 'pages/student_logs.html')


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




