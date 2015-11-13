# a test project
re https://code.djangoproject.com/ticket/25454#comment:2

to reproduce the bug:

```
# get set up
brew install postgres
createdb mydatabase
git clone git@github.com:craigds/django_25454.git
cd django_25454
virtualenv .
. bin/activate 
pip install -r requirements.txt
./manage.py migrate
```

```
./ticket_25454.py
Creating instance with h={'a': 'b'}
...
django.db.utils.ProgrammingError: can't adapt type 'dict'

```
This error happens because of the bug. Let's work around it to create a model instance:

```
./ticket_25454.py --create-with-string
Creating instance with h='"a" => "b"'
Created instance 9
Fetched instance, now m.h == '"a"=>"b"'
```

Note that the `m.h` field is a string and not a dict.
