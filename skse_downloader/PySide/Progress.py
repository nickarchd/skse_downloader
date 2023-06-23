
import PySide6.QtWidgets as widgets
import PySide6.QtCore as core
class Progress(widgets.QWidget):
	def __init__(self, parent = None):
		widgets.QWidget.__init__(self)
		self.parent = parent
		self.pb = widgets.QProgressBar(self)
		self.setGeometry(0,0,230,20)
		self.pb.setGeometry(0,0,self.geometry().size().width(), self.geometry().size().height() )
		self.setWindowFlag(core.Qt.WindowType.Drawer | core.Qt.WindowType.WindowTitleHint)
		origin = self.parent.cfg.get("config", "url")
		self.setWindowTitle(f"Fetching Data From: {origin}")
		
		
	def closeEvent(self, event) -> None:
		event.ignore()
		
