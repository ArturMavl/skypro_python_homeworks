
from string_utils import StringUtils

utils = StringUtils()


def test_capitalize():
    res = utils.capitalize ("привет")
    assert res == "Привет"
def test_capitalize_1():
    res = utils.capitalize("ПРИВЕТ")
    assert res == "Привет"
def test_trim():
    res = utils.trim(" привет")
    assert res == "привет"
def test_trim_1():
    res = utils.trim ("при вет")
    assert res == "при вет"
def test_to_list():
    res = utils.to_list("1/2/3/4/5", "/")
    assert res == ["1", "2", "3", "4", "5" ]
def test_to_list_1():
    res = utils.to_list("", "/")
    assert res == []
def test_to_list_2():
    res = utils.to_list("1/2/3/4/5")
    assert res == ["1/2/3/4/5"]
def test_contains():
    res = utils.contains("Привет", "П")
    assert res == True
def test_contains_1():
    res = utils.contains("Привет", "ф")
    assert res == False
def test_delete_symbol():
    res = utils.delete_symbol("Привет", "в")
    assert res == "Приет"
def test_delete_symbol_1():
    res = utils.delete_symbol("Привет", "о")
    assert res == "Привет"
def test_delete_symbol_2():
    res = utils.delete_symbol("12", "o")
    assert res == "12"
def test_starts_with():
    res = utils.starts_with("Привет", "П")
    assert res == True
def test_starts_with_1():
    res = utils.starts_with("Привет", "п")
    assert res == False
def test_starts_with_2():
    res = utils.starts_with("Привет", "Н")
    assert res == False
def test_end_with():
    res = utils.end_with("Привет", "т")
    assert res == True
def test_end_with_1():
    res = utils.end_with("Привет", "Т")
    assert res == False
def test_end_with_2():
    res = utils.end_with("Привет", "з")
    assert res == False
def test_is_empty():
    res = utils.is_empty(" ")
    assert res == True
def test_is_empty_1():
    res = utils.is_empty("r")
    assert res == False
def test_is_empty_2():
    res = utils.is_empty("")
    assert res == True
def test_list_to_string():
    res = utils.list_to_string[1, 2, 3, 4, 5],
    assert res == "1,2,3,4,5"
def test_list_to_string_1():
    res = utils.list_to_string([], ",")
    assert res == ""