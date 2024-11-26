from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import Note

def user_is_note_owner(view_func):
    def wrapper(request, pk, *args, **kwargs):
        note = get_object_or_404(Note, id=pk)
        if note.author != request.user:
            return HttpResponseForbidden('You are not allowed to view this note')
        return view_func(request, pk, *args, note, **kwargs)
    return wrapper