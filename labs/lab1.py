

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
        self.ax.grid(True)  # Добавляем сетку на график

        self.current_point = None  # Переменная для х

    def add_point(self, x, y):
        # Удаляем предыдущую точку, если она существует
        if self.current_point:
            self.current_point.remove()

        # Добавляем новую точку на график
        self.current_point, = self.ax.plot(x, y, 'ro')  # 'ro' означает красный цвет и точечный стиль

        # Обновляем график
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
        # Добавляем точку на график
        self.add_point(x, y)

        # Очищаем результат
        self.result_label.clear()

    def check_point_in_figure(x, y):
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


