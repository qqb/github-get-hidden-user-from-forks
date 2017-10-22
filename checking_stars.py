import math
import sys

import requests
from bs4 import BeautifulSoup
from github import Github

g = Github('login_or_token')

user_name, repo_name = sys.argv[1], sys.argv[2]

main_page = requests.get('https://github.com/{}/{}'.format(user_name, repo_name))
soup = BeautifulSoup(main_page.text, "html.parser")
stars = soup.findAll("a", {"class": "social-count"})
social_count = stars[1].text.lstrip()

pages = math.ceil(int(social_count) / 51)
print(pages)

web_login = []
for p in range(1, pages + 1):
    page_stars = requests.get('https://github.com/{}/{}/stargazers?page={}'.format(user_name, repo_name, p))
    soup = BeautifulSoup(page_stars.text, "html.parser")
    stars = soup.findAll("h3", {"class": "follow-list-name"})
    for s in stars:
        user_link = s.a.get('href')
        user_login = user_link.replace('/', '')
        web_login.append(user_login)

print(len(web_login))

r = g.get_user(user_name).get_repo(repo_name)
stars = r.get_stargazers()
for star in stars:
    if star.login not in web_login:
        print(star.html_url)
        print(star.url, '\n')
