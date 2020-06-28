#!/usr/bin/env python

__author__ = 'chrisescobedo0617'

import requests
import turtle
import time

def get_astronauts_list():
    space_list = []
    response = requests.get('http://api.open-notify.org/astros.json')
    json_response = response.json()
    for value in json_response.get('people'):
        if value.get('craft') not in space_list:
            space_list.append(value.get('craft'))
        space_list.append(value.get('name'))
    space_list.append(json_response.get('number'))
    print(f'Astronaunts in space are {", ".join(space_list[1:6])} and they are all on board the {space_list[0]}. Total num of people in space is {space_list[-1]}')


location_dict = {}

def get_lat_long_time():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    json_response = response.json()
    location_dict['latitude'] = json_response.get('iss_position').get('latitude')
    location_dict['longitude'] = json_response.get('iss_position').get('longitude')
    location_dict['timestamp'] = json_response.get('timestamp')
    return location_dict


def show_map():
    indy_long = -86.148003
    indy_lat = 39.791000
    get_lat_long_time()
    map_ = turtle.Screen()
    map_.setup(height=.48, width=.56)
    map_.bgpic("map.gif")
    map_.setworldcoordinates(-180,-90,180,90)
    iss = 'iss.gif'
    map_.addshape(iss)
    turtle.shape(iss)
    turtle.goto(float(location_dict.get('longitude')),float(location_dict.get('latitude')))
    dot = turtle.Turtle()
    dot.goto(indy_long,indy_lat)
    dot.dot('yellow')
    indy_response = requests.get('http://api.open-notify.org/iss-pass.json?lat=39.791000&lon=-86.148003')
    indy_json_response = indy_response.json()
    indy_timestamp = indy_json_response.get('response')[0].get('risetime')
    timestamp = turtle.Turtle()
    timestamp.goto(indy_long + 5,indy_lat +5)
    timestamp.write(time.ctime(indy_timestamp),font=("Arial",9,"bold"))
    print(time.ctime(indy_timestamp))
    map_.exitonclick()


def main():
    get_astronauts_list()
    show_map()


if __name__ == '__main__':
    main()