from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'main/upload_photo.html', {'form': form})

def photo_list(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'main/photo_list.html', {'photos': photos})
