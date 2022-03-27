import  sys
import  first
from PyQt5.QtWidgets import  QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow,first.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        # ui = first.Ui_MainWindow()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/mice2.jpg'))
    # mainWindow = QMainWindow()
    ui = MainWindow()
    # 主窗口添加控件
    # ui.setupUi(mainWindow)
    ui.show()
    sys.exit(app.exec_())