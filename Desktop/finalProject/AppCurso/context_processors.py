from django.contrib.auth.context_processors import auth
from AppCurso.models import Avatar


def custom_user(request):
    context = auth(request)
    user = context["user"]
    if user.is_authenticated:
        avatar = Avatar.objects.filter(user=user.id).first()
        context['user_avatar'] = avatar
    else:
        context['user_avatar'] = None  # o context['user_avatar'] = "" <---- no me funciona

    return context