from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def movie_listing(request):
    movies = Movie.objects.all()
    return render(request, 'movie_listing.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)  # Pass request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('movie_listing')  # Redirect to the movie listing page after successful creation
    else:
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})


def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            # return redirect('movie_detail', pk=pk)  # Redirect to movie detail page after successful update
            return redirect('movie_detail', movie_id=pk)  # Redirect to the movie detail page
    else:
        form = MovieForm(instance=movie)
    return render(request, 'update_movie.html', {'form': form, 'movie': movie})



def delete_movie(request, pk):
    # Get the movie object by its primary key (pk)
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        # Delete the movie
        movie.delete()
        # Redirect to the movie listing page after deletion
        return redirect('movie_listing')
    
    # If the request method is not POST, render the confirmation page
    return render(request, 'delete_movie.html', {'movie': movie})