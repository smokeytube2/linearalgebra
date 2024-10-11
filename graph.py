import numpy as np
import math
from vmath import Vmath as v

class Graaf:
    def __init__(self, ax):
        self.ax = ax
        self.x_vals = np.arange(-6, 6)
        self.y_vals = np.arange(-6, 6)
        self.z_vals = np.arange(-6, 6)
        self.X, self.Y = np.meshgrid(self.x_vals, self.y_vals)
        _, self.Z = np.meshgrid(self.x_vals, self.z_vals)

    def punkt(self, x, y, z):
        self.ax.scatter(x, y, z, color='r', s=100)

    def vektor(self, x, y, z, u=0, v=0, w=0):
        self.ax.quiver(u, v, w, x, y, z, color='b', arrow_length_ratio=0.1)
    
    def tasand2(self, A, B, C, D):
        Z = np.zeros_like(self.X)
        if C != 0:
            # Regular plane case: Ax + By + Cz + D = 0
            Z = (-A * self.X - B * self.Y - D) / C
            self.plane = self.ax.plot_surface(self.X, self.Y, Z, alpha=0.7)
        else:
            if A == 0 and B == 0:
                return
            elif A == 0:
                Y = (-A * self.X - C * self.Z - D) / B
                self.plane = self.ax.plot_surface(self.X, Y, self.Z, alpha=0.7)
            elif B == 0:
                X = (-B * self.Y - C * self.Z - D) / A
                self.plane = self.ax.plot_surface(X, self.Y, self.Y, alpha=0.7)
                
    def tasand(self, P0, d1, d2):
        # Parametric equation of the plane: P(u, v) = P0 + u*d1 + v*d2
        X = P0[0] + self.X * d1[0] + self.Y * d2[0]
        Y = P0[1] + self.X * d1[1] + self.Y * d2[1]
        Z = P0[2] + self.X * d1[2] + self.Y * d2[2]
        
        # Plot the plane
        self.ax.plot_surface(X, Y, Z, alpha=0.7)