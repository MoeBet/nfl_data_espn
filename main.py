from bs4 import BeautifulSoup as bs
import requests


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

matches = {nfl_teams[n]: scores[n] for n in range(len(nfl_teams))}

away_teams = nfl_teams[::2]
away_teams_scores = scores[::2]
home_teams = nfl_teams[1::2]
home_teams_scores = scores[1::2]

home_teams_dict = {home_teams[n]: home_teams_scores[n] for n in range(len(home_teams))}
away_teams_dict = {away_teams[n]: away_teams_scores[n] for n in range(len(away_teams))}

i = 0

for _ in range(len(away_teams)):
    print(f"{away_teams[i]} at {home_teams[i]} - {away_teams_scores[i]} : {home_teams_scores[i]}")
    i += 1

