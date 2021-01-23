from django.shortcuts import render, get_object_or_404, redirect
##importei o login required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
### importe para validar o formulario
from .forms import TaskForm

## importe para adcionar uma mensagem de faadback ao usuario
from django.contrib import messages
#importe para paginação, dividir as informação por cada pagina
from django.core.paginator import Paginator


from .models import Task
# Create your views here.

####### Mostra a pagina principal com a Lista de Tarefas
@login_required
def taskList(request):
     ### criar a função de pesquisa Search
    search = request.GET.get('search')

    if search:
        #realizando o filtro pela aplicação com case -sensitive
        tasks = Task.objects.filter(title__icontains=search, user = request.user) 
    

    else:
            
        tasks_list = Task.objects.all().order_by('-create_at').filter(user = request.user)
    ## função criada para decidir quantas paginas seram visiveis na pagina principal
        paginator = Paginator(tasks_list, 3) #definir tarefa por pagina 
        page = request.GET.get('page')
        
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})
   


##### Exibi Tarefas 
@login_required
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
            task.user = request.user
            task.save()
            #### retorna uma menssagem para o usuario
            messages.info(request, 'Criando uma nova Tarefa!')
            return redirect('/')

    form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form})


### editar a tarefa
@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk =id)
    
    form = TaskForm(instance=task)


    if(request.method == 'POST'):
        form =TaskForm(request.POST, instance =task)
   
        ### verificando a validação pra salvar no banco de dados

        if(form.is_valid()):

            task.save()
    
                    
            #### retorna uma menssagem para o usuario
            messages.info(request, 'A tarefa foi Editanda!')
            return redirect('/')
  
        else:
       
            return render(request, 'tasks/edittask.html', {'form':form, 'task':task})
           
    else:

        return render(request, 'tasks/edittask.html',{'form': form, 'task':task})


##### criando a função de deletar uma tarefa
@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
## informando mensagem de delete da tarefa
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/')






def helloworld(request):
    return HttpResponse('rafael Chegou aqui!')


def base(request):
    return render(request, './base.html')

    
   
