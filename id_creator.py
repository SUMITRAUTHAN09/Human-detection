import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class IDCreatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ID Creator')
        self.setGeometry(100, 100, 300, 200)

        # Create widgets
        self.name_label = QLabel('Enter Name:')
        self.name_line_edit = QLineEdit()
        self.submit_button = QPushButton('Submit')

        # Connect widgets to methods
        self.submit_button.clicked.connect(self.generate_id)

        # Create a layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_line_edit)
        layout.addWidget(self.submit_button)

        # Create a container widget and set the layout
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window
        self.setCentralWidget(container)

    def generate_id(self):
        name = self.name_line_edit.text()
        id = 'ID: ' + name.replace(' ', '').lower()
        self.name_line_edit.clear()
        self.show_id(id)

    def show_id(self, id):
        dialog = QMessageBox()
        dialog.setWindowTitle('Generated ID')
        dialog.setText(id)
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IDCreatorApp()
    ex.show()
    sys.exit(app.exec_())