from pathlib import Path

TOMEDO_CACHE_PROXY = str(Path.home()) + "/.tomedoCache/temporaryFiles/proxy/"
API_KEY = "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"
# API_KEY = "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"
GPT_MODEL = "gpt-3.5-turbo"

# Prompt-Generatoren:
# https://easy-peasy.ai/de/templates/chatgpt-prompt-generator
# https://neuralwriter.com/de/prompt-tool/

PROMPT = """
Als Experte für medizinische Fachtexte, sollen Sie einen Arztbrief erstellen.
Der Hauptteil sollte in einzelne Abschnitte unterteilt sein, die jeweils eine präzise Überschrift haben.
Stellen Sie sicher, dass der Arztbrief alle relevanten, vorgegebenen medizinischen Details enthält.
Die Informationen sollten klar und verständlich formuliert sein, damit andere medizinische Fachleute den Arztbrief
problemlos lesen und verstehen können. Achten Sie darauf, dass alle medizinischen Abkürzungen ausgeschrieben und erläutert werden,
um Missverständnisse zu vermeiden.
Bitte entfernen Sie die Überschrift "Arztbrief" aus dem Text.
Bitte entfernen Sie den Gruß "Mit freundlichen Grüßen" aus dem Text.
Bitte stellen Sie auch sicher, dass der Rest des Briefes unverändert bleibt.
Achten Sie bitte insbesondere darauf, dass Sie nichts generierst was nicht in den vorgegebenen Daten enthalten ist.
"""
