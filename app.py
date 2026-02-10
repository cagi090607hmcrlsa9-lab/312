from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#conexion a la base de datos

def conectar_db():
    return sqlite3.connect("database.db")

#tabla

def crear_tabla():
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS desechos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        tipo TEXT,
        peso REAL,
        precio REAL
    )
    """)
    db.commit()
    db.close()

crear_tabla()

#consultar

@app.route("/")
def index():
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM desechos")
    datos = cursor.fetchall()
    db.close()
    return render_template("index.html", datos=datos)

#guarda

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        tipo = request.form["tipo"]
        peso = request.form["peso"]
        precio = request.form["precio"]

        db = conectar_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO desechos (nombre, tipo, peso, precio) VALUES (?, ?, ?, ?)",
            (nombre, tipo, peso, precio)
        )
        db.commit()
        db.close()

        return redirect(url_for("index"))

    return render_template("registrar.html")

# elimina

@app.route("/eliminar/<int:id>")
def eliminar(id):
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM desechos WHERE id = ?", (id,))
    db.commit()
    db.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
