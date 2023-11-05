import requests

def perform_search(query):
    api_key = "AIzaSyBIXxHTSQLsbwJMkdgtkpkjHAkjcA-iTfg"
    search_engine_id = "16a46851ef7c84852"
    url = f'https://www.googleapis.com/customsearch/v1'
    params = {
        'key' : api_key,
        'cx' : search_engine_id,
        'q' : query,
        'num' : 1,
        # 'siteSearch': 'wikipedia.org'
    }

    try :
        response = requests.get(url, params=params)
        data = response.json()
        if 'items' in data:
            for index,item in enumerate(data['items'],1):
                # print(f"{index} {item['title']}")
                return (str(item['snippet']))
        else:
            return None
    except requests.RequestException as err:
        return None



