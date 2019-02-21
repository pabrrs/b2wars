"""
Settings module from b2wars

Will try to read `b2wars.settings.local` settings, but if does not exists,
fallback to `b2wars.settings.docker` settings
"""

try:
    from b2wars.settings.local import *
except ImportError:
    from b2wars.settings.docker import *
