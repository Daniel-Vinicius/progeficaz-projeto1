from flask import Flask, render_template_string, request, redirect
import views

app = Flask(__name__)
app.static_folder = "static"

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/delete/', defaults={'NOTA_ID': None})
@app.route('/delete/<NOTA_ID>')
def delete_note(NOTA_ID):
    views.delete(NOTA_ID)
    return redirect('/')

@app.route('/favorite/', defaults={'NOTA_ID': None})
@app.route('/favorite/<NOTA_ID>')
def favorite_note_route(NOTA_ID):
    views.favorite_note(NOTA_ID)
    return redirect('/')

@app.route('/update/', defaults={'NOTA_ID': None})
@app.route('/update/<NOTA_ID>')
def update_note(NOTA_ID):
    return render_template_string(views.update_page(NOTA_ID))

@app.route('/update/id=<NOTA_ID>&titulo=<NOTA_TITULO>&detalhes=<NOTA_DETALHES>', methods=['POST'])
def update(NOTA_ID, NOTA_TITULO, NOTA_DETALHES):
    views.update(NOTA_ID, NOTA_TITULO, NOTA_DETALHES)
    return redirect('/')

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)