"""
Author: David De La Cruz
Date: 4/26/2025
Filename: dev_branch_code
Description: This file was made in the newly created "development" branch, and I'm going to try to both push this, and merge it with the main branch.
"""

def print_list(arr: list):
    if type(arr) is not list:
        print("Invalid input!")
        return
    for x in arr:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    test_list = [1, 2, "yes", "no", True, False]
    print_list(test_list)

    test_invalid = "okay"
    print_list(test_invalid)