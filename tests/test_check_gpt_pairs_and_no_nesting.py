import sys
sys.path.append('../')
sys.path.append('./')
import main

def test_check_gpt_pairs_no_nesting1():
    str = ""
    assert main.check_gpt_pairs_and_no_nesting(str) == True


def test_check_gpt_pairs_no_nesting2():
    str = "<gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False


def test_check_gpt_pairs_no_nesting3():
    str = "</gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False


def test_check_gpt_pairs_no_nesting4():
    str = "<gpt><gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False


def test_check_gpt_pairs_no_nesting5():
    str = "</gpt></gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False


def test_check_gpt_pairs_no_nesting6():
    str = "</gpt><gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False


def test_check_gpt_pairs_no_nesting7():
    str = "<gpt></gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == True


def test_check_gpt_pairs_no_nesting8():
    str = "<gpt><gpt></gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False


def test_check_gpt_pairs_no_nesting9():
    str = "<gpt><gpt></gpt></gpt>"
    assert main.check_gpt_pairs_and_no_nesting(str) == False