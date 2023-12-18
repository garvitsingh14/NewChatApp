from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"demo.html")

def index(request,group_name):
    print("Group Name ... ",group_name)
    return render(request,"index.html",{'groupname':group_name})

def demo(request):
    return render(request,"demo.html")