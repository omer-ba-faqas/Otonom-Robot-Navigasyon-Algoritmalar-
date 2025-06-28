import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import heapq

# Grid boyutu ve engeller
rows, cols = 25, 50
grid = np.zeros((rows, cols))

grid[0:20, 10] = 1
grid[5:25, 30] = 1
grid[8, 15:20] = 1
grid[15, 35:40] = 1

start = (2, 2)
goal = (22, 48)


# Manhattan mesafesi
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algoritması
def astar(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()
    frames = []

    path = []

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        # Frame: RGB (beyaz zemin)
        frame = np.ones((*grid.shape, 3))

        # Engeller: siyah
        frame[grid == 1] = [0, 0, 0]

        # Ziyaret edilenler: mavi
        for v in visited:
            if grid[v] != 1 and v != start and v != goal:
                frame[v] = [0.2, 0.6, 1.0]

        # Başlangıç: yeşil
        frame[start] = [0, 1, 0]

        # Hedef: kırmızı
        frame[goal] = [1, 0, 0]

        frames.append(frame)

        if current == goal:
            # Path oluştur
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor] == 1:
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, tentative_g, neighbor))
                    came_from[neighbor] = current

    # Son frame'e en kısa yolu sarı çiz
    if path:
        final_frame = frames[-1].copy()
        for p in path:
            if grid[p] != 1 and p != start and p != goal:
                final_frame[p] = [1.0, 1.0, 0]  # Sarı
        frames.append(final_frame)

    return path, frames

# A* çalıştır
path, frames = astar(grid, start, goal)

# Animasyon
fig, ax = plt.subplots()
im = ax.imshow(frames[0], interpolation='none')
ax.set_title("A* Pathfinding Visualization")

def update(i):
    im.set_data(frames[i])
    return [im]

ani = animation.FuncAnimation(
    fig, update, frames=len(frames), interval=10, blit=True, repeat=False
)

plt.show()
