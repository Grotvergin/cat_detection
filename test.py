from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView(self)
        self.browser.setUrl(QUrl.fromLocalFile(r"E:\Projects\cats\ESP32CamClassificationTfjs\data\index.htm"))
        self.setWindowTitle("Детектирование котов!")
        self.setWindowIcon(QIcon("cat.png"))
        self.setCentralWidget(self.browser)
        self.showMaximized()


app = QApplication([])
window = MainWindow()
app.exec_()
