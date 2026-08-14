import sqlite3

def load_template(filename):
  arquivo = open(f'static/templates/{filename}')
  return arquivo.read()

def load_notes():
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()
  dbData = []

  for row in cursor.execute("SELECT * FROM note"):
    dbData.append(row)
  print(dbData)
  con.close()

  NOTE_TEMPLATE = load_template("components/note.html")
  notes_li = []

  for note in dbData:
    notes_li.append(NOTE_TEMPLATE.format(id=note[0], title=note[1], details=note[2]))
  notes = "\n".join(notes_li)

  return notes

def add_note_toDB(title, detail):
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()
  params = (title, detail)
  cursor.execute(f"INSERT INTO note(title, content) VALUES (?, ?);", params)

  con.commit()
  con.close()
