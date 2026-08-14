from utils import get_note, load_notes, load_template, add_note_toDB, delete_note, update_note

def index():
    return load_template("index.html").format(notes=load_notes())

def submit(titulo, detalhes):
    return add_note_toDB(titulo, detalhes)

def delete(id_nota):
    return delete_note(id_nota)

def update_page(id_nota):
    note = get_note(id_nota)
    return load_template("edit.html").format(id=id_nota, defaultTitle=note[1], defaultDetail=note[2])

def update(id, titulo, detalhes):
    return update_note(id, titulo, detalhes)
