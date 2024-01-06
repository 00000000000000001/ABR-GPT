import copy

def doc_to_string(doc):
    res = ""
    for p in doc.paragraphs:
        # print(p.text)
        res += p.text + "\n"
    res = res[:-1]
    return res

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    paragraph._p = paragraph._element = None

def in_which_run_is(m, p):
    if m < 0 or m > len(p.text) - 1:
        return None
    i = 0
    sum = 0
    for run in p.runs:
        sum += len(run.text)
        if sum - 1 >= m:
            return i
        i += 1
    return None


def at_which_position_in_its_run_is(m, p):
    if m < 0 or m > len(p.text) - 1:
        return None
    if m < len(p.runs[0].text):
        return m
    sum = 0
    i = 0
    while sum - 1 < m:
        sum += len(p.runs[i].text)
        i += 1
    k = (sum - 1) - m
    return len(p.runs[i - 1].text) - 1 - k


def cp(m, n, p_src, p_dest):
    if m < 0 or n > len(p_src.text):
        return None
    r_start = in_which_run_is(m, p_src)
    r_finish = in_which_run_is(n, p_src)

    if r_start == None or r_finish == None:
        return None

    for i in range(r_start, r_finish + 1):
        run = p_src.runs[i]
        r_copy = copy.deepcopy(run)._r

        a = 0
        o = len(run.text)
        if i == r_start:
            a = at_which_position_in_its_run_is(m, p_src)
        if i == r_finish:
            o = at_which_position_in_its_run_is(n, p_src) + 1

        r_copy.text = r_copy.text[a:o]
        p_dest._p.append(r_copy)


def remove_run(run, p):
    i = len(p.runs) - 1
    while i >= 0:
        if p.runs[i]._r == run._r:
            p._p.remove(p.runs[i]._r)
            return run
        i -= 1
    return None


def rm(m, n, p):
    if m < 0 or n > len(p.text) - 1:
        return

    r_start = in_which_run_is(m, p)
    r_finish = in_which_run_is(n, p)

    if r_start == None or r_finish == None:
        return None

    a = -1
    o = -1
    arr = []

    for i in range(r_start, r_finish + 1):
        run = p.runs[i]

        if i == r_start:
            a = at_which_position_in_its_run_is(m, p)
        if i == r_finish:
            o = at_which_position_in_its_run_is(n, p)
        if i > r_start and i < r_finish:
            arr.append(run)

    if r_start == r_finish:
        p.runs[r_start].text = p.runs[r_start].text[:a] + p.runs[r_finish].text[o + 1 :]
    else:
        p.runs[r_start].text = p.runs[r_start].text[:a]
        p.runs[r_finish].text = p.runs[r_finish].text[o + 1 :]
    for run in reversed(arr):
        remove_run(run, p)


def mv(m, n, p_src, p_dest):
    cp(m, n, p_src, p_dest)
    rm(m, n, p_src)
