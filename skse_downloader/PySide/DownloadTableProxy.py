from typing import Any

import PySide6
import PySide6.QtCore as _qc
import PySide6.QtGui as _qg

class DownloadTableProxy(_qc.QAbstractTableModel):
	
	header = (
		_qc.QT_TRANSLATE_NOOP('dados', "Game"),
		_qc.QT_TRANSLATE_NOOP('dados', "Version"),
		_qc.QT_TRANSLATE_NOOP('dados', "Link")
	)
	
	def __init__(self, parent, data= None):
		_qc.QAbstractTableModel.__init__(self, parent)
		
	def rowCount(self, parent = None):
		return 1
	
	def columnCount(self, parent = None) -> int:
		return 3
	
	def data(self, index, role):
		if not index.isValid():
			return None
		
		if role not in (_qc.Qt.ItemDataRole.DisplayRole, _qc.Qt.ItemDataRole.EditRole):
			return None
		
	def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
		if role != _qc.Qt.ItemDataRole.DisplayRole:
			return None
		
		if orientation == _qc.Qt.Orientation.Horizontal:
			if section == 0:
				return self.header[0]
			if section == 1:
				return self.header[1]
			if section == 2:
				return self.header[2]
			
		
		
	