import sys
sys.path.append(".../src")

#TODO make it wit pip install

from math_demo import (add, add_with_bug)

def test_addition():
    assert add(2, 2) == 4;
    print("Test BASIC ADDITION PASSED")
#
def test_addition_bugged():
    assert add_with_bug(2, 2) == 4;
    assert add_with_bug(0, 0) == 0;
    print("Test BUGGED ADDITION PASSED")
#


if __name__ == "__main__":
    test_addition()
    test_addition_bugged()