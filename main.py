import requests
from bs4 import BeautifulSoup

headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
	"Connection": "keep-alive",
	"Host": "coderesbgonlinesbsbanners.azurewebsites.net",
	"If-Modified-Since": "Tue, 16 Aug 2022 18:18:23 GMT",
	"If-None-Match": "128fb10c-1f1a-42c8-a7f2-988e6bcfd8c3",
	"Origin": "https://m.apuestas.codere.es",
	"Referer": "https://m.apuestas.codere.es/",
	"sec-ch-ua": "'Chromium';v='104'", 
	"sec-ch-ua-mobile": "?0",
	"sec-ch-ua-platform": "Windows",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "cross-site",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

html_page = requests.get("https://coderesbgonlinesbsbanners.azurewebsites.net/api/feeds/events/5763188069", headers=headers)

print(html_page.status_code)
print(html_page.content)
soup = BeautifulSoup(html_page.content, "html.parser")
print(soup)



