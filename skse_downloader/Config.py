
import os
import stat
import configparser
from pathlib import Path
from skse_downloader.Utils import VERSION_MAJOR, VERSION_MINOR, VERSION_BUILD

class Config(object):
	
	DEFAULT = {
		'config': {
			'url': r"https://skse.silverlock.org",
			'cache_name': 'cache.html',
			'skyrim_path': r"C:\\",
			'delete_cache_after':  '15 days',
			'cache': 1,
			'window_title': f"SKSE Downloader {VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_BUILD}"
		}
		
	}
	
	keys = {}
	filename = "config.cfg"
	path = ""
	
	
	"""Class to load Config File"""
	def __init__(self, config_file: str = "config.cfg"):
		
		self.cfg = configparser.ConfigParser()
		
		self.path = Path(config_file).absolute()
		
		if not Config.config_file_exists(config_file):
				self.save_default(self.path)
				self.keys = self.load(config_file)
				self.filename = config_file
				return

		self.keys = self.load(self.path)
		self.filename = config_file
		
		
	def save_all(self):
		self.save(self.filename)
	
	def load_all(self):
		self.load(self.filename)
	def save(self, out_cfg):
		with open(out_cfg, "w") as fp:
			self.cfg.write(fp)
	def save_default(self, out_cfg):

		
		self.cfg['config'] = self.DEFAULT['config']
			
		with open(out_cfg, "w") as fp:
			self.cfg.write(fp)
			
		self.load(out_cfg)
	
	def set(self, group, key, value) -> bool:

		if not self.cfg.set(group, key, value):
			raise Exception("Config Section: {0} and {1} key not found!".format(group, key))
		return True
	
	def get(self, group: str, key: str) -> str:

		if not self.cfg.get(group, key):
			raise Exception(f"Config Section: {group} and {key} key not found!")
		
		val = self.cfg.get(group, key)
		return val
	
	def load(self, in_cfg):
		if not self.cfg.read(in_cfg):
			raise Exception(f"{in_cfg} not found!")

		return self.cfg.sections().copy()
		
	
	@staticmethod
	def config_file_exists(config_file : str):
	
		try:
			mode = os.lstat(config_file).st_mode
	
			if stat.S_ISDIR(mode) or stat.S_ISCHR(mode) or stat.S_ISLNK(mode):
				return False
			
			if stat.S_ISREG(mode):
				return True
		except FileNotFoundError:
			return False

		return False