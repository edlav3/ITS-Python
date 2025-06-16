from my_project.weather import check_weather
import pytest

# passed
'''def test_check_weather():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree must be considered as average temperature'

def test2():
    assert check_weather(21.00) == "hot", 'Temperatures greater than 20 degree must be considered as hot'

def test3():
    assert check_weather(5.00) == "cold", "Tempareture lower than 10 degree must be considered as cold"

def test4():
    assert check_weather(13.00) == "average", "Tempareture between 10 and 20 degree must be considered as average temperature"

def test5():
    assert check_weather(30.00) == "hot", "Temperature greater then 20 must considered as hot"
    assert check_weather(11) == "cold", "Temperature lower than 10 must be considered as cold"
    # questa funzione include due test insieme -> non verrano considerati come due test separati ma come un unico test'''


@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
    ])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected