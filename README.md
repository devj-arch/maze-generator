# Maze Generator and Visualizer

A Python project that generates mazes using classic algorithms and visualizes them in real time using **pygame**.
The project supports animated maze generation, algorithm selection from the terminal, and saving the maze to a data format for later use.

## Features

* Maze generation using:
  * Depth-First Search (Recursive Backtracker)
  * Prim’s Algorithm

* Real-time animated visualization using pygame

* Clearly distinguishable walls, paths, start and exit
  
* Moving pointer showing the active head of the generation algorithm

* Terminal-based algorithm selection menu

* Maze saved as JSON for reuse in solvers or replay


## Project Structure

``` bash []
maze-generator/
│
├── main.py            # Entry point
├── maze.json          # Saved maze data
├── README.md          # Project documentation
```

## Requirements

* Python 3.9 or newer
* pygame

Install dependencies using:
``` bash
pip install pygame
```

## How to Run

Run the program from the terminal:

``` python
python main.py
```

You will be prompted for:
1. Maze width
2. Maze height
3. Algorithm selection

``` mathematica
Enter maze width: 40
Enter maze height: 40

Select maze generation algorithm:

1. Depth-First Search (Recursive Backtracker)
2. Prim's Algorithm

Enter choice (1 or 2): 1
```

The pygame window will open and animate the maze generation.

## Controls
* Close the pygame window to end visualization

## Maze Representation

* `#` Wall
* ` ` Path
* `S` Start
* `X` Exit

Internally, the maze is stored as a 2D grid of size:

```css
(2 * width + 1) x (2 * height + 1)
```

This ensures continuous walls and proper cell separation.


## Algorithms Overview

### Depth-First Search (Recursive Backtracker)

* Produces long winding corridors
* Simple and fast
* Creates perfect mazes with a single unique solution

  ![DFS Maze animation](https://github.com/user-attachments/assets/1eb78c5a-61c2-4d4d-9e51-d5dd9313cc93)


### Prim’s Algorithm

* Produces more evenly distributed paths
* More branching and shorter corridors
* Also generates perfect mazes

![Prim&#39;s Algo animation](https://github.com/user-attachments/assets/5dd2e206-d2c8-4e82-b7e5-ae69454cf1dc)


## Saved Data

After generation, the maze is saved as:

```bash
maze.json
```

This file can be reused for:

* Maze solving algorithms (BFS, Dijkstra, A*)
* Analysis or export to other formats


## Known Limitations

* Very large mazes may require reducing cell size for display
* Recursive DFS can hit recursion limits for extremely large mazes
* Rendering extremely large grids may impact performance

## Related Repository

🔗 [Maze Solver Repository](https://github.com/devj-arch/maze-solver)


## License

This project is open for learning and experimentation.

Use and modify freely.
