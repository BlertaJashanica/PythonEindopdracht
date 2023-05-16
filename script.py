from github import Github

g = Github("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")

# Specify the repository details
repo_owner = "BlertaJashanica"
repo_name = "PythonEindopdracht"
file_path = "signals.txt"

# Get the repository
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Get the file contents
file = repo.get_contents(file_path)

# Get the last commit that modified the file
last_commit = repo.get_commits(path=file_path)[0]

# Extract the commit details
commit_sha = last_commit.sha
commit_message = last_commit.commit.message
commit_author = last_commit.commit.author.name
