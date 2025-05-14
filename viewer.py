from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PeekPy")
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon("assets/icon.png"))
        
        self.init_ui()

    def init_ui(self):
        label = QLabel("Image Viewer")
        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)