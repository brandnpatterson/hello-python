import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

for t in todos:
    message = 'is complete'
    id = t['id']

    if (t['completed'] == False):
        message = message.split(' ')
        message.insert(1, 'not')
        message = ' '.join(message)

    print(f'Todo {id} {message}')
