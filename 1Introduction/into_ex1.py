import requests
from requests.exceptions import RequestException
import re
import html
from urllib.parse import urlparse

class Webscrap:
    def __init__(self, user_agent):
        self.headers = {'User-Agent': user_agent}

    def get_page(self, url, timeout=10, retries=3):
        try:
            print(f"Tentative de connexion à {url}...")
            
            response = requests.get(url, headers=self.headers, timeout=timeout)

            response.raise_for_status() 
            
            return response

        except RequestException as e:
            
            print(f"Erreur : {e}")
            
            if retries > 0:
                print(f"-> Il reste {retries} essais. On réessaie...")
                # APPEL RÉCURSIF : La fonction s'appelle elle-même avec un essai en moins
                return self.get_page(url, timeout, retries - 1)
            else:
                print("-> Échec définitif.")
                return None
            
scraper = Webscrap(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)...')

# 2. On appelle la méthode (le timeout est de 10 par défaut)
res = scraper.get_page("https://www.esiee.fr/")

if res:
    print(f"Statut : {res.status_code}")
    # On affiche les 100 premiers caractères
    print(res.text[:100])

 


