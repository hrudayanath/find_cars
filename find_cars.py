#find_cars.py

import time
import urllib2
import itertools
import sys, re
from bs4 import BeautifulSoup as bs

'''
class search_data:
   dealer
   url
   terms 

  if (dealer.dealer == "vantrow"):
    print "processing vantrow data"
  elif (dealer.dealer == "sparks"):
    print "processing sparksnissan"
'''

url = 'http://www.sparksnissan.com/inventory/view/Used/Price/5001-10000/Transmissions/Automatic/SortBy0/'

titles = []
search_terms = ['ctl00_ContentSection_ctl03_searchresults', 'vehicletitle']

#search_terms = { 'vantrow': ['vehicledetails', 'pricing']}

def parse_data(soup):
   for car,price  in itertools.izip(soup.find_all(class_="left vehicleinformation"),soup.find_all(class_="single clearfix")):
      car_name = ''.join([text for text in car.h2.get_text()])
      car_trans = car.ul.find(class_ = "vehicletrans").get_text()
      car_odometer = car.ul.find(class_ = "vehicleodometer").get_text()
      car_mpg = car.ul.find(class_ = "mpg").get_text()
      car_price = price.span.get_text()
      print car_name, car_trans, car_odometer, car_mpg, car_price 
    
def get_data(url):
  return urllib2.urlopen(url)

def collect_data():
  dat = bs(get_data(url))
  return parse_data( dat)
    
cars_df = collect_data()
print cars_df

'''
new_cars = compare_fornewcars()
send_alert(new_cars)
'''
