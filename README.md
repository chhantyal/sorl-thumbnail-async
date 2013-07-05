sorl-thumbnail-async
====================

Asynchronous thumbnailing app in django with remote storages like S3. This is modifications of some parts of [sorl-thumbnail], which is a bit slow when used with remote storages. 

- Celery is used to create thumbnail asynchronously.
- Thumbnails are pregenerated and cached.
- Thumbnail options are specified in setting file.

Install
-------

`pip install sorl-thumbnail-async`

Add 'thumbnail' in INSTALLED_APPS.

Dependencies
------------
`pip install django`   
`pip install django-celery`   
`pip install PIL`   
`pip install sorl-thumbnail`

Usage
-----

In models, use `AsyncThumbnailMixin` inherit from. 
This will call celery task on save(), and create thumbnail from specified image field. 

In templates,  
`{% load thumbnail %}`   
`{% thumbnail item.picture small as im %}`  
`...<img src"im.url">`  
`{% endthumbnail %}`

[sorl-thumbnail]: https://github.com/sorl/sorl-thumbnail