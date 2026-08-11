from utils import load_notes, load_template, add_note_to_JSON
def index():
    return load_template("index.html").format(notes=load_notes())

def submit(titulo, detalhes):
    return add_note_to_JSON(titulo, detalhes)
