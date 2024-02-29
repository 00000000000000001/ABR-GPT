from docx_tools import rm, delete_paragraph, in_which_run_is
import hashlib
import sqlite3
import config


def parse_body(doc):
    opened = False
    closed = False
    res = ""
    l = 0
    while l < len(doc.paragraphs):
        p = doc.paragraphs[l]
        i = 0
        while i < len(p.text):
            if i < len(p.text) - 1 and p.text[i : i + 2] == "{{":
                opened = True
                i += 2
            elif i < len(p.text) - 1 and p.text[i : i + 2] == "}}":
                closed = True
            if opened and not closed:
                res += p.text[i]
            i += 1
        l += 1
    if closed:
        return res
    else:
        return None


def delete_body_content(doc):
    opened = False
    closed = False
    l = 0
    while l < len(doc.paragraphs):
        p = doc.paragraphs[l]

        if len(p.text) == 0 and opened and not closed:
            delete_paragraph(p)
            l -= 1
            continue

        i = 0
        while i < len(p.text):
            if i < len(p.text) - 1 and p.text[i : i + 2] == "{{":
                opened = True
                i += 2
            if i < len(p.text) - 1 and p.text[i : i + 2] == "}}":
                closed = True
            if opened and not closed:
                rm(i, i, p)
                i -= 1
                if len(p.text) == 0:
                    delete_paragraph(p)
                    l -= 1
                    break
            i += 1
        l += 1


def replace_body_content(doc, string):
    l = 0
    delete_body_content(doc)
    while l < len(doc.paragraphs):
        p = doc.paragraphs[l]
        i = 0
        while i < len(p.text):
            if i < len(p.text) - 1 and p.text[i : i + 2] == "{{":
                rm(i, i + 1, p)
                i -= 1
                # p.text += string
            if i < len(p.text) - 1 and p.text[i : i + 2] == "}}":
                rm(i, i, p)
                # if p.text == "":
                #     delete_paragraph(p)
                # return
                run_i = in_which_run_is(i, p)
                p.runs[run_i].text = string
            i += 1
        l += 1


def get_hash(file):
    with file:
        bytes = file.read()
        hash = hashlib.md5(bytes).hexdigest()
    return hash

def is_registered(hash):
    con = sqlite3.connect(config.SQLITE_FILE_NAME)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hashes(hash)")
    res = cur.execute(f"SELECT hash FROM hashes WHERE hash = '{hash}'")
    is_registered = res.fetchone() is not None
    con.close()
    return is_registered