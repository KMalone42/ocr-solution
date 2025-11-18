Error caused by upload button was due to no table existing

in trace
`sqlite3.OperationalError: no such table: uploader_uploadedfile`


Per Claude:
"""
Your view calls UploadedFile.objects.create() (line 18 in views.py)
Django tries to INSERT into the database
SQLite responds: "I don't have a table called uploader_uploadedfile"

The table name uploader_uploadedfile follows Django's convention:

uploader = your app name
_ = separator
uploadedfile = your model name (lowercase)
"""



```bash
python manage.py makemigrations uploader
python manage.py migrate
```

### What these do
`makemigrations` - Creates a migration file that tells Django "create the uploader_uploadedfile table"
`migrate` - Actually creates the table in your database

-------------------------------------------------------------------------------

So what now...
Now we have this error

"""
Using the URLconf defined in ocr_thing.urls, Django tried these URL patterns, in this order:

    admin/
    upload/ [name='upload']

The current path, success/url/, didn’t match any of these.
"""

this means I should make a simple success/url/ page that basically tells the user
    "files successfully uploaded." 
