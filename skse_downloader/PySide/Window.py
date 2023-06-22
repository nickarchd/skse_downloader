import sys

import PySide6.QtGui as gui
import PySide6.QtCore as core
import PySide6.QtWidgets as widgets

from PySide6.QtUiTools import QUiLoader
import skse_downloader.resource
from skse_downloader.Config2 import  Config
from skse_downloader.PySide.DownloadTableProxy import DownloadTableProxy

class MainApplication(widgets.QApplication):
	def __init__(self, **kwargs ):
		widgets.QApplication.__init__(self, sys.argv)
		
		if "config" in kwargs:
			self.cfg: Config = kwargs["config"]
		if "data" in kwargs:
			self.data = kwargs["data"]
		
		self.loader()
		self.connectActions()
		
		
	def loader(self):
		self.uiloader = QUiLoader()
		self.window = self.uiloader.load(":main.ui")
		
		source = self.cfg.get("config", "url")
		self.window.cpSource.setPlainText(source)
		
		path = self.cfg.get("config", "skyrim_path")
		self.window.cpGamePath.setPlainText(path)
		title_str = self.cfg.get("config", "window_title")
		title =  title_str if not title_str  else "SKSE Downloader"
		self.window.setWindowTitle(title)
		
		
	def connectActions(self):
		self.window.acFetchDownloads.triggered.connect(self.fetchDownloadResponse)
		self.window.acSavePath.triggered.connect(self.saveGameFilePath)
		
		self.window.btFetchDownload.setDefaultAction(self.window.acFetchDownloads)
		self.window.btSavePath.setDefaultAction(self.window.acSavePath)
		
		self.window.acAboutQt.triggered.connect(lambda: self.aboutQt())
		
		self.downloadModel = DownloadTableProxy(self, self.cfg)
		self.window.cTable.setModel(self.downloadModel)
		
		gen_cache = bool(self.cfg.get("config", "cache"))
		self.window.checkGenCache.setChecked(gen_cache)
	
	def run(self):
		self.window.showNormal()
		sys.exit(self.exec_())
		
	@core.Slot()
	def fetchDownloadResponse(self):
		print("Clicado!!!")
		
		
	@core.Slot()
	def saveGameFilePath(self):
		#print("Savepath")
		dlg = widgets.QFileDialog.getExistingDirectory(caption="Select Folder")
		
		if dlg:
			self.cfg.set("config", "skyrim_path", dlg)
			
			#self.cfg.save_all()
			
			print("Sucesso!")
			return
		
		print("falha")
		
		
	
def run(**kwargs):
	app = MainApplication(**kwargs)
	app.run()