from flask import Flask, render_template, request
import math

app = Flask(__name__)

def formatar_numero(numero):
    if numero.is_integer():
        return int(numero) 
    else:
        return round(numero, 4)  

def resolver_equacao_quadratica(a, b, c):
    passos = []
    passos.append(f"Resolvendo a equação: {a}x² + {b}x + {c} = 0")
    delta = b**2 - 4*a*c
    passos.append(f"Passo 1: Calcular o discriminante (Delta): Δ = b² - 4ac")
    passos.append(f"Δ = ({b})² - 4*({a})*({c})")
    passos.append(f"Δ = {b**2} - {4*a*c}")
    passos.append(f"Δ = {delta}\n")

    if delta < 0:
        passos.append("Delta é negativo (Δ < 0), portanto a equação não possui raízes reais.")
        return passos, None
    elif delta == 0:
        passos.append("Delta é igual a 0 (Δ = 0), a equação possui uma única raiz real.")
        raiz_unica = -b / (2*a)
        raiz_unica = formatar_numero(raiz_unica)
        passos.append(f"Passo 2: Calcular a raiz única:")
        passos.append(f"x = -b / 2a")
        passos.append(f"x = -({b}) / 2*({a})")
        passos.append(f"x = {raiz_unica}")
        return passos, [raiz_unica]
    else:
        passos.append("Delta é positivo (Δ > 0), a equação possui duas raízes reais.\n")
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        
        raiz1 = formatar_numero(raiz1)
        raiz2 = formatar_numero(raiz2)

        passos.append(f"x₁ = (-b + √Δ) / 2a")
        passos.append(f"x₁ = (-({b}) + √{delta}) / 2*({a})")
        passos.append(f"x₁ = {raiz1}\n")
        
        passos.append(f"x₂ = (-b - √Δ) / 2a")
        passos.append(f"x₂ = (-({b}) - √{delta}) / 2*({a})")
        passos.append(f"x₂ = {raiz2}")
        
        return passos, [raiz1, raiz2]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        passos, raizes = resolver_equacao_quadratica(a, b, c)
        return render_template('result.html', passos=passos, raizes=raizes)
    except ValueError:
        return render_template('result.html', error="Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    app.run(debug=True)
