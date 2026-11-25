# Para que o <input type="datetime-local"> carregue corretamente o valor do banco na tela de edição (UpdateView), no seu settings.py verifique se USE_L10N não está sobrescrevendo o formato ISO, ou garanta que a view passe o dado no formato YYYY-MM-DDTHH:MM (o format='%Y-%m-%dT%H:%M' que já coloquei nos widgets acima resolve isso na maioria dos casos).
from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#busca as variaveis de ambiente em .env
load_dotenv( BASE_DIR / '.env' )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
SECRET_KEY =os.getenv('SECRET_KEY') #'django-insecure-qq28_-gw_$b4s+_#)ml-%e(ksrqr@-q+rql4(0u43*x!y$%k+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#coloque * em ALLOWED_HOSTS permitir qualquer dispositivo 
# na rede local acesse essa aplicacao
#e tem que rodar assim:
#   python manage.py runserver 0.0.0.0:8000
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    #PADRAO NA INSTALACAO DO DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APPS DO AUTENTICADOR ALLAUTH
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # MEUS APPS
    'gcms',
    'boletim',

    # adicionados 
    'django_cotton'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]
    
ROOT_URLCONF = 'core.urls'

# LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True, #o que nao achar em dirs, vai procurar nas pastas templates de cada app do projeto
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Em desenvolvimento, isto faz o Django mostrar o email no terminal em vez de tentar enviar de verdade
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# O email que vai aparecer como remetente nos testes
DEFAULT_FROM_EMAIL = 'alexandreinformatica@yahoo.com.br'

#----AUTENTICACAO COM ALLAUTH
# Do not add ModelBackend solely for username login in Django admin;
# its login view is not rate limited.
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1

# 1. Define COMO o utilizador pode fazer login (Username, Email ou Ambos)
# Opções possíveis: 'username' | 'email' | 'username_email'
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_LOGIN_METHODS = {'username', 'email'}

# 2. Torna o preenchimento do email obrigatório no registo (Signup)
# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

# 3. Define se o email precisa de ser verificado por link enviado por correio
# Opções: 'mandatory' (obrigatório) | 'optional' (opcional) | 'none' (nenhuma verificação)
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Coloque 'none' para testes locais para não travar o login

# Faz o logout acontecer imediatamente sem pedir confirmação
ACCOUNT_LOGOUT_ON_GET = True

# Garante que o utilizador é enviado para a Home após sair
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# LOGIN SOCIAL GOOGLE COM ALLAUTH
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }