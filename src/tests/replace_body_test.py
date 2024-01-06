import sys

sys.path.append("..")
# sys.path.append("./src")

from createTestDoc import create_test_doc
from utils import replace_body_content
from docx_tools import doc_to_string

doc = create_test_doc()

replace_body_content(doc, "Hallo Welt!")

text = doc_to_string(doc)

# print(text)

assert text == """Text oberhalb des GPT-Blocks
Hallo Welt!
Text unterhalb des GPT-Blocks"""