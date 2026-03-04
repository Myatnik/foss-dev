import sys
sys.path.append("../src")

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
    assert add_with_bug(3,6) == 13;
#
def test_addition_duplicated():
    assert add(2, 3) == 2+3
#
def test_addition_overcomplicated():
    for i in range(0, 2**320):
        for j in range(0, 2**32):
            assert add(i, j) == sum([i, j])
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])
#
def test_addition_reasonable():
    assert add_with_bug(2, 2) == 4;
    assert add_with_bug(0, 0) == 0;
    assert add_with_bug(3, 6) == 9;
    assert add_with_bug(-3, -6) == -9;
    assert add_with_bug(3, -6) == -3;
    assert add_with_bug(3, 0) == 3;
    assert add_with_bug(-3, 0) == -3;
    print("Test BUGGED REASONABLE PASSED")
#
def test_addition_communitative():
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("Test BUGGED COMMUNITATIVE PASSED")
#

if __name__ == "__main__":
    test_addition()
    test_addition_bugged()
    test_addition_duplicated()
    #test_addition_overcomplicated() #DO NOT RUN
    test_addition_reasonable()
    test_addition_communitative()