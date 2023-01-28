# [[[fill git_describe()]]]
__version__ = '2023.1.28+parent.f527a215'
# [[[end]]] (checksum: ea7b5e19e89cdaba6a667f9be2c199e0)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
