import yaml
from github import Github
import modules
import time
from datetime import datetime, timezone
import importlib
from git import Repo

# Lees het YAML-bestand
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

g = Github("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")

repo_owner = "BlertaJashanica"
repo_name = "PythonEindopdracht"
file_path = "signals.txt"

repo = g.get_repo(f"{repo_owner}/{repo_name}")

file = repo.get_contents(file_path)

last_commit = repo.get_commits()[0]

commit_time = last_commit.commit.committer.date.replace(tzinfo=timezone.utc)  # Make commit time offset-aware

current_time = datetime.now(timezone.utc)  # Get current time in datetime object with timezone info

time_diff = (current_time - commit_time).total_seconds()  # Calculate time difference in seconds

# Get the file content from the last commit if it's within the last 60 seconds
if time_diff <= 70000:
    file_content = repo.get_contents(file_path, ref=last_commit.sha).decoded_content.decode("utf-8").split()
else:
    file_content = ""

parent_vars = config_data.get(file_content[-1], {})
module = parent_vars.get('module')
moduleClass = parent_vars.get('class')
moduleFunction = parent_vars.get('function')

if module is not None:
    module = importlib.import_module(module)
    class_object = getattr(module, moduleClass)
    instance = class_object()
    function = getattr(instance, moduleFunction)
    data = function()

    
    file_name = 'output.txt'
    moduleFunction = 'log'
    function = getattr(instance, moduleFunction)
    output = function(data)
    
    with open(file_name, 'w') as file:
        file.write(output)
    
    
    from git import Repo

    # Provide the path to the repository
    repo_path = 'BlertaJashanica/PythonEindopdracht'

    # Open the repository
    repo = Repo(repo_path)

    # Specify the file path to be committed
    file_path = 'BlertaJashanica/PythonEindopdracht/output.txt'

    # Specify the commit message
    commit_message = 'Added file.txt'

    # Add the file to the index
    repo.index.add([file_path])

    # Commit the changes
    repo.index.commit(commit_message)


else:
    print("Module not found in parent_vars dictionary.")
