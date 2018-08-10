import matplotlib.pyplot as plt

def create_graph():
    x_numbers = [1, 2, 3, 4, 5]
    y_numbers = [i**2 for i in x_numbers]
    plt.plot(x_numbers, y_numbers)
    plt.show()

if __name__ == '__main__':
    create_graph()
