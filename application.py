#!/usr/bin/env python
from flask import Flask, request, jsonify
import os
import requests
import json

application = Flask(__name__)

@application.route("/api", methods=['Get'])
def landing():
    """
    Informational landing display for Simple Geocoding Proxy.
    """
    return jsonify("Geocoding Proxy Service. Ok.")

@application.route("/api/resolveCoordinates", methods=['POST'])
def resolve_coordinates():
    """
    Resolve cordinates given an address.
    Parameters:
        Address - String address representing the desired location.
    Returns:
        Response - JSON encoded response
          {lat: Latitude of coordinate,
          lon: Longitude of coordinate,
          service: Service used to resolve coordinates}
    """
    request.data = eval(request.data)
    address = request.data.get("query").strip().lower()
    return jsonify(geocode_api_wrapper(address))

def geocode_api_wrapper(query):
    """
    Wrap API functions and call them with descending priority.
    """
    #Add new apis to end of list as necessary
    api_sequence = [handle_here_api, handle_google_api]
    success = False
    for api in api_sequence:
        if success != True:
            response = api(query)
            success = response['success'] 
    if success == False:
        response["error_message"] = "Unable to geocode given query. Address not found"
        print("Unable to resolve using any of the APIs")
    return response

def handle_here_api(query):
    """
    Use Here as primary API.
    """
    print("Trying HERE API")
    raw_response = requests.get(
    'https://geocoder.api.here.com/6.2/geocode.json',
    params={'app_id': os.environ['HERE_APP_ID'],
           'app_code': os.environ['HERE_APP_CODE'],
           'searchtext': query},
 )
    response = {}
    try:
        coords = json.loads(raw_response.text)['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
        response['lat'] = coords['Latitude']
        response['lon'] = coords['Longitude']
        response['success'] = True
        response['service'] = 'here'

    except (KeyError, IndexError) as e:
        print(e)
        print('Failure')
        response['success'] = False
    return response

def handle_google_api(query):
    """
    Fallback to Google Maps in event of Here API Failure
    """
    print("Trying Google Maps API")
    raw_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json',
            params={'key':os.environ["GOOGLE_API_KEY"],
                    'address': query})
    response = {}
    try:
        coords = json.loads(raw_response.text)['results'][0]['geometry']['location']
        response['lat'] = coords['lat']
        response['lon'] = coords['lng']
        response['success'] = True
        response['service'] = 'google'
    except (KeyError,IndexError) as e:
        print(e)
        print('Failure')
        response['success'] = False
    return response

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)
