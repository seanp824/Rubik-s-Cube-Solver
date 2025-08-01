import unittest
import random

# Import from your main.py
from main import (
    U, U_prime, D, D_prime, L, L_prime, R, R_prime,
    F, F_prime, B, B_prime,
    solve_white_daisy, solve_daisy_to_white_cross,
    is_white_cross_complete,
)

def make_solved_cube():
    return {
        'U': ['W'] * 9,
        'D': ['Y'] * 9,
        'F': ['G'] * 9,
        'B': ['B'] * 9,
        'L': ['O'] * 9,
        'R': ['R'] * 9
    }

def apply_move(cube, move):
    if move == 'U': U(cube, [])
    elif move == "U'": U_prime(cube, [])
    elif move == 'D': D(cube, [])
    elif move == "D'": D_prime(cube, [])
    elif move == 'L': L(cube, [])
    elif move == "L'": L_prime(cube, [])
    elif move == 'R': R(cube, [])
    elif move == "R'": R_prime(cube, [])
    elif move == 'F': F(cube, [])
    elif move == "F'": F_prime(cube, [])
    elif move == 'B': B(cube, [])
    elif move == "B'": B_prime(cube, [])
    elif move == 'U2': U(cube, []); U(cube, [])
    elif move == 'D2': D(cube, []); D(cube, [])
    elif move == 'L2': L(cube, []); L(cube, [])
    elif move == 'R2': R(cube, []); R(cube, [])
    elif move == 'F2': F(cube, []); F(cube, [])
    elif move == 'B2': B(cube, []); B(cube, [])

def random_scramble(length=20):
    faces = ['U', 'D', 'L', 'R', 'F', 'B']
    suffixes = ['', "'", '2']
    scramble = []
    while len(scramble) < length:
        face = random.choice(faces)
        if scramble and scramble[-1][0] == face:
            continue  # avoid repeats
        scramble.append(face + random.choice(suffixes))
    return scramble

class TestWhiteCross(unittest.TestCase):
    def test_white_cross_on_scrambles(self):
        random.seed(42)
        for i in range(20):  # 20 test scrambles
            scramble = random_scramble()
            cube = make_solved_cube()
            for mv in scramble:
                apply_move(cube, mv)
            move_log = []
            solve_white_daisy(cube, move_log)
            solve_daisy_to_white_cross(cube, move_log)
            with self.subTest(scramble=' '.join(scramble)):
                self.assertTrue(
                    is_white_cross_complete(cube),
                    msg=f"White cross failed on scramble: {' '.join(scramble)}"
                )

if __name__ == "__main__":
    unittest.main()
