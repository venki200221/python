import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
# import tkinter as tk
from PIL import Image 


class MainWindow(QMainWindow):
    def __init__(self):
        # root = tk.Tk()
        # root.overrideredirect(True)
        # root.overrideredirect(False)
        # root.attributes('-fullscreen',True)
        # width= root.winfo_screenwidth()
        # height= root.winfo_screenheight()
        # #setting tkinter window size
        # root.geometry("%dx%d" % (width, height))
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        # root.mainloop()

app = QApplication(sys.argv)
QApplication.setApplicationName('Bigbuddy')
window = MainWindow()
app.exec_()