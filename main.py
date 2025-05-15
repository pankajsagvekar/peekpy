from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import sys

def main():
    app = QApplication(sys.argv)
    window = loadUi("main.ui")

    def upload_image():
        file_name, _ = QFileDialog.getOpenFileName(window, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            pixmap = QPixmap(file_name)
            
            # Scale while keeping aspect ratio
            scaled_pixmap = pixmap.scaled(
                window.imageLabel.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            window.imageLabel.setPixmap(scaled_pixmap)

    # image resizes when window resizes
    def resizeEvent(event):
        if window.imageLabel.pixmap():
            pixmap = window.imageLabel.pixmap()
            scaled_pixmap = pixmap.scaled(
                window.imageLabel.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            window.imageLabel.setPixmap(scaled_pixmap)

    
    
    window.pushButton.clicked.connect(upload_image)
    window.setWindowTitle("Peekpy")
    window.setWindowIcon(QIcon("assets/icon.png"))
    window.resizeEvent = resizeEvent

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
