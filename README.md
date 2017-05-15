# mms_noiseapi

line 81 in mms_noiseapi/settings.py 

```
DATABASES = { 
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBNAME',                          # Edit me
        'USER': 'USERNAME',                        # Edit me
        'PASSWORD': 'PASSWORD',                    # Edit me
        'HOST': '', 
        'POST': '', 
    }   
}
```

```
./manage.py makemigrations app_noiseapi
./manage.py migrate
./manage.py runserver 0.0.0.0:80

http://localhost/api/noise/
```
