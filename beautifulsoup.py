import requests
from bs4 import BeautifulSoup

# 1. Đọc dữ liệu HTML
url = "https://thethao247.vn/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


# 2: Xác định các phần tử quan trọng
player_elements = soup.find_all("span", string="Player Name:")
team_elements = soup.find_all("span", string="Team Name:")
score_elements = soup.find_all("span", string="Score:")

# 3: Trích xuất thông tin
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
