import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://store.steampowered.com/search/?supportedlang=english&specials=1&ndl=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = 'search_results')


overall_tag = results.find_all('div',class_='responsive_search_name_combined')

title = results.find_all("span", class_="title")
prices = results.find_all("div", class_="col search_price discounted responsive_secondrow")
user_rating = results.find_all("div",class_='col search_reviewscore responsive_secondrow')

discount_steam = results.find_all('div',class_='col search_discount responsive_secondrow')

posts_dict = {"Title": [], "Original Price": [],
              "Discounted Price": [], "Discount Percentage": [],
              "User Rating": []
              }

game_title = []
discount_price = []
orig_price = []
discount = []
rating_list = []

counter = 0


for price in prices:
    orig_p = price.text.split(" ")[1].replace("₹","")
    orig_p = orig_p.replace(",",'')
    orig_price.append(int(orig_p))

    discount_p = price.text.split(" ")[2].replace("₹", "")
    discount_p = discount_p.replace(",", '')
    discount_price.append(int(discount_p))

for i in range(len(orig_price)):
    discount.append(int(((orig_price[i]-discount_price[i])/orig_price[i])*100))

dataframe = pd.DataFrame(posts_dict)

dataframe.to_csv('steam_csv')

for tit in title:
    game_title.append(tit.text)

new_text = []
for tit in user_rating:
    new_text.append(tit.span)



for i in new_text:
    if("Very Positive" in str(i)):
        rating_list.append("Very Positive")
    elif("Mostly Positive" in str(i)):
        rating_list.append("Mostly Positive")
    elif ("Overwhelmingly Positive" in str(i)):
        rating_list.append("Overwhelmingly Positive")
    elif ("Mixed" in str(i)):
        rating_list.append("Mixed")
    elif ("Mostly Negative" in str(i)):
        rating_list.append("Mostly Mostly Negative")


#print(game_title)
index = 0
for i in range(len(game_title)):
    i += 1
    if(game_title[i] == 'Grand Theft Auto V'):
        index = i
        break

game_title.remove(game_title[index])
rating_list.remove(rating_list[index])


dataframe = pd.DataFrame({'Title':game_title,'Orignal Price':orig_price,'Discounted Price':discount_price,'Dicount':discount,'User Rating':rating_list})
dataframe = dataframe.sort_values('Dicount')
dataframe.to_csv('Images/steam_data.csv')
