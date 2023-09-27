import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.tasks = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Aplikasi To-Do List')
        self.setGeometry(100, 100, 400, 300)

        self.task_list = QListWidget(self)

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Tambahkan tugas baru')
        
        self.add_button = QPushButton('Tambahkan', self)
        self.add_button.clicked.connect(self.add_task)

        self.remove_button = QPushButton('Hapus', self)
        self.remove_button.clicked.connect(self.remove_task)

        layout = QVBoxLayout()
        layout.addWidget(self.task_list)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)
        input_layout.addWidget(self.remove_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.clear()

    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.tasks.remove(item.text())
            self.task_list.takeItem(self.task_list.row(item))

def main():
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
