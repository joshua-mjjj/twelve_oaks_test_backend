
# PQuery reqired data from restaurant object
def query_restaurant_obj(restaurant):
	data_object = {
        "id": restaurant['id'], 
        "name": restaurant['name'],
        "location": {
            "address1": restaurant['location']['address1'],
            "address2": restaurant['location']['address2'],
            "city": restaurant['location']['city'],
            "state": restaurant['location']['state'],
            "zip": restaurant['location']['zip_code'],
        }, 
        "image_url": restaurant['image_url'],
        "review_count": restaurant['review_count'],
        "rating": restaurant['rating'],
        "phone": restaurant['phone'],
        "categories": restaurant['categories'],
    }
	return data_object
