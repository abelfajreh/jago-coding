import math
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Perhitungan Fisika Dasar")
    parser.add_argument('--snellius', nargs=3, metavar=('theta1', 'v1', 'v2'), type=float, 
                        help="Hitung sudut refraksi menggunakan Hukum Snellius")
    parser.add_argument('--gravitasi', nargs=3, metavar=('m1', 'm2', 'r'), type=float, 
                        help="Hitung gaya gravitasi menggunakan Persamaan Gravitasi Newton")
    parser.add_argument('--hooke', nargs=2, metavar=('k', 'x'), type=float, 
                        help="Hitung gaya pegas menggunakan Hukum Hooke")
    
    args = parser.parse_args()

    if args.snellius:
        theta1, v1, v2 = args.snellius
        print(hukum_snellius(theta1, v1, v2))
    elif args.gravitasi:
        m1, m2, r = args.gravitasi
        print(gravitasi_newton(m1, m2, r))
    elif args.hooke:
        k, x = args.hooke
        print(hukum_hooke(k, x))

if __name__ == "__main__":
    main()
