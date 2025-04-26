"""
Author: David De La Cruz
Date: 4/26/2025
Filename: practice_py
Description: This is a practice file I made through VS Code, and am ready to commit it
"""

class Thing:
    def __init__(self, message = None):
        if not message:
            self.message = "Here I am!"
        else:
            self.message = message

    def print_self_message(self):
        print(self.message)


if __name__ == "__main__":
    obj = Thing("This is a whole new creation...")
    obj.print_self_message()