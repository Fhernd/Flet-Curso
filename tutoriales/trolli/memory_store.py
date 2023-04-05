from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from board import Board
    from board_list import BoardList
    from user import User
    from item import Item

from data_store import DataStore


class InMemoryStore(DataStore):
    """
    A data store that stores data in memory.
    """

    def __init__(self):
        """
        Create a new in memory data store.
        """
        self.boards :dict[int, 'Board'] = {}
        self.users: dict[str, 'User'] = {}
        self.board_lists: dict[int, list['BoardList']] = {}
        self.items: dict[int, list['Item']] = {}
    
    def add_board(self, board: 'Board') -> None:
        """
        Add a new board to the data store.

        :param model: The board model to add.
        """
        self.boards[board.board_id] = board
    