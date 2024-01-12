import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Crear datos sintéticos
rng = np.random.default_rng(42)
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, label='Estudiantes', color='blue')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Matemáticas')
plt.ylabel('Ciencias')
plt.legend()
plt.show()

# Gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones_promedio = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

plt.figure(figsize=(8, 6))
plt.bar(materias, calificaciones_promedio, yerr=errores, capsize=5, color='green', alpha=0.7)
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.show()

# Histograma
plt.figure(figsize=(8, 6))
sns.histplot(matematicas, bins=10, kde=True, color='orange')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')
plt.show()
