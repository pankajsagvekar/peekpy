from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PeekPy")
window.setGeometry(200, 200, 300, 200)

label = QLabel("Image Viewer", window)
label.setAlignment(Qt.AlignCenter)

window.show()

app.exec()