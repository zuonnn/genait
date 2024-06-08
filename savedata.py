import requests
from bs4 import BeautifulSoup
import csv

# 1. Get website content
url = "https://thethao247.vn/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 2. Find relevant elements with higher specificity
player_elements = soup.find_all("span", class_="player-name")  # Assuming a class for player names
team_elements = soup.find_all("span", class_="team-name")    # Assuming a class for team names
score_elements = soup.find_all("span", class_="score")        # Assuming a class for scores

# 3. Extract information with validation
player_names = []
team_names = []
scores = []

if player_elements:  # Check if elements are found before accessing text
    for player in player_elements:
        player_names.append(player.text.strip())

if team_elements:
    for team in team_elements:
        team_names.append(team.text.strip())

if score_elements:
    for score in score_elements:
        scores.append(score.text.strip())

# 4. Write data to CSV file
with open("sports_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Player Name", "Team Name", "Score"])
    for player, team, score in zip(player_names, team_names, scores):
        writer.writerow([player, team, score])

print("CSV file created successfully!")
