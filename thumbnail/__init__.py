from copy import copy

from sorl.thumbnail import get_thumbnail as original_get_thumbnail

from .conf import settings

default_app_config = 'thumbnail.apps.ThumbnailConfig'

def get_thumbnail(file_, name):
    """
    get_thumbnail version that uses aliasses defined in THUMBNAIL_OPTIONS_DICT
    """
    options = settings.OPTIONS_DICT[name]
    opt = copy(options)
    geometry = opt.pop('geometry')

    return original_get_thumbnail(file_, geometry, **opt)
