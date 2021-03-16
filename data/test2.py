from requests import post, get

print(get('http://localhost:5000/api/v2/news').json())
print(post('http://localhost:5000/api/v2/news',
           json={'title': 'NNN',
                 'content': 'PPP',
                 'user_id': 1,
                 'is_private': False}).json())