### Run the dev server
```bash
python manage.py runserver
```

### Create an app
```bash
python manage.py startapp core
```
This adds:
```kotlin
core/
    admin.py
    apps.py
    models.py
    views.py
    urls.py (you create this yourself)
```


Here’s the **bare-minimum, no-nonsense** way to start a Django project.

## 1. Install Django

```bash
pip install django
```

## 2. Create the project

```bash
django-admin startproject myproject
```

This creates:

```
myproject/
    manage.py
    myproject/
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## 3. Run the development server

```bash
cd myproject
python manage.py runserver
```

## 4. Create an app (optional but typical)

```bash
python manage.py startapp core
```

This adds:

```
core/
    admin.py
    apps.py
    models.py
    views.py
    urls.py (you create this yourself)
```

## 5. Hook the app into settings

Edit `myproject/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

## 6. Add a simple view

`core/views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")
```

## 7. Add URLs

Create file: `core/urls.py`:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
```

Edit project `myproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

## 8. Run it

```bash
python manage.py runserver
```

Open browser → `http://127.0.0.1:8000`

























## Create a new project

```bash
django-admin startproject myproject
```

This creates:

```
myproject/
    manage.py
    myproject/
        settings.py
        urls.py
        asgi.py
        wsgi.py
```


Done.

If you want a minimal setup with templates, models, REST API, or Docker, just say.

