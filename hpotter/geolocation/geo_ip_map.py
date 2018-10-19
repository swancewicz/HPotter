#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import re
import json
import sqlite3
from mpl_toolkits.basemap import Basemap
from urllib.request import urlopen

# Folium imports
import numpy as np
import folium
import matplotlib.pyplot as plt


def globe(ip_list):

    # size of window
    plt.figure(figsize=(50,24))
    
    map = Basemap(projection='robin', lat_0=0, lon_0=0)
    #map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
    #map = Basemap(projection='ortho', resolution='l', lat_0=50, lon_0=0)


    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.30)
    map.drawcountries(linewidth=0.30)
    map.drawstates(linewidth=0.30)
    #map.fillcontinents(color='dimgray',lake_color='darkgray')
    #map.fillcontinents(color='coral',lake_color='aqua')

    map.bluemarble()
    # draw the edge of the map projection region (the projection limb)
    map.drawmapboundary(fill_color='darkgray')

    # draw lat/lon grid lines every 30 degrees.
    #map.drawmeridians(np.arange(0,360,30))
    #map.drawparallels(np.arange(-90,90,30))

    for ip in ip_list:
        ## plot geo location from ip
        lat,lon = get_ip(ip)
        x,y = map(lon,lat)
        map.plot(x,y,'ro')

    plt.title("Incoming IP Address").set_fontsize(50)
    plt.show()


def get_ip(ip):
    
    url = "http://ipinfo.io/{}".format(ip)
    response = urlopen(url)
    data = json.load(response)

    ip=data['ip']
    org=data['org']
    city=data['city']
    country=data['country']
    region=data['region']
    location=data['loc']

    ## I can comment this out and return one answer...  this will work better
    for lat,lon in (pair.split(',') for pair in location.split()):
        latitude = lat
        longitude = lon
        #print("Latitude : ", lat, "\nLongitude : ", lon)
        
    return latitude, longitude    

def connect():

    bag = []
    sqlite_db = '/root/github/HPotter/main.db'
    table_name = 'hpotterdb'
    column1 = 'id'
    column2 = 'sourceIP'
    sql = "SELECT {col2} FROM {tn}". format(col2 = column2, tn=table_name)

    # Connect to db
    conn = sqlite3.connect(sqlite_db)
    c = conn.cursor()

    c.execute(sql)
    
    answer = c.fetchall()
    
    for x in answer:
        #print(x[0])   
        bag.append(x[0])

    #print(bag)

    globe(bag)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    connect()

