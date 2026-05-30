import matplotlib.pyplot as plt
import os

def graficar_barras(df, col_x, col_y, titulo, nombre_archivo, horizontal=False):
    # Crear carpeta si no existe
    os.makedirs("graficas", exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    if horizontal:
        ax.barh(df[col_x].astype(str), df[col_y], color="#4CAF50")
        ax.set_xlabel(col_y)
        ax.set_ylabel(col_x)
    else:
        ax.bar(df[col_x].astype(str), df[col_y], color="#2196F3")
        ax.set_xlabel(col_x)
        ax.set_ylabel(col_y)

    ax.set_title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # ── NUEVO: GUARDAR LA GRÁFICA EN PNG ANTES DEL SHOW ──
    plt.savefig(f"graficas/{nombre_archivo}.png", dpi=300)
    
    plt.show()

def graficar_lineas(df, col_x, col_y, titulo, nombre_archivo):
    os.makedirs("graficas", exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.plot(df[col_x].astype(str), df[col_y], marker="o", color="#E91E63", linewidth=2)
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(f"graficas/{nombre_archivo}.png", dpi=300)
    plt.show()

def graficar_torta(df, col_etiqueta, col_valor, titulo, nombre_archivo):
    os.makedirs("graficas", exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.pie(df[col_valor], labels=df[col_etiqueta].astype(str), autopct="%1.1f%%", startangle=90)
    ax.set_title(titulo)
    plt.tight_layout()
    
    plt.savefig(f"graficas/{nombre_archivo}.png", dpi=300)
    plt.show()

def graficar_dispersion(df, col_x, col_y, titulo, nombre_archivo):
    os.makedirs("graficas", exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.scatter(df[col_x].astype(str), df[col_y], color="#9C27B0")
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(f"graficas/{nombre_archivo}.png", dpi=300)
    plt.show()
