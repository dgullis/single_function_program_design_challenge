from lib.single_function_program_design_challenge import *

import pytest

"""
Given a file containing no tasks
Returns string "no tasks to do."
"""

def test_no_tasks_in_file():
    file = "/Users/dangullis/Desktop/Projects/single_function_program_design_challenge/file_one.py"
    assert check_for_tasks(file) == "No tasks found."

"""
Given a file containing one task
Returns task as string
"""

def test_one_task_in_file():
    file = "/Users/dangullis/Desktop/Projects/single_function_program_design_challenge/file_two.txt"
    assert check_for_tasks(file) == "buy groceries for dinner"

"""
Given a file containing two tasks
Returns both tasks as a string
"""

def test_two_tasks_in_file():
    file = "/Users/dangullis/Desktop/Projects/single_function_program_design_challenge/file_three.py"
    assert check_for_tasks(file) == "buy groceries for dinner, make dinner"

"""
If given file is not found
Raise an Exception
"""

def test_file_not_founf():
    file = "/Users/dangullis/Desktop/Projects/single_function_program_design_challenge/file_threee.py"
    with pytest.raises(FileNotFoundError) as e:
        check_for_tasks(file)
        assert str(e.value) == "File not found!"