import yaml
from github import Github
import modules
import time
from datetime import datetime, timezone
import importlib
from git import Repo
import requests


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

commit_time = last_commit.commit.committer.date.replace(tzinfo=timezone.utc)  

current_time = datetime.now(timezone.utc)  

time_diff = (current_time - commit_time).total_seconds()  

if time_diff <= 120:
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
    function()

    
    file_name = 'output.txt'
    moduleFunction = 'log'
    function = getattr(instance, moduleFunction)
    output = function()
    
    with open(file_name, 'w') as file:
        file.write(output)
    

    repository_owner = "BlertaJashanica"
    repository_name = "PythonEindopdracht"
    file_path = "output.txt"
    file_content = output
    github_token = "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"
    commit_message = 'updated output'

    api_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_path}"
    headers = {
        "Authorization": f"Token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    import base64
    file_content_encoded = base64.b64encode(file_content.encode()).decode()

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        current_file = response.json()
        sha = current_file["sha"]
    else:
        sha = None

    payload = {
        "message": commit_message,
        "content": file_content_encoded,
        "sha": sha
    }

    response = requests.put(api_url, json=payload, headers=headers)
    if response.status_code == 201:
        print("File pushed successfully!")
    else:
        print("An error occurred while pushing the file:", response.text)


else:
    print("Module not found in parent_vars dictionary.")
