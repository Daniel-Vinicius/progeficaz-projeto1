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
  con.close()

  NOTE_TEMPLATE = load_template("components/note.html")
  notes_li = []

  for note in dbData:
    notes_li.append(NOTE_TEMPLATE.format(id=note[0], title=note[1], details=note[2], favorite=note[3]))
  notes = "\n".join(notes_li)

  return notes

def add_note_toDB(title, detail):
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()
  params = (title, detail)
  cursor.execute(f"INSERT INTO note(title, content) VALUES (?, ?);", params)

  con.commit()
  con.close()

def delete_note(id):
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()

  cursor.execute(f"DELETE FROM note WHERE id=?", id)

  con.commit()
  con.close()

def get_note(id):
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()

  note = None

  for r in cursor.execute(f"SELECT * FROM note WHERE id=?", id):
    note = r

  con.commit()
  con.close()
  return note

def update_note(id, title, detail):
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()
  params = (title, detail, id)
  print(params)

  cursor.execute(f"UPDATE note SET title = ?, content = ? WHERE id = ?;", params)

  con.commit()
  con.close()

def toggle_fav_note(id):
  con = sqlite3.connect("banco.db")
  cursor = con.cursor()

  cursor.execute(f"UPDATE note SET favorite = NOT favorite WHERE id = ?;", id)

  con.commit()
  con.close()