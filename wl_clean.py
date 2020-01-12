from bs4 import BeautifulSoup
soup = BeautifulSoup(open("output1.html"), features="html.parser")

def process_each(div):
    data = {}
    place_image = div.find_all('img')[0].get('src')
    data['image'] = place_image

    temp = div.find_all('div', {'class':'m-srp-card__photo flex__item'})
    temp = temp[0].find_all('div', {'class':'m-srp-card__post-date pull-right'})
    temp = temp[0].find_all('span', {'itemprop':'dateCreated'})
    date_posted = temp[0].contents[0]
    data['date_posted'] = date_posted

    return data

alldivs = soup.findAll("div", {"class":"flex relative clearfix m-srp-card__container"})
for div in alldivs:
    place_info = process_each(div)
    print(place_info)
    print('\n\n')
