# Featherweight geocoding service
Lightweight and extensible wrapper around geocoding services supporting extension in a simple interface under 100 lines.

### Running the software
1) Edit set_environment_variabbles.sh using your preferred text editor and paste in your api keys.
2) Run ```. ./set_environment_variables.sh``` to set the environment variables which will be read by the application.

### Demo 
1) After setting evironment variables, run ```python application.py``` and this will deploy the service to localhost at http://0.0.0.0:5000/
2) Done! You can now make api calls to the service. Run the script ```./examples.sh``` which contains examples using cURL from a few different scenarios, and this will produce the following output:
```
Demo Apple Campus: 1 Infinite Loop, Cupertino
{"lat":37.33177,"lon":-122.03042,"service":"here","success":true}
Demo Fallback to Google Maps API: 201 3rd St num200
{"lat":37.7850203,"lon":-122.3999147,"service":"google","success":true}
Demo Unresolved Address: 11011 Fake Dr. Suite 1001b
{"error_message":"Unable to geocode given query. Address not found","success":false}
```

### API Documentation
# Status Check
A call to the API root will serve as a check as to whether the service is operational 

**URL** : `/api/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`
"Geocoding Proxy Service. Ok."

===================================

# Status Check
A call to the API root will serve as a check as to whether the service is operational 

**URL** : `/api/resolveCoordinates`

**Method** : `POST`

**Auth required** : YES, via environment variables

**Permissions required** : None

### Required parameters
```
query: A String containing the query address
```
### Response parameters
```
lat: The number representing the latidude of the resolved address
lon: The number representing the longitude of the resolved address
success: Boolean representing whether the address was correctly resolved
service: Which service was used to resolve the address to coordinates
```

### Success Response

**Code** : `200 OK`
"Geocoding Proxy Service. Ok."

**Usage examples**

For a query containing the string "1 Infinite Loop, Cupertino" 

##### Sample Input Parameters

```json
{
    "query": "1 Infinite Loop, Cupertino",
}
```
##### Sample Output Response
```json
{
    "lat": 37.33177,
    "lon": -122.03042,
    "service": "here",
    "success": "true"
}
```
