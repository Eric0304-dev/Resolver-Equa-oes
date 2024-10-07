import math

def resolver_equacao_quadratica(a, b, c):
    print(f"\nResolvendo a equação: {a}x² + {b}x + {c} = 0\n")
    
    if a == 0:
        print("O coeficiente 'a' não pode ser 0 em uma equação quadrática.")
        return

    delta = b**2 - 4*a*c
    print(f"Passo 1: Calcular o discriminante (Delta): Δ = b² - 4ac")
    print(f"Δ = ({b})² - 4*({a})*({c})")
    print(f"Δ = {b**2} - {4*a*c}")
    print(f"Δ = {delta}\n")

    if delta < 0:
        print("Delta é negativo (Δ < 0), portanto a equação não possui raízes reais.")
    elif delta == 0:
        print("Delta é igual a 0 (Δ = 0), a equação possui uma única raiz real.\n")
        raiz_unica = -b / (2*a)
        print(f"Passo 2: Calcular a raiz única:")
        print(f"x = -b / 2a")
        print(f"x = -({b}) / 2*({a})")
        print(f"x = {raiz_unica}")
    else:
        print("Delta é positivo (Δ > 0), a equação possui duas raízes reais.\n")
        print("Passo 2: Calcular as raízes usando a fórmula de Bhaskara:")
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        
        print(f"x₁ = (-b + √Δ) / 2a")
        print(f"x₁ = (-({b}) + √{delta}) / 2*({a})")
        print(f"x₁ = ({-b} + {math.sqrt(delta)}) / {2*a}")
        print(f"x₁ = {raiz1}\n")
        
        print(f"x₂ = (-b - √Δ) / 2a")
        print(f"x₂ = (-({b}) - √{delta}) / 2*({a})")
        print(f"x₂ = ({-b} - {math.sqrt(delta)}) / {2*a}")
        print(f"x₂ = {raiz2}")

def main():
    print("=== Resolvedor de Equação Quadrática ===")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    resolver_equacao_quadratica(a, b, c)

if __name__ == "__main__":
    main()
