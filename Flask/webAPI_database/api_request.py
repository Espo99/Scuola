import requests

URL = "http://127.0.0.1:5000/allBooks"

def ricercaPerId(id):
    PARAMS = {'id':id}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()[PARAMS['id']]
    print(f"libro cercato --> {data}")

def tuttiLibri():
    r=requests.get(url=URL)
    data = r.json()
    for i in data:
        print(i)



tuttiLibri()
print("^^^^")
ricercaPerId(1)



#data = r.json()[PARAMS['id']]
#print(data['title'])