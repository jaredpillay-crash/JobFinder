#from bs4 import BeautifulSoup as bs 
#import requests as rq
#import time
#
#
#html_text = rq.get('https://www.property24.com/for-sale/durban/kwazulu-natal/169').text
#
#soup = bs(html_text, 'lxml')
#homes = soup.find_all('div', class_= "js_listingResultsContainer" )
#content = soup.find_all('span', class_="p24_content")
#vinfo = soup.find_all('span', class_="p24_icons")
#beds = vinfo.find('span', title="Bedrooms")
#
#for home in homes:
#    link = home.a['href']
#    for con in content:
#        ti = con.find('span', itemprop='name').text
#        loc = con.find('span', class_='p24_location').text
#        des = con.find('span', class_='p24_excerpt').text
#        price = con.find('span', class_='p24_price').text
#        
#    
#    
#        
#
#
   #price = home.span.text
   #des = home.find('p', class_="property-card-info__description").text
   #beds = home.find('span', itemprop="numberOfRooms").text
   #baths = home.find('span', itemprop="amenityFeature").text
   #msq = home.find('div', class_="property-card-info__icons")
   #av = msq.find('span')
    
      
  

    