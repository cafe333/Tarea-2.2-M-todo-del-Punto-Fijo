import numpy as np
import matplotlib.pyplot as plt

# Definir la función g(x) para el método de punto fijo
def g(x):
    return np.exp(x) / 4  # Transformación de e^x - 4x = 0

# Método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []
    errores_abs = []

    x_old = x0
    for i in range(max_iter):
        x_new = g(x_old)
        e_abs = abs(x_new - x_old)

        iteraciones.append((i+1, x_new, e_abs))
        errores_abs.append(e_abs)

        if e_abs < tol:
            break

        x_old = x_new

    return iteraciones, errores_abs

# Parámetro inicial
x0 = 1.0  
iteraciones, errores_abs = punto_fijo(x0)

# Imprimir resultados
print("Iteración | x_n      | Error absoluto")
print("-------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e}")

# Graficar convergencia
x_vals = np.linspace(0, 2, 100)
y_vals = g(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$g(x) = \frac{e^x}{4}$", color="blue")
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")
plt.scatter([it[1] for it in iteraciones], [g(it[1]) for it in iteraciones], color="black")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid()
plt.title("Método de Punto Fijo - Ejercicio 2")
plt.show()
