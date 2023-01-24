import pytest
from datetime import datetime
from src.feature_practical_calvin import get_time

name = "Calvin"
timezone = +2

def test_valid_name():
    name = "Calvin"
    user, _, _ = get_time(name, timezone)
    assert type(user) == str

def test_invalid_name():
    name = +2
    with pytest.raises(TypeError):
       get_time(name, timezone)

def test_valid_positive_timezone():
    timezone = +2
    _, current_time, _ = get_time(name, timezone)
    assert int(current_time[:2]) > datetime.utcnow().hour

def test_valid_negative_timezone():
    timezone = -1
    _, current_time, _ = get_time(name, timezone)
    assert int(current_time.split(':')[0]) < datetime.utcnow().hour

def test_invalid_timezone():
    timezone = "+2"
    with pytest.raises(TypeError):
       get_time(name, timezone)


