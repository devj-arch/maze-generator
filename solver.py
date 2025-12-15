import pygame
import heapq
import json

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def load_maze_from_json(path):
    with open(path, "r") as f:
        return json.load(f)

def find_positions(maze):
    start = None
    end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "X":
                end = (x, y)
    return start, end

def dijkstra_solve(maze, screen, cell_size, visit_delay=5, path_delay=10):
    rows = len(maze)
    cols = len(maze[0])

    start, end = find_positions(maze)
    if not start or not end:
        print("Start or end position missing.")
        return

    dist = { (x, y): float("inf") for y in range(rows) for x in range(cols) }
    dist[start] = 0

    parent = {}
    visited = set()

    pq = [(0, start)]

    while pq:
        pygame.event.pump()  # keeps the window responsive

        current_dist, current = heapq.heappop(pq)
        x, y = current

        if current in visited:
            continue
        visited.add(current)

        # Animate visited nodes in purple (128, 0, 128)
        draw_cell(screen, x, y, cell_size, (120, 81, 169))
        pygame.display.update()
        pygame.time.delay(visit_delay)

        if current == end:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < cols and 0 <= ny < rows:
                if maze[ny][nx] == "#":
                    continue

                new_dist = current_dist + 1

                if new_dist < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_dist
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (new_dist, (nx, ny)))

    # Path reconstruction
    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            print("No path found.")
            return
    path.append(start)
    path.reverse()

    # Animate shortest path in gold (255, 215, 0)
    for x, y in path:
        pygame.event.pump()
        draw_cell(screen, x, y, cell_size, (253, 208, 23))
        pygame.display.update()
        pygame.time.delay(path_delay)

def draw_cell(screen, x, y, size, color):
    r = pygame.Rect(x * size, y * size, size, size)
    pygame.draw.rect(screen, color, r)

def run_visual_dijkstra(maze_path, cell_size=20):
    pygame.init()

    maze = load_maze_from_json(maze_path)
    rows = len(maze)
    cols = len(maze[0])

    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))

    # Draw initial maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                color = (0, 255, 64)
            else:
                color = (0, 0, 0)
            draw_cell(screen, x, y, cell_size, color)

    pygame.display.update()

    dijkstra_solve(maze, screen, cell_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    run_visual_dijkstra("maze.json", cell_size=10)
