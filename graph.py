import numpy as np

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
            if A != 0:
                X = (-B * self.X - D) / A  # Solve for x if A != 0
                self.plane = self.ax.plot_surface(X, self.Y, self.X, alpha=0.7)
            elif B != 0:
                Y = (-A * self.Y - D) / B  # Solve for y if B != 0
                self.plane = self.ax.plot_surface(self.X, Y, self.Y, alpha=0.7)
    
    def tasand(self, A, B, C, D):
        Y = (-A * self.X - C * self.Z - D) / B
        self.plane = self.ax.plot_surface(self.X, Y, self.Z, alpha=0.7)