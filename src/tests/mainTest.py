import sys
sys.path.append("..")

from docx import Document
from createTestDoc import create_test_doc
from main import run

document = create_test_doc()
run(document)
# assert len(document.paragraphs) == 1