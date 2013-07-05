from copy import copy
from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver

from .tasks import create_thumbnail

class AsyncThumbnailMixin(object):
    image_field_name = 'picture'

    def call_upload_task(self):
        for name, options in settings.THUMBNAIL_OPTIONS_DICT.iteritems():
            opt = copy(options)
            geometry = opt.pop('geometry')
            create_thumbnail.delay(getattr(self, self.image_field_name), geometry, **opt)

    def save(self, *args, **kwargs):
        super(AsyncThumbnailMixin, self).save(*args, **kwargs)
        self.call_upload_task()
