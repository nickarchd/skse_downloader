import configparser
import sys
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Config:
    DEFAULT = {
        'config': {
            'url': r"https://skse.silverlock.org",
            'cache_name': 'cache.html',
            'skyrim_path': r"C:\Program Files\Skyrim",
            'delete_cache_after': '15 days',
            'cache': 1,
            'window_title': f"SKSE Downloader"
        }
        
    }

    config_path = ""
    filename = "config.cfg"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config['config'] = self.DEFAULT['config']
        self.config_path = Path(self.filename).absolute()

    
    def write_conf(self):
        with open(self.config_path,"w") as fp:
            self.config.write(fp)
            
    def load(self) -> object:
        
        if not self.config.read(self.config_path):
            #raise Exception(f"{self.config_path} not found")
            with open(self.config_path, "w") as f:
                self.config['config'] = self.DEFAULT['config']
                self.write_conf()
                self.load()
        
        return self.config.sections().copy()
        
    def set(self, group, key, value) -> bool:
        
        if not self.config.set(group, key, value):
            raise Exception("Config Section: {0} and {1} key not found!".format(group,key))
        return True
    
    def get(self, group: str, key: str) -> str:
        if not self.config.get(group, key):
            raise Exception(f"Config Section: {group} and {key} key not found!")
        
        val = self.config.get(group, key)
        return val
    
    def get_bool(self, section: str, key: str) -> bool:
        return self.config.getboolean(section, key)
    
    def check_config_exists(self):
        found = False
        try:
            with open(self.config_path,"r") as fp:
                found = True
        except IOError as err:
            print(err)
        
        return found
    
    def print_cfg(self) -> None:
        
        for section in self.config.sections():
            for keys in self.config[section]:
                print(f"Section:{section} -> {keys} : {self.config[section][keys]}")
                
    
    def __str__(self):
        return "Config Class"