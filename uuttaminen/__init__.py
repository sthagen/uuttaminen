# [[[fill git_describe()]]]
__version__ = '2023.1.28+parent.4479c01b'
# [[[end]]] (checksum: c8b416cca66bd2439f169bb8e12cb1a3)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
