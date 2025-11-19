import random
import matplotlib.pyplot as plt
import time

def monte_carlopi(num_points):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for i in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle+=1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    pi_estimate = 4*(inside_circle/num_points)
        
    plt.figure(figsize=(5,5))
    plt.scatter(x_inside, y_inside, color='green', s=1, label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
    plt.legend()
    plt.title(f"Monte Carlo π Estimation\nN={num_points}, π≈{pi_estimate:.5f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()
monte_carlopi(1000)