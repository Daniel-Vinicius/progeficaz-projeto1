from utils import load_notes, load_template
def index():
    return load_template("index.html").format(notes=load_notes())
