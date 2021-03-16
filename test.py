from requests import get, post, delete
print(post('http://localhost:5000/api/v2/news', json={
    'title': 'Первая запись',
    'content': 'Текст новости1',
    'user_id': 2,
    'is_private': False,
    'is_published': True}).json())
print(get('http://localhost:5000/api/v2/news').json())
print(get('http://localhost:5000/api/v2/news/1').json())
