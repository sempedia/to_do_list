from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib import messages
# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    priority_choices = Task._meta.get_field('priority').choices
    status_choices = Task._meta.get_field('status').choices
    context = {
        'tasks': tasks,
        'priority_choices': priority_choices,
        'status_choices': status_choices,
    }
    return render(request, 'tasks/task_list.html', context)


def create_task(request):
    priority_choices = Task._meta.get_field('priority').choices
    status_choices = Task._meta.get_field('status').choices

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        task = Task(title=title, description=description, priority=priority, status=status)
        task.save()

        messages.success(request, 'Task added successfully!')
        return redirect('tasks:task_list')

    context = {
        'priority_choices': priority_choices,
        'status_choices': status_choices,
    }

    return render(request, 'tasks/task_list.html', context)




def update_task(request, task_id):
    # Ensure the task_id is a valid integer, otherwise redirect with an error message
    try:
        task_id = int(task_id)
    except ValueError:
        messages.error(request, 'Invalid task ID.')
        return redirect('task_list')

    # Get the task object with the provided task_id
    task = get_object_or_404(Task, id=task_id)

    priority_choices = Task._meta.get_field('priority').choices
    status_choices = Task._meta.get_field('status').choices

    if request.method == 'POST':
        for field in ['title', 'description', 'priority', 'status']:
            if field in request.POST:
                setattr(task, field, request.POST[field])

        if 'completed' in request.POST:
            if task.status == 'Complete':
                task.status = 'Incomplete'
            else:
                task.status = 'Complete'
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('tasks:task_list')

    # For GET requests, display the update_task form
    context = {
        'task': task,
        'priority_choices': priority_choices,
        'status_choices': status_choices,
    }
    return render(request, 'tasks/update_task.html', context)



def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, 'Task deleted succefully!')
    return redirect('tasks:task_list')


def reset_tasks(request):
    if request.method == 'POST':
        # Delete all tasks in the database
        Task.objects.all().delete()

        # Add a success message
        messages.success(request, 'All tasks have been reset successfully!')
        return redirect('tasks:task_list')

    return render(request, 'tasks/task_list.html')
    