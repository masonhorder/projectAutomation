# import subprocess
# import requests
# import sys
#
# # Notice that you username and token are required here
# r = requests.post(
#   "https://api.github.com/users/masonhorder/repos?access_token=56680a2ca84a69f9d55d3783b864ce7b92ae50b4",
#   data={
#   "name": "hi",
#   "description": "This is your first repository",
#   "homepage": "https://github.com",
#   "private": "true",
#   "has_issues": "true",
#   "has_projects": "true",
#   "has_wiki": "true"
# })
#
# if r.status_code != 200:
#   print("repo created")
#   sys.exit()

import requests
import json

####
# inputs
####
username = 'masonhorder'

# from https://github.com/user/settings/tokens
token = '56680a2ca84a69f9d55d3783b864ce7b92ae50b4'

repos_url = 'https://api.github.com/user/repos'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
repos = json.loads(gh_session.get(repos_url).text)

# print the repo names
for repo in repos:
    print repo['name']

# make more requests using "gh_session" to create repos, list issues, etc.
