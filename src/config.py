from pathlib import Path

TOMEDO_CACHE_PROXY = str(Path.home()) + "/.tomedoCache/temporaryFiles/proxy/"
SQLITE_FILE_NAME = str(Path(__file__).parent.resolve()) + "/../sqlite.db"