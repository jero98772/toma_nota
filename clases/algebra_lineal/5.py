from sympy import symbols, Eq, solve

# Definimos las variables
P_T, P_G, P_F = symbols('P_T P_G P_F')

# Ecuaciones
eq1 = Eq(P_T, (19/18) * P_G)          # Relación entre Tribuna y General
eq2 = Eq(P_G, (6/5) * P_F)            # Relación entre General y Fondo
eq3 = Eq(P_T + P_G + P_F, 104)        # Total al comprar una de cada localidad

# Sustituir las ecuaciones
eq3_sub = eq3.subs(P_T, (19/18) * P_G).subs(P_G, (6/5) * P_F)

# Resolver el sistema de ecuaciones
solution = solve(eq3_sub, P_F)
P_F_value = solution[0]
P_G_value = (6/5) * P_F_value
P_T_value = (19/18) * P_G_value

P_F_value, P_G_value, P_T_value


# Total a pagar por Fondo y General
total_F_G = P_F_value + P_G_value

# Total a pagar por Fondo y Tribuna
total_F_T = P_F_value + P_T_value

total_F_G, total_F_T
