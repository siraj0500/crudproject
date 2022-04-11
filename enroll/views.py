from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
# (1) created a view function to render index page, And new items and also shows
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return redirect('addandshow')
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'add_and_show.html', {'form': fm, 'stu': stud})


#  new function for update/edit
def update_data(request, id):
    if request.method == 'POST':  # after edit becomes post,so save and redirect to main
        pi = User.objects.get(id=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')
    else:
        pi = User.objects.get(id=id)   # editing process
        fm = StudentRegistration(instance=pi)
    return render(request, 'update_student.html', {'form': fm})


# new function for delete
def delete_data(request, id):
    if request.method == 'POST':  # pick by id and delete , goes back to home
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')
