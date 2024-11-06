"""Hukum Fisika.

Usage:
  5TUGAS1_docopt.py snellius <theta1> <v1> <v2>
  5TUGAS1_docopt.py gravitasi <m1> <m2> <r>
  5TUGAS1_docopt.py hooke <k> <x>

Options:
  -h --help     Show this screen.
  
Examples:
  5TUGAS1_docopt.py snellius 30 1500 3000
  5TUGAS1_docopt.py gravitasi 6.972e24 7.358e22 394400000
  5TUGAS1_docopt.py hooke 100 0.2
"""
from docopt import docopt
import math

def hukum_snellius(theta1, v1, v2):
    theta1_rad = math.radians(theta1)
    sin_theta2 = (v2 / v1) * math.sin(theta1_rad)
    
    if sin_theta2 > 1:
        return "Tidak ada refraksi, terjadi refleksi internal."
    else:
        theta2 = math.degrees(math.asin(sin_theta2))
        return f"Sudut refraksi (theta2): {theta2:.2f} derajat"

def gravitasi_newton(m1, m2, r):
    G = 6.674 * 10**-11
    F = G * (m1 * m2) / r**2
    return f"Gaya gravitasi (F): {F:.2e} N"

def hukum_hooke(k, x):
    F = -k * x
    return f"Gaya pegas (F): {F:.2f} N"

if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['snellius']:
        theta1 = float(arguments['<theta1>'])
        v1 = float(arguments['<v1>'])
        v2 = float(arguments['<v2>'])
        print(hukum_snellius(theta1, v1, v2))
    elif arguments['gravitasi']:
        m1 = float(arguments['<m1>'])
        m2 = float(arguments['<m2>'])
        r = float(arguments['<r>'])
        print(gravitasi_newton(m1, m2, r))
    elif arguments['hooke']:
        k = float(arguments['<k>'])
        x = float(arguments['<x>'])
        print(hukum_hooke(k, x))
