import matplotlib.pyplot as plt
import pandas as pd

def visualizar_tiempos():
    # Leer los datos del archivo
    df = pd.read_csv('timestamps.txt')
    
    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(df['Rectángulos'], df['Tiempo_Iterativo(ns)'], 'b-', label='Iterativo')
    plt.plot(df['Rectángulos'], df['Tiempo_Recursivo(ns)'], 'r-', label='Recursivo')
    
    plt.xlabel('Número de Rectángulos')
    plt.ylabel('Tiempo (ns)')
    plt.title('Comparación de Rendimiento: Iterativo vs Recursivo')
    plt.legend()
    plt.grid(True)
    
    # Guardar la gráfica
    plt.savefig('comparacion_tiempos.png')
    plt.close()

if __name__ == "__main__":
    visualizar_tiempos() 