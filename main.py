
Rubik's Cube Solver using Kociemba's Algorithm
Author: Dharani Neelapuram (or your name)
Requirements: pip install kociemba

import kociemba
def convert_to_facelets(color_string):
  #Converts 54-character cube color input to facelet notation.
  #Mapping is done based on center color of each face.
    if len(color_string) != 54:
        raise ValueError("Input must be exactly 54 characters (6 faces × 9 tiles).")
 # Get center colors
    centers = {
        'U': color_string[4],
        'R': color_string[13],
        'F': color_string[22],
        'D': color_string[31],
        'L': color_string[40],
        'B': color_string[49],
    }

    # Reverse map: color → face identifier
    color_to_face = {v: k for k, v in centers.items()}
    facelets = ''.join(color_to_face.get(c, '?') for c in color_string)
    if '?' in facelets:
        raise ValueError("Invalid color mapping. Check if centers are unique and consistent.")

    return facelets

def solve_cube(color_input):
    #Solves the cube from a given 54-character color input string.
    #Returns the optimal move sequence or an error.
    try:
        facelets = convert_to_facelets(color_input)
        solution = kociemba.solve(facelets)
        return solution
    except Exception as e:
        return f" Error: {e}"

if __name__ == "__main__":
    # Replace this string with your scrambled cube's 54-color input
    example_input = (
        'WWWWWWWWW'  # U
        'RRRRRRRRR'  # R
        'GGGGGGGGG'  # F
        'YYYYYYYYY'  # D
        'OOOOOOOOO'  # L
        'BBBBBBBBB'  # B
    )
    print("Input Cube State:", example_input)
    print(" Solving...")
    result = solve_cube(example_input)
    print(" Solution:", result)


#try with example scrumbled input-example_input = (
    "DUUBULFRD"  # U
    "FDRFURRRD"  # R
    "LFBLFFDBU"  # F
    "DRDDBFLUD"  # D
    "LULULLBBL"  # L
    "BGGBRRGGF"  # B
)

