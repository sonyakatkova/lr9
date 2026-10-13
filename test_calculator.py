import pytest
from calculator import Calculator


# Фикстура — создаёт свежий объект перед каждым тестом
@pytest.fixture
def calc():
    return Calculator()


# ADD
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (-5, -5, -10),
    (2.5, 3.5, 6.0),
    (100, 200, 300),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


# SUBTRACT
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (10, 20, -10),
    (2.5, 1.5, 1.0),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# MULTIPLY
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 100, 0),
    (-2, 3, -6),
    (-2, -3, 6),
    (1.5, 2, 3.0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# DIVIDE
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (-10, 2, -5.0),
    (1, 3, 1 / 3),
    (0, 5, 0.0),
])
def test_divide_ok(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


def test_divide_by_zero_raises(calc):
    """Деление на ноль должно бросать ValueError."""
    with pytest.raises(ValueError):
        calc.divide(10, 0)


def test_divide_by_zero_message(calc):
    """Проверяем, что сообщение об ошибке содержит нужный текст."""
    with pytest.raises(ValueError, match="На ноль делить нельзя"):
        calc.divide(5, 0)


# IS_PRIME_NUMBER
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (1, False),
    (0, False),
    (-7, False),
    (4, False),
    (9, False),
    (15, False),
    (100, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected


def test_is_prime_number_wrong_type(calc):
    """Нецелое число должно бросать TypeError."""
    with pytest.raises(TypeError):
        calc.is_prime_number(2.5)


# ДОП. ПРИМЕРЫ (негативные)
def test_divide_by_zero_with_negative(calc):
    with pytest.raises(ValueError):
        calc.divide(-10, 0)


def test_add_with_strings(calc):
    """Проверяем, что add не умеет работать со строками — ловим TypeError."""
    with pytest.raises(TypeError):
        calc.add("1", 2)