from .base import *

#SETTINGFILES_DIRS = {
#    os.path.join(os.path.dirname(BASE_DIR), "settings"),
#}

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "Visitante.static"),
)

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'d9n9gipqcd9ij5',
        'USER': 'clzdcljdlfwjvv',
        'PASSWORD': 'bc057a951154a9a55a5e7e2f0de2ea99b2abc3d796fb3c24e22d81d19b8f7fdf',
        'HOST': 'ec2-3-93-206-109.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


