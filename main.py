from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit
import sys
from apihelp import predict_nomination



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание текстового поля
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 20, 560, 200)

        # Создание кнопки "Справка"
        self.help_button = QPushButton("Справка", self)
        self.help_button.setGeometry(20, 230, 80, 30)
        self.help_button.clicked.connect(self.show_help)

        # Создание кнопки "Отправить"
        self.send_button = QPushButton("Отправить", self)
        self.send_button.setGeometry(500, 230, 80, 30)
        self.send_button.clicked.connect(self.send_text)

        # Создание текстового поля для вывода
        self.output_label = QLabel(self)
        self.output_label.setGeometry(20, 270, 700, 80)

        # Создание текстового поля для вывода моего ФИО
        self.output_label1 = QLabel(self)
        self.output_label1.setGeometry(450, 300, 300, 180)
        self.output_label1.setText('Десанский Артём 20П-1')
    def show_help(self):
        # Обработчик нажатия кнопки "Справка"
        help_text = "В данным момент, в приложении нет возможности ничего, кроме отправки текста. \n" \
                    "Затем текст распределится на какую номинацию он достоин.\n"\
                    "1. Вы можете записать текст в поле ввода\n" \
                    "2. Вы можете отправить текст из поля ввода на генерацию прогноза\n" \
                    "3. Ну и вы можете вызвать справку, которую и так вызвали)))"
        self.output_label.setText(help_text)

    def send_text(self):
        # Обработчик нажатия кнопки "Отправить"
        text = self.text_edit.toPlainText()
        text1 = predict_nomination(text)
        self.output_label.setText(f"Модель SGD вывела такой прогной: {text1}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 600, 420)
    window.show()
    sys.exit(app.exec())