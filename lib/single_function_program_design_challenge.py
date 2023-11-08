import os.path


def check_for_tasks(file):

    if os.path.isfile(file):
        with open(file, 'r') as contents:
            lines = contents.readlines()
        
        raw_tasks = [line for line in lines if line.startswith("#TODO")]
        tasks_stripped = [task.strip("\n").strip("#TODO ") for task in raw_tasks]

        if len(tasks_stripped) == 0:
            return "No tasks found."
        else:
            return ", ".join(tasks_stripped)
    else:
        raise Exception("file not found!")
    