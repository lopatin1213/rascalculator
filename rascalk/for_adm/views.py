from django.shortcuts import render
from .models import UserPro

def pro_users(request):
    pro_users = UserPro.objects.filter(is_pro=True)
    return render(request, 'for_adm/pro.html', {'pro_users': pro_users})


def check_user(request, username, secret_key):
    try:
        user_pro = UserPro.objects.get(user=username, secret_key=secret_key)
        if user_pro.is_pro:
            return render(request, 'for_adm/pro_user.html', {'user_pro': user_pro})
        else:
            return render(request, 'for_adm/not_pro_user.html')
    except UserPro.DoesNotExist:
        return render(request, 'for_adm/user_not_found.html')