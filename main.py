import requests
from bs4 import BeautifulSoup as bs
import check_pg
import photo

page_url = "https://rasp.barsu.by//stud.php"

file = open("rasp_barsy.html", 'w')

html = requests.get(page_url).text

soup = bs(html, 'html.parser')

# faculty = soup.find('select', {'id':'faculty'})
# speciality = soup.find('select', {'id':'speciality'})
# group = soup.find('select', {'id':'groups'})
# weekbegindate = soup.find('select', {'id':'weekbegindate'})

# button = soup.find('input', {'class':'btn btn-primary'})

payload = {
    'faculty':'Инженерный факультет',
    'speciality':'Информационные системы и технологии',
    'groups':'ИСТ31',
    'weekbegindate':'2023-04-03',
    'go':'onsubmit'
}

response = requests.post(page_url, data=payload)

html2 = response.text

soup2 = bs(html2, 'html.parser')

info  = soup2.find_all('td')

file.write(str(info))

rasp = []

for i in info:
    rasp.append(i.text)

rasp = rasp[:-2]

rasp = rasp[:len(rasp)//2]

good_rasp = [[] for i in range(len(rasp)//18)]

amount_les = []

x = 0
k = -1

while x < len(rasp):
    if x % 18 == 0:
        k += 1
        good_rasp[k].append(rasp[x])
        x += 1
    else:
        good_rasp[k].append(rasp[x])
        x += 1

am = 0
for i in good_rasp:
    am = 0
    # print(f" \n{i[0]}  {i[1]}\n") 

    for j in range(2, len(i), 2):
        if i[j + 1] != ' ':
            am += 1
            # print(f"{i[j]} -> {check_pg.divide_pg(i[j + 1])}")
    amount_les.append(am)

photo.draw_rasp(good_rasp) 

# print(amount_les, good_rasp)