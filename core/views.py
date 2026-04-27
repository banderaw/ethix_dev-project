from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Todo, User


def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        user = User.objects.first()

        Todo.objects.create(
            title=title,
            description=description,
            user=user
        )

        return HttpResponse("Todo Created Successfully")

    return render(request, "create.html")


def get_todos(request):
    todos = Todo.objects.all()
    newtodos = []
    for todo in todos:
        newtodos.append(
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "user": todo.user.username,
            }
        )

    return render(request, "index.html", {"todo_lists": newtodos})


def get_todo_by_id(request, todo_id):
    find_todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, "detail.html", {"todo": find_todo})


def update_todo(request):
    return HttpResponse("Update a todo")


def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()
        return redirect("core:get_todos")
        return HttpResponse("Invalid request", status=400)