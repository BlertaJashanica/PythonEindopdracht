import yaml
from github import Github
import modules
import time


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

# Check the time since the last commit
commit_time = last_commit.commit.committer.date.timestamp()
current_time = time.time()
time_diff = current_time - commit_time

# Get the file content from the last commit if it's within the last 60 seconds
if time_diff <= 60:
    file_content = repo.get_contents(file_path, ref=last_commit.sha).content.decode("utf-8")
else:
    file_content = ""


parent_vars = config_data.get(file_content, {})
module = parent_vars.get('module')
moduleClass = parent_vars.get('class')
moduleFunction = parent_vars.get('function')

classe = module.moduleClass
object = classe()
output = object.moduleFunction()




