from src.functions import is_solved


def test_not_finished():
    board = [[0, 0, 1], [0, 1, 2], [2, 1, 0]]
    assert is_solved(board) == -1


def test_winning_row():
    board = [[2, 1, 1], [0, 1, 1], [2, 2, 2]]
    assert is_solved(board) == 2


def test_winning_draw():
    board = [[2, 1, 2], [2, 1, 1], [1, 2, 1]]
    assert is_solved(board) == 0
