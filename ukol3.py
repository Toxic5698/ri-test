import re
import requests
from bs4 import BeautifulSoup

print('Úkol č. 3')
team = input('Zadejte název týmu, třeba Brno: ')


def matches_parsing():
    print("Získávám data...")
    with requests.Session() as se:
        data = BeautifulSoup(
            se.get('https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089').text,
            "html.parser")
    matches = data.find_all(string=team)
    if len(matches) < 1:
        print('Chybně zadaný název týmu.')
        exit()
    for match in matches:
        try:
            match_info = match.find_parent("div", {"class": "list-score status-fin list-score-small date-show"})
            looser = match_info.find_all(class_=re.compile("team-looser"))
            if looser[0].text != team:
                match_date = match_info.find("div", {"class": "datetime-container"}).text.split("•")[0].strip()
                print(f'Dne {match_date} jsme porazili {looser[0].text}')
        except AttributeError:
            exit()


matches_parsing()
