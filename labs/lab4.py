import matplotlib.pyplot as plt
import numpy as np

def lab4():
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    one = (Y <= 3 * X - 5) & (Y <= -3 * X + 13) & (Y >= -0.5 * X + 2)
    two = ((X - 4) ** 2 + (Y + 1) ** 2 <= 4) & (Y <= 2 * X - 8) & (X >= 3)
    three = (Y <= X - 7) & (Y >= X - 10) & (Y <= -2 * X + 11) & (Y >= -2 * X - 5)
    four = (X >= 4) & (X <= 5) & ((X - 4) ** 2 + (Y + 1) ** 2 <= 4)
    five = (Y <= -X + 1) & ((X - 4) ** 2 + (Y + 1) ** 2 <= 4)
    six = (Y <= 5) & (Y >= 1) & (Y >= 1.5 * X + 2) & (X >= -1) & (Y <= 5)
    seven = (Y <= 0.5 * X + 2) & (Y <= -X + 2) & (Y >= -0.25 * X + 0.5)
    eight = (Y <= -X - 1) & (Y <= -3 * X - 1) & (Y >= -1.5 * X - 2.5) & (Y <= 1.5)
    nine = ((X + 1) ** 2 + (Y - 1) ** 2 <= 4) & (Y >= 1) & (X <= -1)
    ten = ((X + 1) ** 2 + (Y - 1) ** 2 <= 4) & (Y <= -X - 1) & (Y <= 1)

    figure1 = one | two | three | four | five
    figure2 = six | seven | eight | nine | ten

    plt.figure()
    plt.contourf(X, Y, figure1, colors='green', alpha=0.5)
    plt.contourf(X, Y, figure2, colors='blue', alpha=0.5)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Фигуры')
    plt.grid(True)
    plt.show()

lab4()


НЕ ХВАТАЕТ ФУНКЦИИ ОПРЕДЕЛЕНИЯ ВХОЖДЕНИЯ ТОЧКИ В ОБЛАСТЬ
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("График")
        self.setGeometry(100, 100, 800, 600)

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
        self.button_add.clicked.connect(self.add_point)
        layout.addWidget(self.button_add)

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

        # Задаем центр и радиус окружности
        center = (-1, 1)
        radius = 2
        # Задаем угловой диапазон для отображения дуги (например, от 45 градусов до 315 градусов)
        start_angle = np.radians(90)
        end_angle = np.radians(270)
        # Создаем массив углов в заданном диапазоне
        angles = np.linspace(start_angle, end_angle, 100)
        # Вычисляем координаты точек окружности в заданном диапазоне углов
        self.x_circle1 = center[0] + radius * np.cos(angles)
        self.y_circle1 = center[1] + radius * np.sin(angles)
        # Строим график
        plt.figure(figsize=(6, 6))  # Размер графика
        # Строим дугу окружности
        self.ax.plot(self.x_circle1, self.y_circle1, linestyle='-')

        # Задаем центр и радиус окружности
        center = (4, -1)
        radius = 2
        # Задаем угловой диапазон для отображения дуги (например, от 45 градусов до 315 градусов)
        start_angle = np.radians(180)
        end_angle = np.radians(270)
        # Создаем массив углов в заданном диапазоне
        angles = np.linspace(start_angle, end_angle, 100)
        # Вычисляем координаты точек окружности в заданном диапазоне углов
        self.x_circle2 = center[0] + radius * np.cos(angles)
        self.y_circle2 = center[1] + radius * np.sin(angles)
        # Строим дугу окружности
        self.ax.plot(self.x_circle2, self.y_circle2, linestyle='-')

        # Задаем центр и радиус окружности
        center = (4, -1)
        radius = 2
        # Задаем угловой диапазон для отображения дуги (например, от 45 градусов до 315 градусов)
        start_angle = np.radians(0)
        end_angle = np.radians(90)
        # Создаем массив углов в заданном диапазоне
        angles = np.linspace(start_angle, end_angle, 100)
        # Вычисляем координаты точек окружности в заданном диапазоне углов
        self.x_circle3 = center[0] + radius * np.cos(angles)
        self.y_circle3 = center[1] + radius * np.sin(angles)
        # Строим дугу окружности
        self.ax.plot(self.x_circle3, self.y_circle3, linestyle='-')

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('График')

    def add_point(self):
        try:
            x = float(self.entry_x.text())
            y = float(self.entry_y.text())
            self.ax.plot(x, y, marker='o', markersize=8, color='red')
            self.canvas.draw()
        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec_())
