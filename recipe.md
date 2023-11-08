# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
so that i can keep track of my tasks
I want to check if a text includes the string #TODO

## 2. Design the Function Signature

name: check_for_tasks
parameters: file
return: lines of text starting with #TODO
side effects: none, prints nothing
_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_for_tasks(file):
    """looks for tasks via lines starting with #TODO

    Parameters: (list all parameters and their types)
        file: a file e.g. .txt / .py with lines of text / code some of which may start with #TODO

    Returns: (state the return value and its type)
        a list of strings where the sting has started with #TODO

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a file containing no tasks
Returns string "no tasks to do."
"""

def test_no_tasks_in_file():
    file = /Users/dangullis/Desktop/Projects/single_function_program_design_challenge/test_file_one.py
    assert check_for_tasks(file) == "no tasks to do."

"""
Given a file containing one task
Returns string of task
"""

def test_one_task_in_file():
    file = "../Desktop/Projects/single_function_program_design_challenge/file_two.txt"
    assert_check_for_tasks(file) == "#TODO buy groceries for dinner"

"""
Given a file containing two tasks
returns both tasks as a string
"""

def test_two_tasks_in_file():
    file = "/Users/dangullis/Desktop/Projects/single_function_program_design_challenge/file_three.py"
    assert check_for_tasks(file) == "#TODO buy groceries for dinner, #TODO make dinner"


# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
