#find_cars.py

import time
import urllib2
import itertools
import sys, re
from bs4 import BeautifulSoup as bs

class search_data:
   def __init__(self, dealer,url):
     
      self.dealer = dealer
      self.url = url

d1 = search_data("sparks", 'http://www.sparksnissan.com/inventory/view/Used/Price/5001-10000/Transmissions/Automatic/SortBy0/')
d2 = search_data("vantrow", 'http://vantrowtoyota.com/Monroe-Louisiana/For-Sale/Used/?MaxMSRP=10000&MinYear=2007')


def parse_data(dealer, soup):
  if (dealer.dealer == "vantrow"):
    print "processing vantrow data"
    for name, car_det, price in itertools.izip(soup.find_all(class_ = "vehicle-link"),soup.find_all(class_ = "vehicle-detail-list"), soup.find_all(class_ = "vehicle-price-default-price")):
      car_name = name.string
      car_trans = car_det.find(class_ ="trans").next_sibling.next_sibling.string
      car_odometer =''
      car_mpg = car_det.find(class_ ="mpg").next_sibling.next_sibling.string
      car_price = price.get_text()
      print car_name, car_trans, car_odometer, car_mpg, car_price 

  elif (dealer.dealer == "sparks"):
    print "processing sparksnissan"
    for car,price  in itertools.izip(soup.find_all(class_="left vehicleinformation"),soup.find_all(class_="single clearfix")):
      car_name = ''.join([text for text in car.h2.get_text()])
      car_trans = car.ul.find(class_ = "vehicletrans").get_text()
      car_odometer = car.ul.find(class_ = "vehicleodometer").get_text()
      car_mpg = car.ul.find(class_ = "mpg").get_text()
      car_price = price.span.get_text()
      print car_name, car_trans, car_odometer, car_mpg, car_price 
    
def get_data(url):
  return urllib2.urlopen(url)

def collect_data(d):
  dat = bs(get_data(d.url))
  return parse_data( d,dat)
    
collect_data(d1)
collect_data(d2)
'''
new_cars = compare_fornewcars()
send_alert(new_cars)
'''
