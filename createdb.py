import sqlite3
con = sqlite3.connect("banco.db")
cursor = con.cursor()
cursor.execute("""
CREATE TABLE note
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 title VARCHAR(150) NOT NULL,
 content VARCHAR NOT NULL,
 favorite BOOLEAN DEFAULT FALSE NOT NULL
)""")

# cursor.execute("""
# INSERT INTO note (id, title, content, favorite)
# VALUES
# (1, 'Receita de miojo', 'Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)', true),
# (2, 'Sorvete com cristais de leite', 'Sirva o seu sorvete favorito em uma vasilha e jogue leite em cima.', false);
# """)

# con.commit()