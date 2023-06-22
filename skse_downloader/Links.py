from bs4 import BeautifulSoup
from typing import List

class LinkData(object):
	text: str
	link: str
	link_text: str

def generate_links(data : BeautifulSoup):
	
	p_tags = data.find_all("p")
	
	links: List[LinkData] = []
	
	for tag in p_tags:
		a_tags = tag.find_all('a')
		
		if not a_tags:
			continue

		for link in a_tags:
			
			data = LinkData()
			data.link = link.get('href')
			data.text = tag.getText()
			data.link_text = link.getText()
			links.append(data)
	return links
