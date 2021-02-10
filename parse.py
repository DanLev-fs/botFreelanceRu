from bs4 import BeautifulSoup
import requests

s = requests.Session()
s.headers.update({"Host": "freelance.ru",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/x-www-form-urlencoded",
	"Origin": "https://freelance.ru",
	"Connection": "keep-alive",
	"Referer": "https://freelance.ru/login/"})
payload = "login=DanLev&passwd=Trb4dro83&check_ip=on&submit=%C2%F5%EE%E4&auth=auth&return_url=%2F"
txt = """
                    """

def auth():
	s.post('https://freelance.ru/login/', data=payload)
	
def parse():
	res = []
	i = 1
	while i != 5:
		html = s.get("https://freelance.ru/project/search/pro?c%5B0%5D=4&q=python&m=or&e=&f=&t=&o=1&page="+str(i)+"&per-page=25")
		soup = BeautifulSoup(html.text)
		mydivs = soup.findAll("div", {"class": "box-shadow project"})
		for div in mydivs:
			if div.find('div', {"class": "col-md-3"}).find("a", href=True) == None and div.find("img", {"alt": "Спец проект"}) == None:
				html = s.get("https://freelance.ru"+div.find('a', {"class": "description"})["href"])
				soup = BeautifulSoup(html.text)
				res.append([str(div.find('h2', {"class": "title"})["title"]), str(soup.find("p", {"class": "txt href_me"}).text), "https://freelance.ru"+str(div.find('a', {"class": "description"})["href"])])
		i+=1
	return res
