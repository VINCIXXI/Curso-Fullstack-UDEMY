from flask import Flask,redirect,url_for, render_template,request,flash
from datetime import datetime
from flask_mysqldb import MySQL #se instala pip install flask-mysqldb antes

app=Flask(__name__)

#esa clave se pide para enviar el formulario
app.secret_key="clave_secreta_flask"

#conexion db
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="proyectoflask"

mysql=MySQL(app)

#context processors
@app.context_processor
def date_now():
    return {
        "now":datetime.utcnow
    }

#end points
@app.route("/")
def index():
    personas=["David","Alejandro","Victor"]

    return render_template('index.html',personas=personas)

@app.route("/informacion") #parametro opcional
@app.route("/informacion/<string:nombre>") #parametros con <> 
@app.route("/informacion/<string:nombre>/<apellidos>")
def informacion(nombre=None,apellidos=None):
    texto=""
    if nombre!=None and apellidos!=None:
        texto=f"Bienvenido, {nombre} {apellidos}"
    
    return render_template('informacion.html',texto=texto)

@app.route("/contacto")
@app.route("/contacto/<redireccion>")
def contacto(redireccion=None):
    if redireccion!=None:
        return redirect(url_for("lenguajes"))

    return render_template("contacto.html")

@app.route("/lenguajes-programacion")
def lenguajes():
    return render_template("lenguajes.html")
    #return "<h1>Pagina de lenguajes</h1>"

@app.route("/crear-coche",methods=["GET","POST"])
def crear_coche():
    if request.method=="POST":
        marca=request.form["marca"]
        modelo=request.form["modelo"]
        precio=request.form["precio"]
        ciudad=request.form["ciudad"]

        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL,%s,%s,%s,%s)",(marca,modelo,precio,ciudad))
        cursor.connection.commit()
        flash("Has creado el coche correctamente")
       
        return redirect(url_for("index"))
    
    return render_template("crear_coche.html")

@app.route("/coches")
def coches():
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches")
    coches=cursor.fetchall()
    cursor.close()

    return render_template("coches.html",coches=coches)

@app.route("/coche/<coche_id>")
def coche(coche_id):
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id=%s", (coche_id))
    coche=cursor.fetchall()
    cursor.close()

    return render_template("coche.html",coche=coche[0])

@app.route("/borrar-coche/<coche_id>")
def borrar_coche(coche_id):
    cursor=mysql.connection.cursor()
    cursor.execute("DELETE FROM coches WHERE id=%s", (coche_id))
    mysql.connection.commit()

    flash("El coche ha sido eliminado")

    return redirect(url_for('coches'))

@app.route("/editar-coche/<coche_id>",methods=["GET","POST"])
def editar_coche(coche_id):
    if request.method=="POST":
        marca=request.form["marca"]
        modelo=request.form["modelo"]
        precio=request.form["precio"]
        ciudad=request.form["ciudad"]

        cursor=mysql.connection.cursor()
        cursor.execute("""
            UPDATE coches
            SET marca=%s,
                modelo=%s,
                precio=%s,
                ciudad=%s
            WHERE id=%s
        """,(marca,modelo,precio,ciudad))
        cursor.connection.commit()
        flash("Has creado el coche correctamente")
       
        return redirect(url_for("coches"))

    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id=%s", (coche_id))
    coche=cursor.fetchall()
    cursor.close()

    return render_template("crear_coche.html",coche=coche[0])


if __name__ =="__main__":
    app.run(debug=True) #necesitamos que el servidor este funcionando y se reinicie automaticamente
