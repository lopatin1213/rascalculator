from django.shortcuts import render, redirect
from for_adm.models import AppRasCalck, news
from django.http import FileResponse, HttpResponse
from .models import Review
from .forms import ReviewForm
from django.db.models import Avg  # Добавляем необходимые агрегаты
from .forms import VoteForm
from .models import Vote



def poll_view(request):
    # Получаем IP адрес текущего пользователя
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

    # Проверяем, участвовал ли пользователь раньше
    previous_vote = Vote.objects.filter(ip_address=user_ip).exists()

    if previous_vote:
        return redirect('main')  # перенаправление на главную страницу

    form = VoteForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        selected_option = form.cleaned_data['vote_option']
        Vote.objects.create(option=selected_option, ip_address=user_ip)
        return redirect('main')

    context = {'form': form}
    return render(request, 'main_page/poll.html', context)
def main_view(request):
    """Главная страница приложения."""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-id')
    average_rating = Review.objects.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0

    # Остальные части твоего исходного кода
    versions = AppRasCalck.objects.order_by('-version').all()
    the_news = news.objects.all()  # Берем самую свежую запись # Показываем последнюю новость

    context = {
        'versions': versions,
        'news': the_news,
        'reviews': reviews,
        'average_rating': round(float(average_rating), 1),
        'review_form': form,
        'is_main': True
    }
    return render(request, 'main_page/main.html', context)

def download(request):
    versions = AppRasCalck.objects.filter(is_latest=True).first()
    versions = versions.pk
    return redirect(f"version/{versions}")

from django.shortcuts import get_object_or_404


def download_specific_version(request, filename):
    # Получаем объект по имени файла
    version = get_object_or_404(AppRasCalck, file__endswith=filename)
    response = FileResponse(version.file, filename=filename)
    return response

def version_info(request, pk):
    version = get_object_or_404(AppRasCalck, pk=pk)
    return render(request, 'main_page/version_info.html', {"version": version})
