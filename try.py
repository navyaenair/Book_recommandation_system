import requests
import urllib.parse


class Request:
     def __init__(self,method,args): 
         self.args=args
         self.method=method

request=Request('GET',{'search':"java"})

if request.method == 'GET':
     search=urllib.parse.quote(request.args.get('search',''))
     url=f'https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5'
     response=requests.get(url)
     #print(response.json())

     if response.status_code==200: #200 means the request was successful ,400 means not found,401 means unauthorized
        data =response.json()
        for item in data.get('items',[]):
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', 'N/A')
            publisher = volume_info.get('publisher', 'N/A')
            published_date = volume_info.get('publishedDate', 'N/A')
            authors = volume_info.get('authors', ['N/A'])
            rating = volume_info.get('averageRating', 'N/A')
            image_links = volume_info.get('imageLinks', {})
            image = image_links.get('thumbnail', 'N/A')

            # Print or process the data as needed
            print(f"Title: {title}")
            print(f"Publisher: {publisher}")
            print(f"Published Date: {published_date}")
            print(f"Authors: {', '.join(authors)}")
            print(f"Rating: {rating}")
            print(f"Image: {image}")
            print("-" * 40)

            