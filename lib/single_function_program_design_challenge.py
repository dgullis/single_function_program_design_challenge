import os.path


def check_for_tasks(file_path):
    
    #check if given file exists
    if os.path.isfile(file_path):

        #if file exists open file in read only as 'contents'
        with open(file_path, 'r') as contents:
            # extract contents of file line by line
            lines = contents.readlines()
        
        # iterate over each line and if the line starts with #TODO add this to a list
        raw_tasks = [line for line in lines if line.startswith("#TODO")]
        # iterate over found tasks and strip them of line breaks and #TODO.
        # add these stripped tasks into a new list
        tasks_stripped = [task.strip("\n").strip("#TODO ") for task in raw_tasks]

        # check to see if any tasks have been found
        if not tasks_stripped:

            # treturn appropriate string if none found
            return "No tasks found."
        else:
            # if takss found return them as a string
            return ", ".join(tasks_stripped)
    else:
        # if file was not found return an exception statement to explain this
        raise FileNotFoundError("File not found!")
    