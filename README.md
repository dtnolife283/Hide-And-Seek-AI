# 🤖 Hide and Seek: AI-Based Game Simulation

A course project for **Introduction to Artificial Intelligence (CTT303)** — Spring 2024.  
This simulation mimics a game of *Hide and Seek* where intelligent agents (seeker and hiders) interact within a grid-based environment, navigating walls, obstacles, and using observation strategies.

## 🕹️ Game Description

The game takes place on a 2D rectangular grid filled with:

- **Walls** (impassable)
- **Movable Obstacles**
- **One Seeker Agent**
- **One or More Hider Agents**

### Rules:
- Agents can move in 8 directions (N, NE, E, SE, S, SW, W, NW).
- Movement is restricted by walls and obstacles.
- Agents observe their surroundings within a limited range.
- Hiders occasionally broadcast approximate positions to the seeker.
- The seeker wins by catching all hiders before time runs out.

## 🎮 Levels of Complexity

1. **Level 1**: One stationary hider, unlimited time.
2. **Level 2**: Multiple stationary hiders, unlimited time.
3. **Level 3**: Movable hiders with 2-cell observation range, turn-based movement.
4. **Level 4**: Hiders reposition obstacles before game start; seeker can move them during the game; time-limited.

## 🧠 AI & Algorithms

- Pathfinding (e.g., A*, BFS)
- Partial observability modeling
- Game scoring system:
  - `-1` point per movement step
  - `+20` points per captured hider


## 🗺️ Input Format

Each map file contains:
- First line: map size (e.g., `10 15`)
- Next N lines: map matrix using integers:
  - `0`: empty
  - `1`: wall
  - `2`: hider
  - `3`: seeker
- Remaining lines: obstacle coordinates (top, left, bottom, right)

## 📦 Output

- **Text-based result**: Map with agent paths, captured hiders, and game points.
- **(Optional)** GUI using graphical libraries for demonstration.

## 🛠️ Environment

- Language: `Python / C++ / Java` (replace with yours)
- Libraries: `numpy`, `pygame`, or others (list dependencies)

## 📈 Evaluation Criteria

| Feature | Score |
|--------|-------|
| Level 1 | 15% |
| Level 2 | 15% |
| Level 3 | 15% |
| Level 4 | 10% |
| Graphics/Visualization | 10% |
| Map Variations (min. 5) | 5% |
| Report & Reflection | 30% |
| **Total** | **100%** |

## 📜 License

This project is for educational purposes only. All rights reserved © 2024.

