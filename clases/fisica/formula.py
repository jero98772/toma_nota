from math import sqrt,pi

def campo_magnetico_solenoide(mu0, I, N, L, a, x):
    """
    Calcula la intensidad del campo magnético Bx en un solenoide en el punto x.

    Parámetros:
    mu0 : float  -> Permeabilidad magnética del vacío (4π × 10⁻⁷ T·m/A).
    I   : float  -> Corriente eléctrica en amperios (A).
    N   : int    -> Número de vueltas del solenoide.
    L   : float  -> Longitud del solenoide en metros (m).
    a   : float  -> Radio del solenoide en metros (m).
    x   : float  -> Posición en el eje del solenoide donde se mide el campo.

    Retorna:
    Bx  : float  -> Intensidad del campo magnético en Teslas (T).
    """
    term1 = (L / 2 - x) / sqrt((L / 2 - x)**2 + a**2)
    term2 = (L / 2 + x) / sqrt((L / 2 + x)**2 + a**2)
    Bx = (mu0 * I * N) / (2 * L) * (term1 + term2)
    return Bx

# Parámetros de ejemplo
mu0 = 4 * pi * 1e-7  # Permeabilidad magnética del vacío (T·m/A)
I = 1  # Corriente en Amperios
N = 75  # Número de vueltas
L = 0.16  # Longitud del solenoide en metros
a = 0.013  # Radio del solenoide en metros
x = -0.08  # Posición en el eje donde se mide el campo

# Cálculo del campo magnético
for i in range(-8,10,2):
    Bx = campo_magnetico_solenoide(mu0, I, N, L, a, i/100)
    #print(f"{i/100}) Campo magnético en x={i/100} m: {Bx:.6e} T")
    print(Bx)

"""
0.00029355693795503086
0.0005402047322570685
0.0005729137455850608
0.0005799121124276308
0.0005814220537125553
0.0005799121124276308
0.0005729137455850608
0.0005402047322570685
0.00029355693795503086

"""