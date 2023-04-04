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
    