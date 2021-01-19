from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm


from .models import Task
# Create your views here.

####### Mostra a pagina principal com a Lista de Tarefas
def taskList(request):
    tasks = Task.objects.all().order_by('-create_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})


##### Exibi Tarefas 
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})

### Adicionado uma nova tarefa
def newTask(request):
    ## verficar se method e POST
    if request.method == 'POST':
        form = TaskForm(request.POST)
        ## verificando os dados são validos
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Inserido'
            task.save()
            return redirect('/')

    form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form})


### editar a tarefa

def editTask(request, id):
    task = get_object_or_404(Task, pk =id)
    form = TaskForm(instance=task)


    if(request.method == 'POST'):
        form =TaskForm(request.POST, instance =task)

        ### verificando a validação pra salvar no banco de dados

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form':form, 'task':task})
        
    else:
        return render(request, 'tasks/edittask.html',{'form': form, 'task':task})






def helloworld(request):
    return HttpResponse('rafael Chegou aqui!')


def base(request):
    return render(request, './base.html')

    
   
