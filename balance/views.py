from flask import render_template, request

from .models import ListaMovimientos, Movimiento
from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    return render_template('inicio.html', movs=lista.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])

def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    lista = ListaMovimientos()
    
    if request.method == 'GET':
        return render_template('nuevo.html')
    
    if request.method == 'POST':
            
        mov = Movimiento(request.form["date"], 
                         request.form["subject"],
                         request.form["mov_type"], 
                         request.form["amount"])
        
   
        lista.agregarMovimiento(mov)

        if mov.has_errors()>0:
            return f"ERROR: {mov.errores}"
        else:
            return "OK"
        
        return render_template('nuevo.html')


@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento'


@app.route('/borrar')
def delete():
    """
    Elimina un movimiento existente
    """
    return 'Borrar movimiento'
