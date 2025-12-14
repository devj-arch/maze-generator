import pygame
import random
import json


def select_algorithm():
    print("\nSelect maze generation algorithm:\n")
    print("1. Depth-First Search (Recursive Backtracker)")
    print("2. Prim's Algorithm")

    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice == "1":
            return "dfs"
        elif choice == "2":
            return "prim"
        else:
            print("Invalid choice. Please enter 1 or 2.")


def generate_maze_dfs(width, height, screen, cell_size, colors, delay=5):
    maze = [["#" for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def draw_cell(x, y, value):
        rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colors[value], rect)
        pygame.display.update(rect)

    def carve(x, y):
        maze[y * 2 + 1][x * 2 + 1] = " "
        draw_cell(x * 2 + 1, y * 2 + 1, " ")

        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if maze[ny * 2 + 1][nx * 2 + 1] == "#":
                    maze[y * 2 + 1 + dy][x * 2 + 1 + dx] = " "
                    draw_cell(x * 2 + 1 + dx, y * 2 + 1 + dy, " ")
                    pygame.time.delay(delay)

                    # Allow pygame to refresh during recursion
                    pygame.event.pump()

                    carve(nx, ny)

    carve(0, 0)
    maze[1][0] = "S"
    maze[height * 2 - 1][width * 2] = "X"
    draw_cell(0, 1, "S")
    draw_cell(width * 2, height * 2 - 1, "X")
    return maze


def generate_maze_prim(width, height, screen, cell_size, colors, delay=5):
    # full grid of walls
    maze = [["#" for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]

    def draw_cell(x, y, value):
        rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colors[value], rect)
        pygame.display.update(rect)

    # frontier list of walls
    frontier = []

    # pick a random starting cell
    sx = random.randint(0, width - 1)
    sy = random.randint(0, height - 1)

    def add_frontier(cx, cy):
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                wx = cx * 2 + 1 + dx
                wy = cy * 2 + 1 + dy
                if maze[wy][wx] == "#":
                    frontier.append((cx, cy, dx, dy))

    # carve start cell
    maze[sy * 2 + 1][sx * 2 + 1] = " "
    draw_cell(sx * 2 + 1, sy * 2 + 1, " ")
    add_frontier(sx, sy)

    while frontier:
        cx, cy, dx, dy = random.choice(frontier)
        frontier.remove((cx, cy, dx, dy))

        nx = cx + dx
        ny = cy + dy

        # if neighbor not visited, carve
        if maze[ny * 2 + 1][nx * 2 + 1] == "#":
            # carve wall
            wx = cx * 2 + 1 + dx
            wy = cy * 2 + 1 + dy
            maze[wy][wx] = " "
            draw_cell(wx, wy, " ")

            # carve neighbor cell
            maze[ny * 2 + 1][nx * 2 + 1] = " "
            draw_cell(nx * 2 + 1, ny * 2 + 1, " ")

            pygame.time.delay(delay)
            pygame.event.pump()

            add_frontier(nx, ny)

    # entrance and exit
    maze[1][0] = "S"
    maze[2 * height - 1][2 * width] = "X"
    draw_cell(0, 1, "S")
    draw_cell(2 * width, 2 * height - 1, "X")

    return maze


def save_maze(maze, filename="maze.json"):
    with open(filename, "w") as f:
        json.dump(maze, f)


def run(width, height, cell_size=10, delay=5, algorithm="dfs"):
    pygame.init()
    h, w = height * 2 + 1, width * 2 + 1
    screen = pygame.display.set_mode((w * cell_size, h * cell_size))
    pygame.display.set_caption("Animated Maze Generator")

    colors = {
        "#": (0, 255, 64),  # Wall = White
        " ": (0, 0, 0),        # Path = Black
        "S": (42, 142, 255),      # Start = Blue
        "X": (200, 0, 0),      # Exit = Red
        "P": (255, 255, 255),
    }

    screen.fill(colors["#"])
    pygame.display.flip()

    if algorithm == "dfs":
        maze = generate_maze_dfs(
            width, height, screen, cell_size, colors, delay)
    else:
        maze = generate_maze_prim(
            width, height, screen, cell_size, colors, delay)

    save_maze(maze)

    # Keep window open after maze is done
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    w = int(input("Enter maze width: "))
    h = int(input("Enter maze height: "))

    algo = select_algorithm()

    # increase delay for slower animation
    run(w, h, cell_size=8, delay=10, algorithm=algo)
