from utils import load_notes, load_template, add_note_toDB, delete_note
def index():
    return load_template("index.html").format(notes=load_notes())

def submit(titulo, detalhes):
    return add_note_toDB(titulo, detalhes)

def delete(id_nota):
    return delete_note(id_nota)
