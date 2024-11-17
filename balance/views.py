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
        # TODO: crear un movimiento, agregarlo a la lista, guardar la lista y devolver el texto 'OK' (o 'ERROR' si falla)
        
        datosIngresados = request.form
        for elmnt in datosIngresados:
            if datosIngresados[value]=='':
                return render_template('nuevo.html', "Error: datos incompletos")
           
            else:

                mov = Movimiento(request.form["date"], 
                            request.form["subject"],
                            request.form["mov_type"], 
                            request.form["amount"])
        
            lista.agregarMovimiento(mov)

            return render_template('nuevo.html', "Datos agregados")


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
