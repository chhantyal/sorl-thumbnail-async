sorl-thumbnail-async
====================

Asynchronous thumbnailing app in django with remote storages like S3. This is modifications of some parts of [sorl-thumbnail], which is a bit slow when used with remote storages. 

- Celery is used to create thumbnail asynchronously.
- Thumbnails are pregenerated and cached.
- Thumbnail sizes and options are specified in one place (your settings file).

Install
-------

`pip install sorl-thumbnail-async`

Add 'thumbnail' to your INSTALLED_APPS.

Dependencies
------------
`pip install django`   
`pip install django-celery`   
`pip install PIL`   
`pip install sorl-thumbnail`

Usage
-----

In your `settings.py` add an option called `THUMBNAIL_OPTIONS_DICT`, defining all your thumbnail sizes:

	THUMBNAIL_OPTIONS_DICT = {
	        'small': {
	                'geometry': '140x140',
	                'crop': 'center'
	        }
	    }

In your models, use `thumbnail.models.AsyncThumbnailMixin` as a baseclass. Make sure that your model inherits
from AsyncThumbnailMixin first. This will call celery task on save(), and create one or more thumbnails
from the specified image field. Use class variable `image_field_name` to configure the field that
contains the image. Defaults to `picture`.

Example:

	from sorl import thumbnail
	from thumbnail.models import AsyncThumbnailMixin
	
	
	class MyModel(AsyncThumbnailMixin, models.Model):
	    image_field_name = 'image'
	
	    image = thumbnail.ImageField(upload_to='my_model/')

In templates:

	{% load thumbnail_tags %}
	{% thumbnail item.picture small as im %}
	<img src"{{ im.url }}">
	{% endthumbnail %}

Settings
--------
You can add as many sizes and option as needed. It is a python dictionary. 

	THUMBNAIL_OPTIONS_DICT = {
	        'small': {
	                'geometry': '140x140',
	                'crop': 'center'
	        }
	    }

[sorl-thumbnail]: https://github.com/sorl/sorl-thumbnail