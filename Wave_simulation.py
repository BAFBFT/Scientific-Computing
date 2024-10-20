import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Set up the domain, grid, and wave-equation parameters
Lx, Ly = 10, 10
Nx, Ny = 200, 200  
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1) # spatial discretisation
dt = 0.01  # time step
T = 1
Nt = int(T / dt)
c = 2  


# Courant-Friedrichs-Lewy (CFL) stability condition check 
CFL_1 = c * (dt / dx)
CFL_2 = c * (dt / dy)
assert CFL_1 <= 1 and CFL_2 <= 1, "Stability condition violated"


# Arrays to store wave states
u = np.zeros((Nx, Ny))
u_prev = np.zeros((Nx, Ny))
u_next = np.zeros((Nx, Ny))


# Initial condition: small perturbation at the center
x_center, y_center = Lx / 2, Ly / 2
drop_radius = 0.1

for i in range(Nx):
    for j in range(Ny):
        distance_to_drop = np.sqrt((i * dx - x_center)**2 + (j * dy - y_center)**2)
        if distance_to_drop < drop_radius:
            u_prev[i, j] = -0.3  # Initial displacement

# Set up the figure and axis for heatmap visualization
fig, ax = plt.subplots(figsize=(6, 6))

# Create the heatmap using imshow
heatmap = ax.imshow(u, extent=[0, Lx, 0, Ly], origin='lower', cmap='plasma', vmin=-0.2, vmax=0.2)


# Add a colorbar to show the displacement values
cbar = plt.colorbar(heatmap)
cbar.set_label('Displacement')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Wave Propagation (Heatmap)')


# Animation update function
def update_wave(frame):
    global u, u_prev, u_next

    N = int(Nx / 2)  # Iteratively solve for one quadrant

    # Solve for the entire grid, not just one quadrant
    for i in range(1, N):
        for j in range(1, N):
            u_next[i, j] = (2 * u[i, j] - u_prev[i, j] +
                            (c * dt / dx) ** 2 * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j]) +
                            (c * dt / dy) ** 2 * (u[i, j + 1] - 2 * u[i, j] + u[i, j - 1]))

    # Reflecting solution to other quadrants, to reduce computations needed
    u_next[N:, :] = np.flipud(u_next[:N, :])
    u_next[:, N:] = np.fliplr(u_next[:, :N])
    u_next[N:, N:] = np.flipud(np.fliplr(u_next[:N, :N]))

    # Update the heatmap data without recreating the plot
    heatmap.set_data(u_next)  # Set the new data for the heatmap

    # Update wave state for the next iteration
    u_prev[:, :] = u[:, :]
    u[:, :] = u_next[:, :]

    return [heatmap] 


# Create the animation with blitting enabled
ani = animation.FuncAnimation(fig, update_wave, frames=Nt, interval=20, blit=True)

plt.show()


