import numpy as np
import pandas as pd
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyDeCsaoAAMATv2BaZjYkrtJabSEkl20E_o'

google_places = GooglePlaces(YOUR_API_KEY)

key_words=['theatre', 'museum','restaurant','shop','sightseeing','beach', 'food market','point of interest','attraction','casino']
query_results=[None]*len(key_words)

i=0
for kw in key_words:
    # You may prefer to use the text_search API, instead.
    query_results[i] = google_places.nearby_search(location='tel aviv, israel', keyword=kw, radius=10000, types=[types.TYPE_FOOD])
    
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:
    # http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

    if query_results[i].has_attributions:
        print (query_results[i].html_attributions)

    i+=1



name = []
geo_location_lat = []
geo_location_lng = []
address = []
place_id = []

local_phone_number = []
website = []
url = []

rating = []
type_of_the_attraction = []


i_place=0

for query_result in query_results:
    for place in query_result.places:
        #print(place)
        name.append(place.name)
        geo_location_lat.append(place.geo_location['lat'])
        geo_location_lng.append(place.geo_location['lng'])
        place_id.append(place.place_id)
        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        #dataFrameRestraunts['details'] = place.details # A dict matching the JSON response from Google.
        local_phone_number.append(place.local_phone_number)
        website.append(place.website)
        url.append(place.url)
        rating.append(place.rating)
        address.append(place.formatted_address)
        type_of_the_attraction.append(place.types)
        i_place+=1

        
        if i_place%10==0:
            print(i_place)

dataFrameStore3 = pd.DataFrame()
dataFrameStore3['name'] = name
dataFrameStore3['geo_location_lat'] = geo_location_lat
dataFrameStore3['geo_location_lng'] = geo_location_lng
dataFrameStore3['address'] = address
dataFrameStore3['rating'] = rating
dataFrameStore3['type_of_the_attraction'] = type_of_the_attraction
dataFrameStore3['place_id'] = place_id
dataFrameStore3['local_phone_number'] = local_phone_number
dataFrameStore3['website'] = website
dataFrameStore3['url'] = url

dataFrameStore3.to_csv("dataFrameAll_.csv",encoding='UTF-8',index=False)
