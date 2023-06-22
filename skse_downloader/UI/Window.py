import tkinter as tk
import tkinter.ttk as ttk
from skse_downloader.Utils import VERSION_MAJOR, VERSION_MINOR, VERSION_BUILD
import skse_downloader.Scrape as Scrape
import skse_downloader.Links as Links


class WindowTK:
	root: tk.Tk = None
	rows = 0
	cols = 0
	
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("500x650")
		self.root.title(f"SKSE Downloader {VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_BUILD}")

		self.frame = tk.Frame(self.root)

		self.treeview = ttk.Treeview(self.root, show='headings', height=8)
		self.treeview.pack()
		
		self.root.columnconfigure(0, weight=1)
		self.root.columnconfigure(1, weight=3)
		self.prepare()
		pass
	
	def prepare(self):
		page = Scrape.load_page()
		links = Links.generate_links(page)
		self.rows = len(links)
		self.cols = 3
		self.prepare_grid(links)
		
	def prepare_grid(self, links):
		self.treeview['columns'] = ('game_id', 'game_link', 'game_version')
		
		headers = {
			"game_id": "Game",
			"game_link": "Link",
			"game_version": "Version"
		}
		
		for key, value in headers.items():
			self.treeview.column(key, anchor=tk.CENTER, width=80)
			self.treeview.heading(key, text=value, anchor=tk.CENTER)
	
		for link in links:
			self.treeview.insert(parent='', index=0, values=(link.text, link.link_text, link.link))
		
		self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
		
	def run(self):
		self.root.mainloop()
		