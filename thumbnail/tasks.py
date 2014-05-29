import celery

from sorl.thumbnail import default
from sorl.thumbnail.images import ImageFile

@celery.task
def create_thumbnail(image_file, geometry_string, **options):
    # Note that thumbnail options must be same for a type of thumbnail.
    # Otherwise, different thumbnails are created.
    source = ImageFile(image_file)
    for key, value in default.backend.default_options.items():
            options.setdefault(key, value)
    name = default.backend._get_thumbnail_filename(source, geometry_string, options)
    thumbnail = ImageFile(name, default.storage)
    source_image = default.engine.get_image(source)
    default.backend._create_thumbnail(source_image, geometry_string, options, thumbnail)

    # Need to set size to store in kvstore.
    size = default.engine.get_image_size(source_image)
    source.set_size(size)

    default.kvstore.get_or_set(source)
    default.kvstore.set(thumbnail, source)