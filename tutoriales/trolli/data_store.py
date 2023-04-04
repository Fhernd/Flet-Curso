from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board
    from board_list import BoardList
    from user import User
    from item import Item


class DataStore:

    def add_board(self, model) -> None:
        """
        Add a new board to the data store.

        :param model: The board model to add.
        """
        raise NotImplementedError

    def get_board(self, id: int) -> "Board":
        """
        Get a board from the data store.

        :param id: The id of the board to get.
        :return: The board.
        """
        raise NotImplementedError
    