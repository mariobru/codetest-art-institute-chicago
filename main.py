#!/usr/bin/env python3 
import requests
import csv
import json
import random
import argparse

def getConfig():
    parser = argparse.ArgumentParser(description='This script solves StyleSage Data Operations Coding Test, sending requests to AIC API.')
    parser.add_argument('-p', '--page', type=int, help='Enter the page number from 1 to 100 that the API request will use.')
    parser.add_argument('-l', '--limit', type=int, help='Set how many record each page should return.')
    args = parser.parse_args()
    return args


def getAgentsInfo(page='1', limit='12'):
    """
    This function will send a request to api.artic.edu and will get
    the following agent info:
    - id
    - title
    - description
    - artwork_ids
    - is_artist
    - agent_type_title

    It receives the following parameters:
    - page (max_value = 100)
    - limit (max_value = 100)
    """

    url = 'https://api.artic.edu/api/v1/agents?page={}&limit={}&fields=id,title,description,artwork_ids,is_artist,agent_type_title'.format(page, limit)
    response = requests.get(url)
    response = response.json()
    data = response['data']
    filtered_agents = [d for d in data if d['is_artist'] == True and d['agent_type_title'] == 'Individual']
    five_agents = filtered_agents[:5]
    return five_agents

def getArtworkInfo(artwork_id):
    """
    This function will get the following info from an artwork given its id:
    - title
    - artist_display
    - place_of_origin
    - medium_display
    - dimensions    
    """

    url = 'https://api.artic.edu/api/v1/artworks/{}?fields=title,artist_display,place_of_origin,medium_display,dimensions'.format(artwork_id)
    response = requests.get(url)
    response = response.json()
    data = response['data']
    return data

def gatherData(data):
    """
    This function will gather all the requested info and will 
    return it as a list of dictionaries.
    """

    filtered_data = []
    for d in data:
        r = random.randrange(len(d['artwork_ids']))
        rand_artwork = d['artwork_ids'][r]
        artwork_info = getArtworkInfo(rand_artwork)
        agent = {}
        agent['title'] = d['title']
        agent['description'] = d['description']
        agent['artwork_ids'] = d['artwork_ids']
        agent['num_artworks'] = len(d['artwork_ids'])
        agent['rand_artwork'] = rand_artwork
        agent['artwork_title'] = artwork_info['title']
        agent['artist_display'] = artwork_info['artist_display']
        agent['place_of_origin'] = artwork_info['place_of_origin']
        agent['dimensions'] = artwork_info['dimensions']
        agent['medium_display'] = artwork_info['medium_display']
        filtered_data.append(agent)
    return filtered_data

def saveCSV(filtered_data):
    """
    This function will save all gathered data as CSV file.
    """

    keys = filtered_data[0].keys()
    with open('export.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(filtered_data)
    print("The CSV file has been saved in the current directory.")

def main():
    config = getConfig()
    data = getAgentsInfo(config.page)
    filtered_data = gatherData(data)
    saveCSV(filtered_data)

if __name__=='__main__':
    main()