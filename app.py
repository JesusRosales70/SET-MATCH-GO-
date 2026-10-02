from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        p1 = request.form.get('p1')
        p2 = request.form.get('p2')
        p3 = request.form.get('p3')

        respuestas = [p1, p2, p3]
        frio_score = respuestas.count('frio')
        calido_score = respuestas.count('calido')

        if calido_score > frio_score:
            estacion = "Otoño / Primavera (Subtono Cálido)"
            descripcion = "Tus tonos dorados y venas verdosas indican que te favorecen las gamas tierra, mostaza, terracota y dorados."
            paleta = ["#D97706", "#B45309", "#78350F", "#F59E0B"]
        elif frio_score > calido_score:
            estacion = "Invierno / Verano (Subtono Frío)"
            descripcion = "Tus rasgos destacan con colores joya, azul marino, borgoña, blanco puro, negro y accesorios plateados."
            paleta = ["#1E3A8A", "#831843", "#0F172A", "#6B21A8"]
        else:
            estacion = "Paleta Neutra"
            descripcion = "Tienes un balance armónico entre tonos fríos y cálidos. Puedes experimentar con casi cualquier color de contraste medio."
            paleta = ["#059669", "#DC2626", "#2563EB", "#D97706"]

        return render_template('resultado.html', estacion=estacion, descripcion=descripcion, paleta=paleta)

    return render_template('test.html')

# ESTA SECCIÓN ES IMPRESCINDIBLE PARA QUE EL SERVIDOR CORRA
if __name__ == '__main__':
    app.run(debug=True)