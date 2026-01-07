import git
import os
import sys
import requests

def post_comment(comment):
  GITHUB_TOKEN = sys.argv[2]
  COMMENT_URL = sys.argv[3]

  headers = {
      "Authorization": f"token {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
  }

  data = {
      "body": comment
  }

  try:
    response = requests.post(COMMENT_URL, headers=headers, json=data)
  except Exception as e:
    print(e)
  
comments = sys.argv[1].splitlines()
for comment_line in comments:
  if 'source' in comment_line:
    source = comment_line.split(':')
    source[1] = source[1].strip()
    try:
      repo = git.Repo.clone_from(f'https://calebu:{sys.argv[2]}@github.com/calebu/' + source[1], source[1])
      print(f"Repository successfully cloned to {os.path.abspath(source[1])}")
    except Exception as clone_exc:
      post_comment(f"Unable to clone source repo: {clone_exc}")
  elif 'target' in comment_line:
    target = comment_line.split(':')
    target[1] = target[1].strip()
    try:
      repo = git.Repo.clone_from(f'https://calebu:{sys.argv[2]}@github.com/calebu/' + target[1], target[1])
      print(f"Repository successfully cloned to {os.path.abspath(target[1])}")
    except Exception as clone_exc:
      post_comment(f"Unable to clone source repo: {clone_exc}")