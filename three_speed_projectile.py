from projectile_motion import *
from matplotlib.pyplot import legend

if __name__ == '__main__':
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)

    plt.legend(['20', '40', '60'])
    plt.show()
