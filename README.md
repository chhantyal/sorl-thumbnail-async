sorl-thumbnail-async
====================

Asynchronous thumbnailing app in django with remote storages like S3. This is modifications of some parts of [sorl-thumbnail], which is a bit slow when used with remote storages. 

- Celery is used to create thumbnail asynchronously.
- Thumbnails are pregenerated and cached.
- Thumbnail options are specified in setting file.

Install
-------

`pip install sorl-thumbnail-async`

Dependencies
------------
`pip install django`   
`pip install django-celery`   
`pip install PIL`   
`pip install sorl-thumbnail`


[sorl-thumbnail]: https://github.com/sorl/sorl-thumbnail