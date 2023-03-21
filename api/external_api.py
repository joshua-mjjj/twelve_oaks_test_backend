import requests
import json

from backend.settings import YELP_API_END_POINT, API_KEY, YELP_API_DETAIL_POINT
from django.core.cache import cache



def get_restaurants_data(location, search_term):
    
    cache_key = f'restaurant_data:{location}:{search_term}'
    restaurant_data = cache.get(cache_key)
    if restaurant_data is not None:
       # Returning cached version
        return restaurant_data

    headers = {'Authorization': 'Bearer %s' % API_KEY}
    params = {'location': location, 'term': search_term}
    url = YELP_API_END_POINT + '?location=' + location + '&term=' + search_term

    # Make the API request to YELP
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        cache.set(cache_key, data, timeout=300) 
        return data
    else:
        print('Error:', response.status_code)
        return None

def get_restaurant_detail_data(restaurant_id):
    
    cache_key = f'restaurant_detail_data:{restaurant_id}'
    detail_data = cache.get(cache_key)
    if detail_data is not None:
        # Returning cached version
        return detail_data

    headers = {'Authorization': 'Bearer %s' % API_KEY}
    url = YELP_API_DETAIL_POINT + '/' + restaurant_id

    # Make the API request to YELP
    response = requests.get(url, headers=headers)

    # Parse the JSON data
    if response.status_code == 200:
        data = json.loads(response.text)
        cache.set(cache_key, data, timeout=300) 
        return data
    else:
        print('Error:', response.status_code)
        return None