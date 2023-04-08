class User:
    """
    A user model.
    """
    def __init__(self, name, password):
        """
        Create a new user.

        :param name: The user's name.
        :param password: The user's password.
        """
        self.name = name
        self.password = password
