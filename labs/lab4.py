2 ЗАДАНИЕ

import time
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QComboBox, QMessageBox)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtGui


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)
        layout.addWidget(self.canvas)
        plt.grid(True)
        self.setCentralWidget(cental_widget)

        self.plot_button = QPushButton('Нарисовать график')
        self.plot_button.clicked.connect(self.plot_data)

        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('-15')
        self.range_end_input = QLineEdit('10')

        self.add_function_button = QPushButton('Добавить функцию в список')
        self.function_label = QLabel("Введите функцию:")
        self.function_input = QLineEdit('')
        self.function_widget = QComboBox()
        self.function_widget.addItems(['x**2+x**3+1', '5*x-5', 'x**2+3'])
        self.add_function_button.clicked.connect(self.add_function)

        self.point_amount = QLabel('Количество точек на графике:')
        self.point_input = QLineEdit('50')

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.error_message = QMessageBox()
        self.error_message.setText("Неверная функция")
        self.error_message.setWindowTitle('Ошибка')
        self.error_message.setIcon(QMessageBox.Critical)

        self.error_message2 = QMessageBox()
        self.error_message2.setText("На данном диапазоне f(c) != 0")
        self.error_message2.setWindowTitle('Ошибка')
        self.error_message2.setIcon(QMessageBox.Critical)

        self.bisection_button = QPushButton('Метод половинного деления')
        self.bisection_button.clicked.connect(self.bisection)

        self.bisection_label = QLabel("Полученный диапазон:")
        self.bisection_range_start_current = QLineEdit('-15')
        self.bisection_range_end_current = QLineEdit('10')
        self.bisection_range_start_current.setEnabled(False)
        self.bisection_range_end_current.setEnabled(False)

        self.add_range_button = QPushButton('Изменить диапазон')
        self.add_range_button.clicked.connect(self.change_range)
        layout.addWidget(self.function_widget)
        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.range_end_input)
        layout.addWidget(self.add_range_button)
        layout.addWidget(self.bisection_label)
        layout.addWidget(self.bisection_range_start_current)
        layout.addWidget(self.bisection_range_end_current)
        layout.addWidget(self.bisection_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.add_function_button)
    def vectors(self):
        expression = self.function_widget.currentText()

        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
            points = int(self.point_input.text())
        except ValueError:
            range_start = 0
            range_end = 1
            points = 50

        functions = {}
        try:
            exec(f'def f(x): return {expression}', functions)
            function = functions['f']
            x = np.linspace(range_start, range_end, points)
            y = [function(value) for value in x]
            return x, y

        except NameError:
            self.error_message.show()
            return 0
        except SyntaxError:
            self.error_message.show()
            return 0

    def plot_data(self):
        if self.vectors() != 0:
            x, y = self.vectors()
            axes = plt.subplot()
            axes.plot(x, y)
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')

            self.centralWidget().layout().itemAt(0).widget().draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        plt.grid(True)
        self.canvas.draw()

    def add_function(self):
        text_x = self.function_input.text()
        self.function_widget.addItems([text_x])

    def bisection(self):
        a, b = float(self.bisection_range_start_current.text()), float(self.bisection_range_end_current.text())
        EPS = 10**-3
        expression = self.function_widget.currentText()
        functions = {}
        exec(f'def ff(x): return {expression}', functions)
        f = functions['ff']
        c = (a + b) / 2

        while abs(f(c)) >= EPS:
            if f(c) == 0:
                self.bisection_range_start_current.setText(str(a))
                self.bisection_range_end_current.setText(str(b))
            plt.scatter(c, f(c))
            self.canvas.draw()

            if f(c) < 0:
                if f(b) > 0:
                    a = c
                elif f(a) > 0:
                    b = c
            elif f(c) > 0:
                if f(b) < 0:
                    a = c
                elif f(a) < 0:
                    b = c
                    
            x = np.linspace(a, b, 50)
            y = [f(value) for value in x]
            plt.plot(x, y)
            self.bisection_range_start_current.setText(str(a))
            self.bisection_range_end_current.setText(str(b))
            a, b = float(self.bisection_range_start_current.text()), float(self.bisection_range_end_current.text())
            c = (a + b) / 2
    def change_range(self):
        self.bisection_range_start_current.setText(str(self.range_start_input.text()))
        self.bisection_range_end_current.setText(str(self.range_end_input.text()))


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()










1 ЗАДАНИЕ
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("График")
        self.setGeometry(100, 100, 700, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.label_x = QLabel("X:")
        layout.addWidget(self.label_x)
        self.entry_x = QLineEdit()
        layout.addWidget(self.entry_x)

        self.label_y = QLabel("Y:")
        layout.addWidget(self.label_y)
        self.entry_y = QLineEdit()
        layout.addWidget(self.entry_y)

        self.button_add = QPushButton("Добавить точку")
        self.button_add.clicked.connect(self.add_point_in_figure)
        layout.addWidget(self.button_add)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.x_line1 = [-1, 0, 1, 0, -2]
        self.y_line1 = [-1, -2.5, -4, -1, 1]
        self.x_line2 = [-2, 2, 0, 2, -1, -1]
        self.y_line2 = [1, 0, 2, 5, 5, 3]
        self.x_line3 = [4, 3, 5, 7, 6]
        self.y_line3 = [-3, -4, -5, -3, -1]
        self.x_line4 = [4, 3, 2, 4, 3, 2]
        self.y_line4 = [1, 4, 1, 0, -2, -1]

        self.ax.plot(self.x_line1, self.y_line1, linestyle='-')
        self.ax.plot(self.x_line2, self.y_line2, linestyle='-')
        self.ax.plot(self.x_line3, self.y_line3, linestyle='-')
        self.ax.plot(self.x_line4, self.y_line4, linestyle='-')

        center = (-1, 1)
        radius = 2
        start_angle = np.radians(90)
        end_angle = np.radians(270)
        angles = np.linspace(start_angle, end_angle, 100)
        self.x_circle1 = center[0] + radius * np.cos(angles)
        self.y_circle1 = center[1] + radius * np.sin(angles)
        self.ax.plot(self.x_circle1, self.y_circle1, linestyle='-')

        center = (4, -1)
        radius = 2
        start_angle = np.radians(180)
        end_angle = np.radians(270)
        angles = np.linspace(start_angle, end_angle, 100)
        self.x_circle2 = center[0] + radius * np.cos(angles)
        self.y_circle2 = center[1] + radius * np.sin(angles)
        self.ax.plot(self.x_circle2, self.y_circle2, linestyle='-')

        center = (4, -1)
        radius = 2
        start_angle = np.radians(0)
        end_angle = np.radians(90)
        angles = np.linspace(start_angle, end_angle, 100)
        self.x_circle3 = center[0] + radius * np.cos(angles)
        self.y_circle3 = center[1] + radius * np.sin(angles)
        self.ax.plot(self.x_circle3, self.y_circle3, linestyle='-')

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('График')
        self.ax.grid(True)

        self.current_point = None

    def add_point(self, x, y):
        self.result_label.clear()

        if self.current_point:
            self.current_point.remove()

        self.current_point, = self.ax.plot(x, y, 'ro')

        self.canvas.draw()

    def add_point_in_figure(self):
        x_input = self.entry_x.text()
        y_input = self.entry_y.text()

        try:
            x = float(x_input)
            y = float(y_input)
        except ValueError:
            self.result_label.setText("Введите корректные числа для координат X и Y")
            return

        self.add_point(x, y)

        if self.check_point_in_figure(x, y):
            self.result_label.setText("Точка попала в фигуру")
        else:
            self.result_label.setText("Точка вне фигуры")

    def check_point_in_figure(self, x, y):
        one = (y <= 3 * x - 5) and (y <= -3 * x + 13) and (y >= -0.5 * x + 2)
        two = ((x - 4) ** 2 + (y + 1) ** 2 <= 4) and (y <= 2 * x - 8) and (x >= 3)
        three = (y <= x - 7) and (y >= x - 10) and (y <= -2 * x + 11) and (y >= -2 * x - 5)
        four = (x >= 4) and (x <= 5) and ((x - 4) ** 2 + (y + 1) ** 2 <= 4)
        five = (y <= -x + 1) and ((x - 4) ** 2 + (y + 1) ** 2 <= 4)
        six = (y <= 5) and (y >= 1) and (y >= 1.5 * x + 2) and (x >= -1) and (y <= 5)
        seven = (y <= 0.5 * x + 2) and (y <= -x + 2) and (y >= -0.25 * x + 0.5)
        eight = (y <= -x - 1) and (y <= -3 * x - 1) and (y >= -1.5 * x - 2.5) and (y <= 1.5)
        nine = ((x + 1) ** 2 + (y - 1) ** 2 <= 4) and (y >= 1) and (x <= -1)
        ten = ((x + 1) ** 2 + (y - 1) ** 2 <= 4) and (y <= -x - 1) and (y <= 1)

        figure1 = one or two or three or four or five
        figure2 = six or seven or eight or nine or ten

        if figure1 or figure2:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec_())

2 ЗАДАНИЕ
from PyQt5.QtWidgets import (
 QApplication,
 QLabel,
 QLineEdit,
 QMainWindow,
 QPushButton,
 QVBoxLayout,
 QWidget,
 QSpinBox,
 QMessageBox,
 QFileDialog,
 QComboBox
)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Назначим заголовок окна
        self.setWindowTitle("График")

        # Создание виджетов
        self.canvas = FigureCanvas(plt.figure()) # Создание полотна Matplotlib

        # Создание центрального виджета
        central_widget = QWidget()
        layout = QVBoxLayout() # макет, на который будут добавляться виджеты
        central_widget.setLayout(layout) # добавление макета на центральный виджет

        # Добавление виджетов на макет
        layout.addWidget(self.canvas)

        # Установка центрального виджета
        self.setCentralWidget(central_widget)

        self.plot_button = QPushButton("Нарисовать график")
        self.plot_button.clicked.connect(self.plot_data)

        layout.addWidget(self.plot_button)

        self.range_label = QLabel("Диапазон:")
        self.range_start_input = QLineEdit('-1')
        self.range_end_input = QLineEdit('1')

        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.range_end_input)

        self.function_label = QLabel("Функция:")
        self.function_input = QLineEdit('x**3')

        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)



    def plot_data(self):
        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
        except ValueError:
            range_start = 0
            range_end = 1

        # Получаем количество точек из QSpinBox
        num_points = 100

        x = np.linspace(range_start, range_end, num_points)

        try:
            expression = self.function_input.text()
        except ValueError:
            expression = "x**3"

        try:
            functions = {}  # определим словарь функций
            exec(f"def f(x): return {expression}", functions)
            function = functions["f"]

            x = np.linspace(range_start, range_end, num_points)
            y = [function(value) for value in x]

            plt.title('График функции ' + expression)

            plt.plot(x, y)
            plt.grid(True)

            plt.xlabel('x')
            plt.ylabel('y')
            # Добавляем функцию в виджет списка, если она не была добавлена ранее
            # Обработка ошибки ввода неверной функции
            self.centralWidget().layout().itemAt(0).widget().draw()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при построении графика: {e}")

# Создать приложение QApplication
app = QApplication([])
# Создать окно приложения
main_window = MainWindow()
main_window.show()
# Запустить приложение
app.exec_()

3 ЗАДАНИЕ
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("График и таблица")
        self.setGeometry(100, 100, 700, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.button_plot = QPushButton("Построить")
        layout.addWidget(self.button_plot)
        self.button_plot.clicked.connect(self.plot_graph)

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('График')
        self.ax.grid(True)

        self.current_point = None

        # Создание таблицы
        self.table = QTableWidget()
        self.table.setRowCount(4)  # Установка количества строк
        self.table.setColumnCount(6)  # Установка количества столбцов
        self.table = QTableWidget()
        self.table.setRowCount(4)  # Установка количества строк
        self.table.setColumnCount(9)  # Установка количества столбцов

        for i in range(4):
            for j in range(9):
                item = QTableWidgetItem(str(i * j))
                item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)  # установка флага для редактирования
                self.table.setItem(i, j, item)

        # Заполнение и установка редактируемости таблицы
        for i in range(4):
            for j in range(6):
                item = QTableWidgetItem(str(i * j))
                item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable) # установка флага для редактирования
                self.table.setItem(i, j, item)

        layout.addWidget(self.table)

        # Соединение изменений в таблице с функцией обновления графика
        self.table.itemChanged.connect(self.update_graph)

    def plot_graph(self):
        x_val = float(self.entry_x.text())
        y_val = float(self.entry_y.text())
        if self.current_point:
            self.current_point.remove()
        self.current_point, = self.ax.plot(x_val, y_val, 'ro')
        self.canvas.draw()

    def update_graph(self, item):
        row = item.row()
        col = item.column()
        val = float(item.text())
        if col == 1 or col == 2 or col == 3 or col == 4 or col == 5:
            x_val = float(self.table.item(row, 1).text())
            y_val = float(self.table.item(row, 2).text())
            length = float(self.table.item(row, 3).text())
            width = float(self.table.item(row, 4).text())
            angle = float(self.table.item(row, 5).text())

            # Обновление прямоугольника на графике
            rect = plt.Rectangle((x_val, y_val), length, width, angle=angle, edgecolor='blue', facecolor='none')
            self.ax.add_patch(rect)
            self.canvas.draw()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec_())
