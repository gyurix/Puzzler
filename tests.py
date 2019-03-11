from difcalc import *
from operations import *


def prepare_state():
    s = State()
    s.data = [[1, 2, 3], [4, 'm', 5], [6, 7, 8]]
    s.find_pos()
    return s


def test_state_to_string():
    assert str(prepare_state()) == "((1 2 3)(4 m 5)(6 7 8))"


def test_operation_up():
    op = OperationUp()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s2.data == [[1, 'm', 3], [4, 2, 5], [6, 7, 8]]
    assert s2.data == s3.data


def test_operation_down():
    op = OperationDown()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s2.data == [[1, 2, 3], [4, 7, 5], [6, 'm', 8]]
    assert s2.data == s3.data


def test_operation_right():
    op = OperationRight()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s2.data == [[1, 2, 3], [4, 5, 'm'], [6, 7, 8]]
    assert s2.data == s3.data


def test_operation_left():
    op = OperationLeft()
    s = prepare_state()
    s2 = op.apply(s)
    assert s2.data == [[1, 2, 3], ['m', 4, 5], [6, 7, 8]]
    s3 = op.apply(s2)
    assert s2.data == s3.data


def test_equals():
    s = prepare_state()
    s.x = 0
    s.y = 0
    assert prepare_state() == s


def test_dif_calc_incorrect_ep():
    s = prepare_state()
    s2 = prepare_state()
    s2.data = [[3, 2, 1], ['m', 4, 5], [6, 7, 8]]
    assert DifCalcIncorrectEP().apply(s, s2) == 3


def test_dif_calc_dist_from_correct_ep():
    s = prepare_state()
    s2 = prepare_state()
    s2.data = [[3, 2, 1], ['m', 4, 5], [6, 7, 8]]
    assert DifCalcDistanceFromCorrectEP().apply(s, s2) == 5
