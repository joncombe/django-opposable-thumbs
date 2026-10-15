django-opposable-thumbs
====

Tested on Django 5.2, Python 3.12 and Pillow 12.3. Requires Pillow 9.1+.

Example settings:

```
OPPOSABLE_THUMBS = {
    'CACHE_DIR': os.path.join(BASE_DIR, 'path/to/folder/'),
    'ALLOWED_SOURCES': [
        'http://example.com/static/one/',
        'http://example.com/static/two/',
        'http://somwehereelse.com/',
    ]
}
```
