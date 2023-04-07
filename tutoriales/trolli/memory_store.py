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
    
    def get_board(self, id: int) -> 'Board':
        """
        Get a board from the data store.

        :param id: The id of the board to get.
        :return: The board.
        """
        return self.boards[id]

    def update_board(self, board: 'Board', update: dict):
        """
        Update a board in the data store.

        :param model: The board model to update.
        :param update: The update to apply to the board.
        """
        for k in update:
            setattr(board, k, update[k])
    
    def get_boards(self) -> list['Board']:
        """
        Get all boards from the data store.

        :return: The boards.
        """
        return [self.boards[id] for id in self.boards]

    def remove_board(self, board: 'Board') -> None:
        """
        Remove a board from the data store.

        :param board: The board model to remove.
        """
        del self.boards[board.board_id]
        self.board_lists[board.id] = []
    
    def add_list(self, board: int, list: 'BoardList'):
        """
        Add a new list to the data store.

        :param board: The board to add the list to.
        :param list: The list model to add.
        """
        if board in self.board_lists:
            self.board_lists[board].append(list)
        else:
            self.board_lists[board] = [list]
    
    def get_lists_by_board(self, board) -> list["BoardList"]:
        """
        Get all lists for a board from the data store.

        :param board: The board to get the lists for.

        :return: The lists.
        """
        return self.board_lists.get(board, [])
    
    def remove_list(self, board: int, id: int):
        """
        Remove a list from the data store.

        :param board: The board to remove the list from.
        :param id: The id of the list to remove.
        """
        self.board_lists[board] = [l for l in self.board_lists[board] if l.id == id]
    
    
