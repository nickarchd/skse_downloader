import pytermgui as ptg

class WindowTUI:
	
	def __init__(self):
		self.objects = []
	
	
	
	def render(self):
		with ptg.WindowManager() as manager:
			manager.layout.add_slot("Body")
			
			manager.add(
				ptg.Window("AUI")
			)
		