import requests

print('--------------------------------------------------------')
print(requests.get('http://127.0.0.1:5000/').text)
requests.post('http://127.0.0.1:5000/', {'nums':7})
print(requests.get('http://127.0.0.1:5000/').text)
print('--------------------------------------------------------')