from django.shortcuts import render,HttpResponse

# Create your views here.
def intro(request):
    return render(request,'index.html')

def education(request):
    return render(request,'education.html')

def work(request):
    return render(request,"work.html")

def awards(request):
    return render(request,"awards.html")

def contact(request):
    return render(request,"contact.html")

def projects(request):
    return render(request,"projects.html")

def skills(request):
    return render(request,"skills.html")