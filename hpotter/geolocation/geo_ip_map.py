#!/usr/bin/python3

import sqlite3
import folium
import pandas as pd
import webbrowser
from urllib.request import urlopen # need this to stay in here
import json



def folium_Mapbox_Control_Room(ip_list):

    f = folium.Figure(width=1000, height=500)
    map = folium.Map(location=[20,0], tiles="Mapbox Control Room", zoom_start=3, min_zoom=2).add_to(f)


    ## This loop fill in ip,lat,lon into dataFrame
    data = pd.DataFrame([])
    for ip in ip_list:
        lat,lon = get_ip(ip)
        data = data.append(pd.DataFrame({'lat': lat, 'lon': lon, 'IP':ip}, index=[0]), ignore_index=True)


    local_ipv4, local_ipv6= "127.0.0.1", "::1"
    previous_ip = []  # Prevents re-iterating through ip's already plotted

    for ip in ip_list:
        if ip == local_ipv4 or ip == local_ipv6:
            previous_ip.append(ip) 
            
        if not ip in previous_ip:
            lat,lon = get_ip(ip)

            folium.Marker(location=[float(lat),float(lon)], popup=ip).add_to(map)
            previous_ip.append(ip)

    map.save(outfile='MapboxControlRoom.html')

    ## Open in default browser
    webbrowser.open('MapboxControlRoom.html')
    ## To open in non-default browser
    #webbrowser.get('firefox').open_new_tab('test3.html')




def folium_OpenStreetMap(ip_list):

    f = folium.Figure(width=1000, height=500)
    map = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=3, min_zoom=2).add_to(f)


    ## This loop fill in ip,lat,lon into dataFrame
    data = pd.DataFrame([])
    for ip in ip_list:
        lat,lon = get_ip(ip)
        data = data.append(pd.DataFrame({'lat': lat, 'lon': lon, 'IP':ip}, index=[0]), ignore_index=True)


    local_ipv4, local_ipv6= "127.0.0.1", "::1"
    previous_ip = []  # Prevents re-iterating through ip's already plotted

    for ip in ip_list:
        if ip == local_ipv4 or ip == local_ipv6:
            previous_ip.append(ip) 
            
        if not ip in previous_ip:
            lat,lon = get_ip(ip)

            folium.Marker(location=[float(lat),float(lon)], popup=ip).add_to(map)
            previous_ip.append(ip)


    map.save(outfile='OpenStreetMap.html')

    ## Open in default browser
    webbrowser.open('OpenStreetMap.html')
    ## To open in non-default browser
    #webbrowser.get('firefox').open_new_tab('test3.html')



def get_ip(ip):

    latitude, longitude = "", ""
    url = "http://ipinfo.io/{ip}".format(ip=ip)
    
    response = urlopen(url)
    data = json.load(response)
    
    ip = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    location = data['loc']

    #  I can comment this out and return one answer...  this will work better
    for lat, lon in (pair.split(',') for pair in location.split()):
        latitude = lat
        longitude = lon
       # print("Latitude : ", lat, "\nLongitude : ", lon)
        
    return latitude, longitude    



def connect():

    bag_of_ips = []

    # Change path for your machine's main.db location, starting at the top level (Windows: C:/, E:/ F:/, etc. Linux will start at /root/...)
    sqlite_db = '/root/github/HPotter/main.db'
    table_name = 'hpotterdb'
    column1 = 'id'
    column2 = 'sourceIP'
    sql = "SELECT {col2} FROM {tn};". format(col2=column2, tn=table_name)
    
    # Connect to db
    conn = sqlite3.connect(sqlite_db)
    c = conn.cursor()

    c.execute(sql)
    
    answer = c.fetchall()
    
    for x in answer:
        bag_of_ips.append(x[0])

    ## Launch maps    
    folium_OpenStreetMap(bag_of_ips)
    folium_Mapbox_Control_Room(bag_of_ips)

    conn.commit()
    conn.close()




if __name__ == '__main__':
    connect()

