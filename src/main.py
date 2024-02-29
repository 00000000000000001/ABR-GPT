from docx import Document
from gpt import abr_gpt

import sys

# Du kannst jetzt Module aus dem neuen Verzeichnis importieren

sys.path.insert(0, "tests")

from docx_tools import doc_to_string
from utils import replace_body_content, parse_body

import config
import glob
import re
import fcntl
import os


def run():
    try:
        if config.API_KEY != "":
            # some var
            msg = ""

            # walk files in tomedo cache
            file_input = config.TOMEDO_CACHE_PROXY
            briefe = glob.glob(file_input + "*.docx")
            for brief in briefe:
                doc = Document(brief)

                pattern = r"\$\[.+\]\$"
                string = doc_to_string(doc)
                if not re.search(
                    pattern, string
                ):  # eine Vorlage gilt als nicht generiert, wenn irgendwo in der Vorlage ein Briefkommando vorkommt
                    pattern = r"\{\{.*?\}\}"
                    if re.search(
                        pattern, string, re.DOTALL
                    ):  # Wenn ein body in der Vorlage markiert ist
                        # tu es!
                        string = parse_body(doc)
                        final_result = abr_gpt(string)
                        replace_body_content(doc, final_result)
                        doc.save(brief)

                        msg += "[✅]" + re.split(r"(.*)/((.+).docx)", brief)[2] + "\n"
        else:
            msg = "Bitte hinterlegen Sie einen API-Key in config.py"
    except:
        msg = "Es gab einen Fehler."
        
    if msg == "":
        msg = "Es wurden keine unfertigen Briefe gefunden. Falls Sie etwas anderes erwartet haben, öffnen Sie bitte Sie den Arztbrief, der erstellt werden soll und versuchen Sie es erneut."

    aktuelles_verzeichnis = os.path.dirname(os.path.realpath(__file__))

    os.system(
        # 'osascript -e \'tell app "Tomedo" to display dialog "'
        # + msg
        # + '" buttons {"OK"} default button "OK"\''
       'osascript -e \'tell app "Tomedo" to display dialog "' + msg + '" buttons {"OK"} with icon {"' + aktuelles_verzeichnis + '/icon.png"}\''       
    )


lock_file_path = "/tmp/my_script.lock"

# Versuchen, einen exklusiven Lock auf der Datei zu setzen
try:
    lock_file = open(lock_file_path, "w")
    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print("Das Skript wird bereits ausgeführt. Beende.")
    sys.exit(1)

# Hier folgt der eigentliche Code des Skripts
try:
    run()
except Exception as e:
    print("Fehler: " + str(e))

# Am Ende den Lock freigeben
fcntl.flock(lock_file, fcntl.LOCK_UN)
lock_file.close()
