from bs4 import BeautifulSoup
import requests

username = input("Enter which users repository to list\n")
user_url = "https://github.com/" + username + "?tab=repositories"
result = requests.get(user_url)
src = result.content
soup = BeautifulSoup(src, 'lxml')

while True:
    for repository in soup.findAll('h3', class_='wb-break-all'):
        print(repository.a.text.strip())
    next_page = soup.find("a", class_='next_page')
    if next_page:
        url = "https://github.com" + str(next_page.get('href'))
        soup = BeautifulSoup(requests.get(url).content, "lxml")
    else:
        break
