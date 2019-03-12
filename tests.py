from astar import a_star_solve
from difcalc import *
from main import print_path
from operations import *


def prepare_state(data='((1 2 3)(4 m 5)(6 7 8))'):
    return State().load_data(data)


def test_state_to_string():
    assert str(prepare_state()) == '((1 2 3)(4 m 5)(6 7 8))'


def test_operation_up():
    op = OperationUp()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s == prepare_state()
    assert s2.data == [[1, 'm', 3], [4, 2, 5], [6, 7, 8]]
    assert s3 is None


def test_operation_down():
    op = OperationDown()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s == prepare_state()
    assert s2.data == [[1, 2, 3], [4, 7, 5], [6, 'm', 8]]
    assert s3 is None


def test_operation_right():
    op = OperationRight()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s == prepare_state()
    assert s2.data == [[1, 2, 3], [4, 5, 'm'], [6, 7, 8]]
    assert s3 is None


def test_operation_left():
    op = OperationLeft()
    s = prepare_state()
    s2 = op.apply(s)
    s3 = op.apply(s2)
    assert s == prepare_state()
    assert s2.data == [[1, 2, 3], ['m', 4, 5], [6, 7, 8]]
    assert s3 is None


def test_equals():
    s = prepare_state()
    s.x = 0
    s.y = 0
    assert prepare_state() == s


def test_dif_calc_incorrect_ep():
    s = prepare_state()
    s2 = prepare_state('((3 2 1)(m 4 5)(6 7 8))')
    assert DifCalcIncorrectEP(s2).apply(s) == 3


def test_dif_calc_dist_from_correct_ep():
    s = prepare_state()
    s2 = prepare_state('((3 2 1)(m 4 5)(6 7 8))')
    assert DifCalcDistanceFromCorrectEP(s2).apply(s) == 5


def test_a_star_same():
    s1 = prepare_state()
    s2 = prepare_state()
    out = a_star_solve(s1, DifCalcIncorrectEP(s2))
    assert len(out) == 1
    assert out[0] == s2


def test_a_star_one_step():
    s1 = prepare_state()
    s2 = prepare_state('((1 2 3)(m 4 5)(6 7 8))')
    out = a_star_solve(s1, DifCalcIncorrectEP(s2))
    assert len(out) == 2
    assert out[0] == s1
    assert out[1] == s2


def test_a_star_two_step():
    s1 = prepare_state('((1 2 3)(4 5 m)(6 7 8))')
    s_mid = prepare_state()
    s2 = prepare_state('((1 2 3)(m 4 5)(6 7 8))')
    out = a_star_solve(s1, DifCalcIncorrectEP(s2))
    assert len(out) == 3
    assert out[0] == s1
    assert out[1] == s_mid
    assert out[2] == s2


def test_a_star_3x2():
    s1 = prepare_state('((m 1 2)(3 4 5))')
    s2 = prepare_state('((3 4 5)(m 1 2))')
    out = a_star_solve(s1, DifCalcIncorrectEP(s2))
    print_path(out)
    assert len(out) == 22
    assert out[len(out) - 1] == s2


def test_a_star_4x2():
    s1 = prepare_state('((m 1 2 3)(4 5 6 7))')
    s2 = prepare_state('((3 2 5 4)(7 6 1 m))')
    out = a_star_solve(s1, DifCalcDistanceFromCorrectEP(s2))
    print_path(out)
    assert len(out) == 37
    assert out[len(out) - 1] == s2
