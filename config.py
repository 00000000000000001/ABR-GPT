from pathlib import Path
import utils

TOMEDO_CACHE_PROXY = str(Path.home()) + "/.tomedoCache/temporaryFiles/proxy/"
API_KEY = utils.lese_datei_inhalt("/Users/jonas/Documents/git/ABR-GPT_V2/api_key.txt")
ASS_KEY = utils.lese_datei_inhalt("/Users/jonas/Documents/git/ABR-GPT_V2/asst_key.txt")