def test_implicit_typecasting():
    x = 10
    y = 3.5
    z = x + y
    assert z == 13.5
    assert isinstance(z, float)


def test_string_to_int():
    assert int("250") == 250


def test_float_to_int():
    assert int(99.99) == 99


def test_list_set_tuple_conversion():
    data = [1, 2, 2, 3, 4, 4, 5]
    assert len(set(data)) == 5


def test_tuple_to_string():
    result = ''.join(['A', 'q', 'i', 'l'])
    assert result == "Aqil"


def test_string_list_set():
    sentence = "python typecasting is very very powerful"
    assert "very" in set(sentence.split())


def test_dict_keys_values():
    student = {'name': 'Aqil', 'age': 23, 'marks': 90}
    assert 'name' in student
    assert student['age'] == 23


def test_type_mixing():
    assert 5 / 2.0 == 2.5


def test_list_str_to_int_sum():
    numbers = ["10", "20", "30", "40"]
    assert sum(int(n) for n in numbers) == 100


def test_nested_conversion():
    assert set(str(122333)) == {'1', '2', '3'}
