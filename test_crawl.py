import csv
from bs4 import BeautifulSoup

# Load the HTML content
html_content = """
<html>
  <body>
    <div class="info">
      <h2>Tên: John Doe</h2>
      <p>Địa chỉ: 123 Main St, Anytown, USA</p>
      <p>Số điện thoại: 555-555-5555</p>
      <p>Email: <a href="mailto:johndoe@example.com">johndoe@example.com</a></p>
    </div>
    <div class="info">
      <h2>Tên: Jane Doe</h2>
      <p>Địa chỉ: 456 Elm St, Othertown, USA</p>
      <p>Số điện thoại: 555-555-1234</p>
      <p>Email: <a href="mailto:janedoe@example.com">janedoe@example.com</a></p>
    </div>
  </body>
</html>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class "info"
info_divs = soup.find_all('div', {'class': 'info'})

# Create a list to store the extracted data
data = []

# Loop through each div element
for div in info_divs:
    # Extract the data from each div element
    ten = div.find('h2').text.split(': ')[1]
    dia_chi = div.find_all('p')[0].text.split(': ')[1]
    so_dien_thoai = div.find_all('p')[1].text.split(': ')[1]
    email = div.find('a')['href'].split('mailto:')[1]
    
    # Append the extracted data to the list
    data.append([ten, dia_chi, so_dien_thoai, email])

# Write the data to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Address', 'Phone NUmber', 'Email'])  # header row
    writer.writerows(data)