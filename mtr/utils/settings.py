from django.conf import settings


def strip_media_root(path):
    if path:
        return path.split(settings.MEDIA_ROOT.rstrip('/'))[1].lstrip('/')
    return path


def getattr_with_prefix(prefix, name, default):
    """Custom settings prefix for avoiding name colissions"""

    prefix = getattr(settings, '{}_SETTINGS_PREFIX'.format(prefix), prefix)

    default.update(getattr(settings, '{}_{}'.format(prefix, name), {}))

    return default

THEMES = getattr_with_prefix('THEMES', 'SETTINGS', {
    'mtr.sync': {
        'DIR': 'mtr/sync',
        'THEME': 'default',
        'USE_IN_RENDER': True,
    }
})

GETTEXT = getattr_with_prefix('GETTEXT', 'SETTINGS', {
    'FORMAT': '{}:{}',
})
