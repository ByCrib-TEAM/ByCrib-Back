import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv('MODE', 'PRODUCTION')
BASE_DIR = Path(__file__).resolve().parent.parent

if MODE == 'DEVELOPMENT':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:3000',
    'http://localhost:8000',
    'https://bycrib-back-x7zl.onrender.com'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://bycrib-back-x7zl.onrender.com'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'corsheaders',
    'django_extensions',
    'django_filters',
    'drf_spectacular',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ENDPOINT = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
FILE_UPLOAD_PERMISSIONS = 0o640

CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')

if MODE == 'DEVELOPMENT':
    MY_IP = os.getenv('MY_IP', '127.0.0.1')
    MEDIA_URL = f'http://{MY_IP}:19003/media/'
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
else:
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'app.pagination.CustomPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'PAGE_SIZE': 10,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.getenv("ACCESS_TOKEN_LIFETIME_MINUTES", 15))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME_DAYS", 1))),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": os.getenv("JWT_SIGNING_KEY", SECRET_KEY),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ByCrib API',
    'DESCRIPTION': 'API para o e-commerce ByCrib, com autenticação JWT e integração Cloudinary.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

PASSAGE_APP_ID = os.getenv('PASSAGE_APP_ID', 'app_id')
PASSAGE_API_KEY = os.getenv('PASSAGE_API_KEY', 'api_key')
PASSAGE_AUTH_STRATEGY = 2

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

print(f'\n[SETTINGS] MODO={MODE} | DEBUG={DEBUG} | DB={DATABASES["default"]["ENGINE"]}')
print(f'MEDIA_URL={MEDIA_URL}')