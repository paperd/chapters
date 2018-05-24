import matplotlib.pyplot as plt, numpy as np, random as rand
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm

if __name__ == '__main__':
    n = 200
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), num=n)
    y = norm.pdf(x)
    dic = {}
    for i, row in enumerate(y):
        dic[x[i]] = [np.random.uniform(0, row) for _ in range(n)]
    xs, ys = [], []
    for key, vals in dic.items():
        for y in vals:
            xs.append(key)
            ys.append(y)
    fig1 = plt.figure()
    ax = Axes3D(fig1)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.scatter(xs, ys, zs=0, c=xs, cmap='rainbow')
    fig2 = plt.figure()
    ax = Axes3D(fig2)
    r = 2
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:0.5*pi:180j, 0.0:2.0*pi:720j]
    X = r*sin(phi)*cos(theta)
    Y = r*sin(phi)*sin(theta)
    Z = 2 * cos(phi)
    ax.plot_surface(X, Y, Z, cmap='rainbow')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
