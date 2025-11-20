# check_gui.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow  # 作成したファイルを読み込み

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # デザインを適用
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())