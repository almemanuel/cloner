from github import Github
import os
import git

g = Github('YOUR_GITHUB_PERSONAL_TOKEN')

user = g.get_user('YOUR_USERNAME')

clone_dir = 'RELATIVE/PATH/TO/YOUR/FOLDER'

if not os.path.exists(clone_dir):
    os.makedirs(clone_dir)

for repo in user.get_repos():
    repo_url = repo.clone_url
    print(f'Cloning {repo.name}...')
    git.Repo.clone_from(repo_url, os.path.join(clone_dir, repo.name))
