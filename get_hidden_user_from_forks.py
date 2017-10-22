import sys

import requests
from bs4 import BeautifulSoup
from github import Github

g = Github('login_or_token')

user_name, repo_name = sys.argv[1], sys.argv[2]

r = requests.get('https://github.com/{}/{}/network/members'.format(user_name, repo_name))
soup = BeautifulSoup(r.text, "html.parser")
forks = soup.findAll("div", {"class": "repo"})
web_login = []
for fork in forks:
    user_link = fork.a.get('href')
    user_login = user_link.replace('/', '')
    web_login.append(user_login)

r = g.get_user(user_name).get_repo(repo_name)
forks = r.get_forks()
for fork in forks:
    if fork.owner.login not in web_login:
        print(fork.owner.html_url)
        print(fork.owner.url, '\n')
