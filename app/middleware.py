import http.client
import json

class Moviesmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "8f04ef8676mshe89d5170fe5a229p141dafjsn253a67c2af04"
        }

        conn.request("GET", "/title/auto-complete?q=game%20of%20thr", headers=headers)

        res = conn.getresponse()
        data = res.read()
        dict_data = json.loads(data)
        json.dump(dict_data,open("app/raw/movies.json","w"))
        print("Data written successfully")

    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        return response
