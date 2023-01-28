import sys

from uuttaminen.cli import app

if __name__ == '__main__':
    sys.exit(app(sys.argv[1:]))  # pragma: no cover
