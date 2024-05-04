import pytest
from datetime import datetime
import calendar


def hasClass(time,person):
    if time == "Wednesday" and person == "mum":
        return True
    
    elif time == "Saturday"  and person == "mum" or person == "max":
        return True
    else:
        return False

def test_hasClass():
    assert hasClass("Wednesday", "mum") == True
    assert hasClass("Saturday", "mum") == True
    assert hasClass("Saturday", "max") == True
    assert hasClass("Wednesday", "max") == False
    assert hasClass("Monday", "mum") == False