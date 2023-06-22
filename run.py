import skse_downloader.Scrape
from skse_downloader.Links import generate_links
from skse_downloader.Config import Config as Cfg
from skse_downloader.Config2 import Config as Cfg2
from skse_downloader.Utils import PlatformType, using_platform

if __name__ == "__main__":
	
	cfg = Cfg2()
	cfg.load()
	force_tkinter: bool = False
	
	page = skse_downloader.Scrape.load_page()
	data = generate_links(page)
	
	if using_platform() == PlatformType.PLATFORM_LINUX:
		from skse_downloader.TUI.Window import WindowTUI
		win = WindowTUI()
		win.render()
	elif (using_platform() == PlatformType.PLATFORM_LINUX or using_platform() == PlatformType.PLATFORM_WIN32) and force_tkinter:
		from skse_downloader.UI.Window import WindowTK
		win = WindowTK()
		win.run()
	else:
		from skse_downloader.PySide import Window
		Window.run(config=cfg, data=data)
