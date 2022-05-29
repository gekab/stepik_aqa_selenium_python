# pytest -v --tb=line part3_lesson3_step8_test_abs_project_test.py
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"