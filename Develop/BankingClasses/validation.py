""" This class validates the email addresses and password when logging on."""

class Validation:
    """ This class contains methods for validating email addresses and passwords."""
    @staticmethod
    # TODO: Implement the validate_email method using the staticmethod decorator.
    # TODO: The method should take an email parameter and return True if the email contains an "@" symbol.
    def validate_email(email):
        if "@" in email:
            return True
        else:
            return False
    @staticmethod
    # TODO: Implement the validate_password method using the staticmethod decorator.
    def validate_password(password):
        """
        This method validates a password based on the following criteria:
        - The password must be at least 8 characters long.
        - The password must contain at least one uppercase letter,
          one lowercase letter, one digit, and one special character (!@#$%^&*).

        Args:
          password (str): The password to be validated.

        Returns:
          bool: True if the password is valid, False otherwise.
        """
        # TODO: Implement the password length validation logic.
        # TODO: Check if the password is at least 8 characters long if not return False.
        if len(password) < 8:
            return False

        # TODO: Set the initial values for uppercase, lowercase, digit, and special characters to False.
        # TODO: Has at least one uppercase letter, i.e., has_upper = False
        # TODO: Has at least one lowercase letter
        # TODO: Has at least one digit
        # TODO: Has at least one special character
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_characters = "!@#$%^&*"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True
        # TODO: Use if/elif/else statements to check the character type.
        # TODO: Set the corresponding variable to True if it fits the criteria.

        # Return the boolean value based on the conditions.
        return has_upper and has_lower and has_digit and has_special
