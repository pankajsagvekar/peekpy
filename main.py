from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import sys

def main():
    app = QApplication(sys.argv)
    window = loadUi("main.ui")

    original_pixmap = None
    zoom_level = 1.0

    def upload_image():
        nonlocal original_pixmap, zoom_level
        file_name, _ = QFileDialog.getOpenFileName(
            window, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_name:
            original_pixmap = QPixmap(file_name)
            zoom_level = 1.0  # Reset zoom
            display_image()

    def display_image():
        if original_pixmap:
            label_size = window.imageLabel.size()
            scaled_width = int(label_size.width() * zoom_level)
            scaled_height = int(label_size.height() * zoom_level)

            scaled_pixmap = original_pixmap.scaled(
                scaled_width,
                scaled_height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            window.imageLabel.setPixmap(scaled_pixmap)
            window.imageLabel.setAlignment(Qt.AlignCenter)

    def zoom_in():
        nonlocal zoom_level
        zoom_level = min(zoom_level + 0.1, 5.0)  # prevent infinite zoom
        display_image()

    def zoom_out():
        nonlocal zoom_level
        zoom_level = max(0.1, zoom_level - 0.1)
        display_image()

    def resizeEvent(event):
        display_image()

    # Setup buttons and behavior
    window.pushButton.clicked.connect(upload_image)
    window.zoomInButton.clicked.connect(zoom_in)
    window.zoomOutButton.clicked.connect(zoom_out)

    window.setWindowTitle("Peekpy")
    window.setWindowIcon(QIcon("assets/icon.ico"))
    window.resizeEvent = resizeEvent

    # prevent QLabel from growing unbounded
    window.imageLabel.setScaledContents(False)
    window.imageLabel.setMinimumSize(1, 1)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
