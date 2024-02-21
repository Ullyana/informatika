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
