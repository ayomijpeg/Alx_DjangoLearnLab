from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'api_project.urls'
SECRET_KEY = 'django-insecure-xyz123!supersecretkey!replace-this-value'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',  # Added DRF
    'api',             # Added your app
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',            # Needed for sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',         # Needed for auth
    'django.contrib.messages.middleware.MessageMiddleware',            # Needed for messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # Use SQLite for simplicity
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

STATIC_URL = '/static/'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DEBUG = True

