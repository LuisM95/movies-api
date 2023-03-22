from dotenv import load_dotenv
import requests, os

# URL = 'http://localhost:8000/api/v1/reviews?page=2&limit=4' first form of queryset 

load_dotenv()
URL = os.getenv('URL')
credentials = os.getenv('USER')

response = requests.post(URL +' login', json=credentials)

if response.status_code == 200:
    print('User Login Successfully!')
    #print(response.json())
    #print(response.cookies)
    #print(response.cookies.get_dict())

    user_id = response.cookies.get_dict().get('user_id')
    #print(user_id)

    cookies = {'user_id':user_id}
    response = requests.get(URL + 'reviews', cookies= cookies)

    if response.status_code == 200:
        for review in response.json():
            print(f"{review['review']} - { review['score']}")

            
"""REVIEW_ID = 6
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

REVIEW = {
    'review':'New Review from requests',
    'score':5
}

#response = requests.put(URL,json=REVIEW) update
response = requests.delete(URL,json=REVIEW) #delete

if response.status_code == 200:
    print("The Review has delete Successfully")
    print(response.json())"""

"""REVIEW= {
    'user_id':1,
    'movie_id': 1,
    'review': 'Review creada con requests',
    'score': 4
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print("Review created successfully!")
else:
    print(
        response.content
    )"""
"""HEADERS = { 'accept': 'application/json'}
QUERYSET = {'page':2, 'limit':4}

response = requests.get(URL, headers=HEADERS, params=QUERYSET)

if response.status_code == 200:
    print("Request made Successfully")

    if response.headers.get('content-type') == 'application/json':
        reviews = response.json()
        for review in reviews:
            print(f"=> Score: {review['score']} - {review['review']} ")"""


