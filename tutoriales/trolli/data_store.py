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
    
    def get_boards(self) -> list["Board"]:
        """
        Get all boards from the data store.

        :return: The boards.
        """
        raise NotImplementedError
    
    def update_board(self, model, update):
        """
        Update a board in the data store.

        :param model: The board model to update.
        :param update: The update to apply to the board.
        """
        raise NotImplementedError
    
    def remove_board(self, board) -> None:
        """
        Remove a board from the data store.

        :param board: The board model to remove.
        """
        raise NotImplementedError
    
    def add_user(self, model) -> None:
        """
        Add a new user to the data store.

        :param model: The user model to add.
        """
        raise NotImplementedError

    def get_users(self) -> list["User"]:
        """
        Get all users from the data store.

        :return: The users.
        """
        raise NotImplementedError

    def get_user(self, id: int) -> "User":
        """
        Get a user from the data store.

        :param id: The id of the user to get.
        :return: The user.
        """
        raise NotImplementedError

    def remove_user(self, id) -> None:
        """
        Remove a user from the data store.

        :param id: The user model to remove.
        """
        raise NotImplementedError
    
    def add_list(self, board, model) -> None:
        """
        Add a new list to the data store.

        :param board: The board to add the list to.
        :param model: The list model to add.
        """
        raise NotImplementedError

    def get_lists(self) -> list["BoardList"]:
        """
        Get all lists from the data store.

        :return: The lists.
        """
        raise NotImplementedError

    def get_list(self, id: int) -> "BoardList":
        """
        Get a list from the data store.

        :param id: The id of the list to get.
        :return: The list.
        """
        raise NotImplementedError
    
    def get_lists_by_board(self, board) -> list["BoardList"]:
        """
        Get all lists for a board from the data store.

        :param board: The board to get the lists for.
        :return: The lists.
        """
        raise NotImplementedError

    def remove_list(self, board, id) -> None:
        """
        Remove a list from the data store.

        :param board: The board to remove the list from.
        :param id: The list model to remove.
        """
        raise NotImplementedError
    
    def add_item(self, board_list, model) -> None:
        """
        Add a new item to the data store.

        :param board_list: The list to add the item to.
        :param model: The item model to add.
        """
        raise NotImplementedError

    def get_items(self, board_list) -> list["Item"]:
        """
        Get all items from the data store.

        :param board_list: The list to get the items for.
        :return: The items.
        """
        raise NotImplementedError
    