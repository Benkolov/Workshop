from django.shortcuts import render, redirect, get_object_or_404

from Workshop.core.photo_utils import apply_likes_count, apply_user_liked_photo
from Workshop.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Workshop.pets.models import Pet
from Workshop.pets.utils import get_pet_by_name_and_username


def details_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': PetCreateForm,
    }

    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug)
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug)
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)
