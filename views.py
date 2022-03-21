from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from rest_framework import generics
from .serializers import TaskSerializer
from .serializers import TasklistSerializer
from .serializers import TagSerializer
from .serializers import OwnerSerializer
from .models import Task,Owner,User,Tasklist,Tag
from .forms import TaskCreationForm

from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from todolist.forms import UserCreationForm



class TaskUpdateView(UpdateView):
    models = Task
    template_name = 'CRUD/create.html'

    fields = ["name","description", "completed", "due_date","priority","tasklist","Tag","User"]



def tasks_home(request):
    
    tasks = Task.objects.filter(User=request.user)
    return render(request, 'home.html',{'tasks':tasks})
    def post(self, request):
        task = request.data.get('task')
        # Create an article from the above data
        serializer = TaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({"success": "task '{}' created successfully".format(task_saved.name)})




def get_queryset(self):
    user = self.request.user
    return Task.objects.filter(tasks = User)



class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def create (request):
    error = ''
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = TaskCreationForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'CRUD/create.html', data)



class TagCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class OwnerCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class TasklistCreateView(generics.ListCreateAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer


class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer


class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Create your views here.
