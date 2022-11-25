# @Time : 2022/11/23 15:35
# @Author : WZG
# --coding:utf-8--

import numpy as np
import matplotlib.pyplot as plt
plot_x = np.linspace(-1., 6., 141)

plot_y = (plot_x-2.5)**2 - 1.
plt.plot(plot_x, plot_y)
print(plt.show())

epsilon = 1e-8
eta = 0.1


def J(theta):
    return (theta - 2.5) ** 2 - 1.


def dJ(theta):
    return 2 * (theta - 2.5)


theta = 0.0
while True:
    gradient = dJ(theta)
    last_theta = theta
    theta = theta - eta * gradient

    if (abs(J(theta) - J(last_theta)) < epsilon):
        break

print(theta)
print(J(theta))

theta = 0.0
theta_history = [theta]
while True:
    gradient = dJ(theta)
    last_theta = theta
    theta = theta - eta * gradient
    theta_history.append(theta)

    if (abs(J(theta) - J(last_theta)) < epsilon):
        break

plt.plot(plot_x, J(plot_x))
plt.plot(np.array(theta_history), J(np.array(theta_history)), color="r", marker='+')
print(plt.show())

theta_history = []


def gradient_descent(initial_theta, eta, epsilon=1e-8):
    theta = initial_theta
    theta_history.append(initial_theta)

    while True:
        gradient = dJ(theta)
        last_theta = theta
        theta = theta - eta * gradient
        theta_history.append(theta)

        if (abs(J(theta) - J(last_theta)) < epsilon):
            break


def plot_theta_history():
    plt.plot(plot_x, J(plot_x))
    plt.plot(np.array(theta_history), J(np.array(theta_history)), color="r", marker='+')
    print(plt.show())


eta = 0.01
theta_history = []
gradient_descent(0, eta)
plot_theta_history()

'''
def J(theta):
    try:
        return (theta-2.5)**2 - 1.
    except:
        return float('inf')
def gradient_descent(initial_theta, eta, n_iters = 1e4, epsilon=1e-8):
    
    theta = initial_theta
    i_iter = 0
    theta_history.append(initial_theta)

    while i_iter < n_iters:
        gradient = dJ(theta)
        last_theta = theta
        theta = theta - eta * gradient
        theta_history.append(theta)
    
        if(abs(J(theta) - J(last_theta)) < epsilon):
            break
            
        i_iter += 1
        
    return
eta = 1.1
theta_history = []
gradient_descent(0, eta)'''