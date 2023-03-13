from django.shortcuts import render,redirect

from task_app.models import Task


def task_list (request):
    tasks = Task.objects.all()

    return render(request,
           'task_app/lista.html',
            context= {'tasks': tasks }
           )



def task_create (request):
    if request.method == "POST":
        data = request.POST

        Task.objects.create(
            name =  data.get('name'),
            adress = data.get('adres'),
        )

    return render (request,
                   'task_app/add.html')


def task_detail(request):
    if request.method == "GET":
        member = request.GET.get('member')
    members = Task.objects.filter(name = member)

    return render(request,
                  'task_app/detail.html',
                  context = {"members":members,"member":member},
                  )


def task_delete(request ):

    return render(request,
                  'task_app/layout.html',

                  )

def task_read(request,id):
    task= Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()
        return redirect('task_app:task_list')

    return render(request,
                  "task_app/read.html",
                  context= {'task':task},
                  )