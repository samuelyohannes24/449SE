import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QCheckBox, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.setWindowTitle("Custom SOS GUI")
        self.setGeometry(200, 150, 450, 350)

        # Create central widget and layout
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout()

        # Add text
        self.title_label = QLabel("SOS Game GUI Example", self)
        self.layout.addWidget(self.title_label)

        # Add checkbox
        self.game_checkbox = QCheckBox("Activate Game Features", self)
        self.layout.addWidget(self.game_checkbox)

        # Add radio buttons
        self.radio_layout = QHBoxLayout()
        self.option_one = QRadioButton("Player Mode", self)
        self.option_two = QRadioButton("Spectator Mode", self)
        self.radio_layout.addWidget(self.option_one)
        self.radio_layout.addWidget(self.option_two)
        self.layout.addLayout(self.radio_layout)

        # Set the layout to the widget
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.blue, 3, Qt.DashLine)
        painter.setPen(pen)

        # Draw a custom diagonal line
        painter.drawLine(60, 220, 380, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CustomWindow()
    main_window.show()
    sys.exit(app.exec_())
