from django.conf import settings

# Default sorl-thumbnail backend is overridden. We need to tell which backend to use.
THUMBNAIL_BACKEND = 'sorl-thumbnail-async.thumbnail.backend.AsyncThumbnailBackend'

# Instead of original sorl-thumbnail design, we predefine the thumbnail options
# here and reuse same everywhere. 
DEFAULT_OPTIONS_DICT = {
    'small': {
            'geometry': '140x140',
            'crop': 'center'
    }
}
OPTIONS_DICT = getattr(settings, 'THUMBNAIL_OPTIONS_DICT', DEFAULT_OPTIONS_DICT)