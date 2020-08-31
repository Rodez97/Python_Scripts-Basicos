import requests

url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCHrKd8ElaVdk7OBQAgx8JrQpip'
datos = requests.get('https://www.youtube.com/feeds/videos.xml?channel_id=UCHrKd8ElaVdk7OBQAgx8JrQpip')
print(datos)