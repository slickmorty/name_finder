from bs4 import BeautifulSoup as bs

with open("list.html", "r") as f:
    content = f.read()
    soup = bs(content, 'lxml')
    names = soup.find_all(
        'span', class_='style-scope ytd-playlist-panel-video-renderer', id='video-title')

names_txt = open("names.txt", "w")


for index, name in enumerate(names, start=1):
    name = name.text.replace(" ", "")
    name = name.replace("\n", "")
    if(name != ""):
        print(f"{index}:{name}")
        names_txt.write(f"{index}:{name} \n")
