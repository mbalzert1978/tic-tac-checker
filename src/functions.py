"""Functions to solve tic tac toe game."""


def is_solved(board: list[list[int]]) -> int:
    """
    Check if a tic tac toe board is solved.

    Args:
    ----
    board: a 2d list of integers 3 x 3 grid.

    Returns:
    -------
    ```
    1 when winner is 1
    2 when winner is 2
    0 on a draw
    -1 when unsolved.
    ```
    """
    return solve_game_from(
        set(fetch_diagonals(board) + fetch_row(board) + fetch_col(board)),
    )


def fetch_row(board) -> list[int]:
    """Fetch the result of rows of a tic tac toe board."""
    return [board[i][0] * board[i][1] * board[i][2] for i in range(3)]


def fetch_col(board) -> list[int]:
    """Fetch the result of columns of a tic tac toe board."""
    return [board[0][i] * board[1][i] * board[2][i] for i in range(3)]


def fetch_diagonals(board) -> list[int]:
    """Fetch the result of diagonals of a tic tac toe board."""
    return [
        board[0][0] * board[1][1] * board[2][2],
        board[0][2] * board[1][1] * board[2][0],
    ]


def solve_game_from(result: set[int]) -> int:  # sourcery skip: assign-if-exp
    """
    Solve a tic tac toe game from a result.

    Args:
    ----
    result: result set

    Returns:
    -------
    ```
    1 when winner is 1
    2 when winner is 2
    0 on a draw
    -1 when unsolved.
    ```
    """
    if 1 in result:
        return 1
    if 8 in result:  # noqa: PLR2004
        return 2
    if 0 in result:
        return -1
    return 0
