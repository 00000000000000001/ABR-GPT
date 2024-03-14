def lese_datei_inhalt(pfad):
    try:
        # Öffne die Datei im Lesemodus ('r') und lese ihren Inhalt
        with open(pfad, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
        return inhalt.strip()
    except FileNotFoundError:
        # Gib eine Fehlermeldung zurück, wenn die Datei nicht gefunden wurde
        return "Datei nicht gefunden."
    except Exception as e:
        # Gib eine allgemeine Fehlermeldung zurück, falls ein anderer Fehler auftritt
        return f"Ein Fehler ist aufgetreten: {e}"