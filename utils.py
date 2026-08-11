import json

def load_template(filename):
  arquivo = open(f'static/templates/{filename}')
  return arquivo.read()

def load_data(filename):
  arquivo = open(f'static/data/{filename}')
  conteudo = arquivo.read()
  decoder = json.decoder.JSONDecoder()
  dicionario = decoder.decode(conteudo)
  return dicionario

def load_notes():
  data = load_data("notes.json")
  NOTE_TEMPLATE = load_template("components/note.html")
  notes_li = []

  for d in data:
    notes_li.append(NOTE_TEMPLATE.format(title=d['titulo'], details=d['detalhes']))
  notes = "\n".join(notes_li)

  return notes
