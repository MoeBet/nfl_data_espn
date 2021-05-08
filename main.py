from bs4 import BeautifulSoup
import requests
import time

week = "17"
year = "2020"
response = requests.get(f'https://www.espn.com/nfl/scoreboard/_/year/{year}/seasontype/2/week/{week}')
data = response.content
soup = BeautifulSoup(data, "html.parser")

soup.find()