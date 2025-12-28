from django.shortcuts import render, redirect

# Create your views here.
from for_adm.models import AndroidApp, news

def view(request):
    # Остальные части твоего исходного кода
    versions = AndroidApp.objects.order_by('-version').all()
    the_news = news.objects.all()  # Берем самую свежую запись # Показываем последнюю новость

    context = {
        'versions_admin': versions,
        'news': the_news,
        'is_main': False,
        'is_android': True
    }
    return render(request, 'android/main.html', context)
def download(request):
    versions = AndroidApp.objects.filter(is_latest=True).first()
    versions = versions.pk
    return redirect(f"version/{versions}")
from django.shortcuts import get_object_or_404
def version_info_android(request, pk):
    version = get_object_or_404(AndroidApp, pk=pk)
    return render(request, 'main_page/version_info.html', {"version": version})