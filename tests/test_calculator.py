import programs.calculator as calculator

def test_addition():
    assert calculator.addition(4,3) == 7 #assert tests things when python -m pytest [testfile] --cov=[file] is run
    assert calculator.addition(5,3) == 8
    assert calculator.addition(7,60) == 67
    assert calculator.addition(89,1) == 90
    assert calculator.addition(90, 91) == 181

def test_subtraction():
    assert calculator.subtraction(4,3) == 1 #assert tests things when python -m pytest [testfile] --cov=[file] is run
    assert calculator.subtraction(5,3) == 2
    assert calculator.subtraction(7,60) == -53
    assert calculator.subtraction(89,1) == 88
    assert calculator.subtraction(90, 91) == -1

def test_multiplication():
    assert calculator.multiplication(4,3) == 12 #assert tests things when python -m pytest [testfile] --cov=[file] is run
    assert calculator.multiplication(5,3) == 15
    assert calculator.multiplication(7,60) == 420
    assert calculator.multiplication(89,1) == 89
    assert calculator.multiplication(90, 91) == 8190

def test_division():
    assert calculator.division(12,3) == 4 #assert tests things when python -m pytest [testfile] --cov=[file] is run
    assert calculator.division(15,3) == 5
    assert calculator.division(420,60) == 7
    assert calculator.division(89,1) == 89
    assert calculator.division(8190, 91) == 90