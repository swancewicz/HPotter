#!/usr/bin/python3


import matplotlib.pyplot as plt
import numpy as np
import re
import json
import sqlite3
import folium
from mpl_toolkits.basemap import Basemap
from urllib.request import urlopen

# Folium imports
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt



def world_map(value1, value2):

    # size of window
    plt.figure(num=None, figsize=(24,24))
    
    map = Basemap(projection='robin', lat_0=0, lon_0=0,)

    #map.bluemarble()
    map.drawmapboundary(fill_color='#A6CAE0')
    map.fillcontinents(color='grey', alpha=0.3)

    # plot geo location from ip
    lat,lon=value1, value2
    x,y = map(lon,lat)
    map.plot(x,y,'ro')

    plt.title("Attacker's IP")
    #plt.title('contour lines over filled continent background')
    plt.show()



def globeorigional(value1, value2):

    #map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
    map = Basemap(projection='ortho', resolution='l', lat_0=50, lon_0=0)

    # size of window
    plt.figure(figsize=(16,16))

    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)
    map.drawstates(linewidth=0.24)
    map.fillcontinents(color='dimgray',lake_color='darkgray')
    #map.fillcontinents(color='coral',lake_color='aqua')


    #map.bluemarble()
    # draw the edge of the map projection region (the projection limb)
    map.drawmapboundary(fill_color='darkgray')

    # draw lat/lon grid lines every 30 degrees.
    #map.drawmeridians(np.arange(0,360,30))
    #map.drawparallels(np.arange(-90,90,30))

    ## plot geo location from ip
    lat,lon=value1, value2
    x,y = map(lon,lat)
    map.plot(x,y,'bo')
    #map.plot(x,y,'r')

    # contour data over the map.
    #cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
    plt.title("Incoming IP Address")
    #plt.title('contour lines over filled continent background')
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



def globe(ip_list):

    map = Basemap(projection='robin', lat_0=0, lon_0=0,)
    #map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
    #map = Basemap(projection='ortho', resolution='l', lat_0=50, lon_0=0)

    # size of window
    plt.figure(figsize=(24,24))

    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)
    map.drawstates(linewidth=0.24)
    map.fillcontinents(color='dimgray',lake_color='darkgray')
    #map.fillcontinents(color='coral',lake_color='aqua')

    #map.bluemarble()
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

    plt.title("Incoming IP Address")
    plt.show()



def main():

    ## n.korea,russia,africa,colorado
    list_of_ips = ["2.63.255.255", "27.106.204.0", "41.31.255.255 ", "73.95.156.214", "2.191.255.255"]
    
    sqlite_file = '/root/github/HPotter/main.db'
    table_name = 'test_IP_matplotlib'
    column_name = 'IP_address'
    
    # Connect to db
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM {tn} WHERE {cn}'. format(tn=table_name, cn=column_name))
    
    # can use fetchall()
    result = c.fetchone() 
    if result:
        #print(result[0])
        answer = result[0]

    globe(list_of_ips)
    #world_map(list_of_ips)
    conn.commit()
    conn.close()



main()

