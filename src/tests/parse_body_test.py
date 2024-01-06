import sys

sys.path.append("./src")

from createTestDoc import create_test_doc
from utils import parse_body

doc = create_test_doc()

text = parse_body(doc)

# print(text)

assert (
    text
    == """Anamnese, Untersuchung, Indikationsstellung:
    Spontan aufgetretener schmerzloser Gelenkerguss im linksseitigen Kniegelenk
    MRT-Untersuchung zur Darstellung struktureller Veränderungen. 
    Ausführliche schriftliche und mündliche Aufklärung des Patienten über eventuelle Komplikationen der MRT-Untersuchung bei 3 Tesla Feldstärke.Technik:
    Kernspintomographie bei 3 Tesla Feldstärke; Verwendung einer Mehrkanal-Oberflächenspule. 
    Nach Planungssequenzen werden folgende Pulssequenzen durchgeführt:
    PD-gewichtete TSE-Sequenzen mit SPAIR-Fettsuppression in sagittaler, axialer, coronarer Orientierung. Sagittale T1-gewichtete TSE-Sequenzen, isometrische PD-gewichtete 3D-TSE-Sequenzen mit Erzeugung mehrerer multiplanarer Reformationen.Befund:
    Es liegen keine Voruntersuchungen des Kniegelenks zur Korrelation vor. 
    Im medialen Kniegelenkskompartiment sind die Knorpelüberzüge nach medial hin deutlich ausgedünnt bis fehlend, tibialseitig zeigen sich dabei kleinere subcortikale ödematöse und beginnend zystische Veränderungen. 
    An der kniemittigen medialen Femurkondyle zeigt sich ein markanter umschriebener Knorpeldefekt mit deutlichem osteochondralem Begleitödem. Der Innenmeniskus ist zudem deutlich nach medial extrudiert, verschmächtigt und gering aufgefasert; entlang des Hinterhorns zeigen sich markante Auffaserungen im Sinne kleinerer horizontaler Rissbildungen. Geringer ödematöser Reizzustand der angrenzenden posteromedialen Gelenkkapsel
    Weitgehend unauffällige Darstellung der Knorpelüberzüge im patellofemoralen sowie im lateralen Kniegelenkskompartiment. 
    Unauffälliger Außenmeniskus.
    Regelrechte Kreuz- und Kollateralbänder sowie kleinere und mittlere ligamentäre Strukturen. 
    Unauffällige lange Sehnen einschließlich der Quadrizeps- und Patellarsehne.
    Deutlicher Kniegelenkserguss ohne relevante synoviale Hypertrophie oder andere Anzeichen einer entzündlichen Genese.
    Zeichen einer deutlichen Arthrose auch im proximalen Tibiofibulargelenk mit markanter subcortikaler zystischer Läsion und geringem ödematösen Reizzustand.
    Ansonsten regelrechte Darstellung der knöchernen Strukturen sowie der Knochenmarkräume.
    Kräftige Ober- und Unterschenkelmuskulatur.
    Einzelne unspezifische popliteale Lymphknoten, unauffällige poplitealen Gefäße.
    Unauffällige Haut sowie Unterhautfettgewebe.Beurteilung:
    Zeichen einer markanter, deutlichen medialseitigen Gonarthrose.
    Deutlich umschriebener osteochondrale Defekt an der kniemittigen medialen Femurkondyle; aufgrund der scharfkantigen Berandung möglicherweise ursächlich für die akute Reizung des Kniegelenks und den deutlichen akuten Erguss.
    Ausgeprägte meniskodegenerative Veränderungen mit horizontalen Rissbildungen insbesondere entlang des Innenmeniskushinterhorns.
    deutliche arthrotische Veränderungen auch im proximalen Tibiofibulargelenk.Procedere:
    Im Anschluss an die Untersuchung erfolgte die ausführliche Befundbesprechung und Bilddemonstration an Herrn Mustermann."""
)
