import requests
from bs4 import BeautifulSoup
import re

def collect_move_data():
    data = requests.get("https://bulbapedia.bulbagarden.net/wiki/List_of_moves_in_other_languages").content
    
    result = {}
    
    soup = BeautifulSoup(data, "html.parser")
    print(soup)
    
    table = soup.find("table", class_ = 'roundy sortable')
    print(table)
    table_body = table.find("tbody")
    
    
    table_rows = table_body.find_all("tr")
    for row in table_rows:
        columns = row.find_all("td")
        
        if columns != []:
            
           ENG = columns[1].text.strip()
           JPN=  columns[2].text.strip()
           #Note to self if you want both ways just add the reverse of this dictionary
           result[JPN] = ENG
           result[ENG] = JPN
    
    return result

def collect_mon_data():
    data = requests.get('https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names').content
    
    mon_dictionary = {}
    
    soup = BeautifulSoup(data,"html.parser")
    tables = soup.find_all('table' , class_ = 'roundy roundtable') 
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            data = row.find_all('td')
            if data != []:
                mon_dictionary[data[3].text.strip()] = data[2].text.strip()
    return mon_dictionary

def collect_ability_data():
    ability_data = {}
    data = requests.get('https://bulbapedia.bulbagarden.net/wiki/List_of_Abilities_in_other_languages').content
    
    soup = BeautifulSoup(data,'html.parser')
    print(soup)
    
    table = soup.find('table', class_ = 'roundy sortable')
    
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns != []:
            ability_data[columns[2].text.strip()] = columns[1].text.strip()
            ability_data[columns[1].text.strip()] = columns[2].text.strip()

    return ability_data

def collect_item_data(text):
    text = text.lower()
    text = re.match("^[a-z\-0-9_ ]*$", text)
    text = text.string
    text = text.replace(' ','-')
    
    try:
        data = requests.get(f"https://pokemondb.net/item/{text}").content
    
        soup = BeautifulSoup(data, 'html.parser')
        
        header = soup.find("h2", string= "Other languages")
        table = header.find_next_sibling()
        
        rows = table.find_all("tr")
        
        if len(rows != 0 ):
        
            return rows[1].find("td").text.strip()
        
    
        
        
        return "None"
    except:
        return "なし"
        
def write(data , var_name):
    with open(f'{var_name}.py', 'a', encoding= 'utf -8') as f:
        f.write(f'{var_name} = {data}\n')



if __name__ == "__main__":
    # move_data = collect_move_data()
    # write(move_data, 'moves')
    mon_data = collect_mon_data()
    write(mon_data, 'mons')
    # ability_data = collect_ability_data()
    # write(ability_data, 'abilities')
    
    print(collect_item_data("None"))
        