import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PyQt5.QtGui import QKeySequence

class SimpleTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle("Simple Text Editor")
        self.init_shortcuts()
        self.resize(800, 600)

    def init_shortcuts(self):
        self.textEdit.addAction(QKeySequence("Ctrl+N"), self.new_file)
        self.textEdit.addAction(QKeySequence("Ctrl+O"), self.open_file)
        self.textEdit.addAction(QKeySequence("Ctrl+S"), self.save_file)
        self.textEdit.addAction(QKeySequence("Ctrl+Q"), self.close)
        self.textEdit.addAction(QKeySequence("Ctrl+Z"), self.textEdit.undo)
        self.textEdit.addAction(QKeySequence("Ctrl+Shift+Z"), self.textEdit.redo)
        self.textEdit.addAction(QKeySequence("Ctrl+X"), self.textEdit.cut)
        self.textEdit.addAction(QKeySequence("Ctrl+C"), self.textEdit.copy)
        self.textEdit.addAction(QKeySequence("Ctrl+V"), self.textEdit.paste)

    def new_file(self):
        self.textEdit.clear()

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.textEdit.setPlainText(file.read())

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.textEdit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = SimpleTextEditor()
    editor.show()
    sys.exit(app.exec_())
