@echo off
del resource.py
..\venv\Lib\site-packages\PySide6\rcc.exe -g python  -o resource.py res/res.qrc
