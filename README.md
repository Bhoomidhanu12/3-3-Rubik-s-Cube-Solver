# 3-3-Rubik-s-Cube-Solver
To solve a 3×3 Rubik’s Cube from any scrambled state
This project implements an efficient solver for the 3×3 Rubik’s Cube based on **Kociemba’s Two-Phase Algorithm**. It takes any valid scrambled cube state and returns a minimal or near-optimal sequence of moves to solve it.
## Features
- Solves **any valid scrambled 3×3 cube**
- Uses **Kociemba's optimal two-phase algorithm**
- Efficiently predicts cube state and simulates moves
- Modular design for state prediction, move simulation, and solution generation
- Extendable to support 2x2, 4x4, and more
   ## 📚 What is Kociemba's Algorithm?
Kociemba's Two-Phase Algorithm breaks the solution into:
### Phase 1:  
Transform the cube into a special subset (the **G1 group**) where:
- All edges are oriented
- The middle layer edges are in the middle layer
### Phase 2:  
From that subset, it moves the cube into the **solved state** using allowed moves in a limited move set.
This design reduces search space significantly, often solving in under **20 moves**.
## Data Structures Used
- **String**: To represent cube state (54-char string: `URFDLB`)
- **Hash Tables**: For pruning tables and fast lookups
- **Arrays**: To represent facelets, corner/edge orientation and permutations
- ## 🧮 Time & Space Complexity
| Phase      | Time Complexity     | Space Complexity  |
|------------|---------------------|-------------------|
| Phase 1    | O(b^d), b≈18, d≈7   | ~1MB (prune table)|
| Phase 2    | O(b^d), b≈10, d≈10  | ~1MB (prune table)|
| Total      | Fast enough for <100ms solutions | ~2MB Total |
 **Note**: Pruning tables are precomputed to guide the solver efficiently.
## 🎯 Input Format
You must provide a **54-character string** representing the cube, face by face:
Order:  
`U` (Up), `R` (Right), `F` (Front), `D` (Down), `L` (Left), `B` (Back)
Each face has 9 letters (top-left to bottom-right):
UUUUUUUUURRRRRRRRRGGGGGGGGGDDDDDDDDDLLLLLLLLLBBBBBBBBB
