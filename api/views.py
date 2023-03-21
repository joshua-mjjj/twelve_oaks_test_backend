import requests
import json

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse 
from backend.settings import YELP_API_END_POINT, API_KEY, YELP_API_DETAIL_POINT
from django.core.cache import cache
from .external_api import get_restaurants_data, get_restaurant_detail_data
from .utils import query_restaurant_obj


# Get Resturants data
@api_view(['GET'])
@permission_classes([AllowAny,])
def GetResturantsData(request): 
    try: 
        if request.method == 'GET':
            location = request.GET.get('location')
            search_term = request.GET.get('search_term')

            if location and search_term:
                restaurant_data = get_restaurants_data(location, search_term)

                restaurant_data_list = []
                for restaurant in restaurant_data['businesses']:
                    # print(restaurant)
                    data_object = query_restaurant_obj(restaurant)

                    restaurant_data_list.append(data_object)
                    restaurants_list = {
                      'data' : restaurant_data_list
                    }
                return JsonResponse(restaurants_list, status=status.HTTP_200_OK)
            else: 
                sample_error_message = {
                  'message' : 'Please provide a location and search item'
                }
                return Response(sample_error_message, status=status.HTTP_400_BAD_REQUEST)
    except:
        sample_error_message = {
              'message' : 'Please provide a location and search item'
            }
        return Response(sample_error_message, status=status.HTTP_400_BAD_REQUEST) 


# Get Resturants detail data
@api_view(['GET'])
@permission_classes([AllowAny,])
def GetResturantsDetailData(request, pk):
    if pk:
        restaurant_detail_data = get_restaurant_detail_data(pk)
        if restaurant_detail_data != None:
            data_object = query_restaurant_obj(restaurant_detail_data)
            restaurants_detail = {
              'data' : data_object
            }
            return JsonResponse(restaurants_detail, status=status.HTTP_200_OK)
        else:
            sample_error_message = {
              'message' : 'Please provide a valid id'
            }
            return Response(sample_error_message, status=status.HTTP_400_BAD_REQUEST)
    else: 
        sample_error_message = {
          'message' : 'Please provide a valid id'
        }
        return Response(sample_error_message, status=status.HTTP_400_BAD_REQUEST)
    






