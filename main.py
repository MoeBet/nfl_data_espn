from bs4 import BeautifulSoup as bs
import requests
import time

week = "17"
year = "2020"
response = requests.get(f'https://www.cbssports.com/nfl/scoreboard/{year}/regular/{week}/')
soup = bs(response.content, "html.parser")

game_results = soup.find_all("td", attrs={"class": "total-score"})
team_names = soup.find_all("a", attrs={"class": "team helper-team-name"})

nfl_teams = []
scores = []

for name in team_names:
    holder = name.getText()
    nfl_teams.append(holder)

for result in game_results:
    holder = result.getText()
    scores.append(holder)



score_holder = 0
score_holder_2 = 1
team_holder = 0
team_holder_2 = 1

for _ in nfl_teams:
    print(f"{nfl_teams[score_holder]} vs. {nfl_teams[score_holder_2]} {scores[score_holder]}:{scores[score_holder_2]}")
    score_holder += 2
    score_holder_2 += 2
    team_holder += 2
    team_holder_2 += 2

