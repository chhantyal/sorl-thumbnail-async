from sorl.thumbnail.base import ThumbnailBackend
from sorl.thumbnail import default
from sorl.thumbnail.images import ImageFile, DummyImageFile

class AsyncThumbnailBackend(ThumbnailBackend):
    def get_thumbnail(self, file_, geometry_string, **options):
        source = ImageFile(file_)
        for key, value in self.default_options.items():
            options.setdefault(key, value)
        name = self._get_thumbnail_filename(source, geometry_string, options)
        thumbnail = ImageFile(name, default.storage)
        cached = default.kvstore.get(thumbnail)
        if cached:
            return cached
        # We don't check if thumbnail exists as sorl-thumbnail does. It becomes
        # very costly for remote storages.
        # Furthermore, I have added following code to reduce/prevent duplicate
        # tasks in celery. It's hacky.
        try:
            default.kvstore.get_or_set(source)
            default.kvstore.set(thumbnail, source)
            return thumbnail
        except IOError:
            pass
        # Finally, if there is no thumbnail, we create one.
        from .tasks import create_thumbnail
        job = create_thumbnail.delay(file_, geometry_string, **options)
        # Sometimes thumbnail generation takes quite some time, show dummy.
        if job:
            return DummyImageFile(geometry_string)