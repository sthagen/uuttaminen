# [[[fill git_describe()]]]
__version__ = '2023.1.25+parent.62a86a96'
# [[[end]]] (checksum: dee51b111a6a42d8f516f96bed333cb5)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
