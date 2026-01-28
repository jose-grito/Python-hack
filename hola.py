#!/usr/bin/env python3
"""
🎯 CURSO DE PYTHON - Menú Principal
github.com/jose-grito/Python-hack
"""

import os

def mostrar_bienvenida():
    print("="*60)
    print("        🐍 CURSO COMPLETO DE PYTHON        ")
    print("="*60)
    print("\n¡Bienvenido al curso de Python desde cero!")
    print("Aprende paso a paso con ejemplos prácticos.")
    print("\n📍 Repositorio: github.com/jose-grito/Python-hack")
    
def mostrar_opciones():
    print("\n📂 CONTENIDO DISPONIBLE:")
    print("1. Lección 01: Hola Mundo")
    print("   → python basico/01-hola-mundo.py")
    print("\n2. Ver estructura completa")
    print("3. Ir al README del curso")
    print("4. Salir")
    
def ver_estructura():
    print("\n📁 ESTRUCTURA DEL CURSO:")
    print("basico/      - Lecciones básicas (en desarrollo)")
    print("intermedio/  - Lecciones intermedias (próximamente)")
    print("avanzado/    - Lecciones avanzadas (próximamente)")
    print("proyectos/   - Proyectos prácticos (próximamente)")
    print("\n✨ Nuevo contenido cada semana!")

if __name__ == "__main__":
    mostrar_bienvenida()
    
    while True:
        mostrar_opciones()
        opcion = input("\n👉 Selecciona una opción (1-4): ")
        
        if opcion == "1":
            print("\n🚀 Ejecutando primera lección...")
            os.system("python basico/01-hola-mundo.py")
            
        elif opcion == "2":
            ver_estructura()
            
        elif opcion == "3":
            print("\n📖 Mostrando README...")
            os.system("cat README.md | head -30")
            
        elif opcion == "4":
            print("\n👋 ¡Hasta pronto! No olvides darle ⭐ al repo")
            break
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")
