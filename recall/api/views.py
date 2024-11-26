from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .forms import NoteForm
from .models import Note
from .decorators import user_is_note_owner


@login_required(login_url='logIn')
#find a way to redirect directly to home page after sign up without taking to log in page
def home(request):
    template_name='home.html'
    return render(request, template_name)


@login_required(login_url='logIn')
def createNote(request):
    form = NoteForm()
    context = {'form':form}
    template_name='createNote.html'
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form_object = form.save(commit=False)
            form_object.author = request.user
            form.save()
            return redirect('note-detail', form_object.id)
        else:
            messages.error(request, 'correct the errors below')
    else:
        form = NoteForm()
    return render(request, template_name, context)


@login_required(login_url='login')
@user_is_note_owner
def noteDetail(request, pk, note=None):
    context = {'note':note}
    template_name = 'noteDetail.html'
    return render (request, template_name, context)


@login_required(login_url='login')
@user_is_note_owner
def updateNote(request, pk, note=None):
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note-detail', pk=note.id)
    else:
        form = NoteForm(instance=note)

    context = {'note':note, 'form':form}
    template_name = 'updateNote.html'
    return render (request, template_name, context)


@login_required(login_url='login')
@user_is_note_owner
def deleteNote(request, pk, note=None):
    note.delete()
    return redirect('home')
    

@login_required(login_url='login')
def get_original_notes(request):
    user = request.user
    notes = Note.objects.filter(author=user)
    
    results = [{
        'id': note.id, 
        'title': note.title, 
        'body': note.body,
        'tags': [{'name': tag.name} for tag in note.tags.all()]
    } for note in notes]
    
    return JsonResponse({'results': results})

