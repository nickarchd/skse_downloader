from bs4 import BeautifulSoup
import urllib.request
import pathlib

def load_page():
	"loads a page from internet (silverlock)s"
	try:
		with open("cache.html", "rb") as f:
			data = f.read().decode('utf-8')
	except FileNotFoundError as e:
		data = save_page_html("https://skse.silverlock.org")
		save_page_cache("cache.html", data)
	bs = Scrape(data)
	return bs

def delete_cache():
	"Just delete the html cache"
	try:
		with open("cache.html", "rb") as f:
			cache = pathlib.Path("cache.html")
			cache.unlink()
			return True
	except FileNotFoundError:
		return False

def delete_cache_recreate():
	"delete the html cache and create a new cache downloading from internet"
	try:
		with open("cache.html", "rb") as f:
			cache = pathlib.Path("cache.html")
			cache.unlink()
			return load_page()
	except FileNotFoundError:
		return None
def save_page_html(url):
	"""loads the page and return as string"""
	with urllib.request.urlopen(url) as f:
		html = f.read()
		return html

def save_page_cache(in_file: str, html_data):
	"""save page buffer to disk"""
	with open(in_file,"wb") as fp:
		fp.write(html_data)
		return True
	
def load_page_from_file(out_file):
	"""load page from disk"""
	with open(out_file, "rb") as fp:
		return fp.read()
	
def Scrape(file_in) -> BeautifulSoup:
	"""scrape the page and returns as Beautiful Soup Object"""
	bs = BeautifulSoup(file_in, 'html.parser')
	return bs


