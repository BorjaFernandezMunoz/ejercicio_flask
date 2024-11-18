import csv
from datetime import date

from flask import render_template

from . import RUTA_FICHERO


class Movimiento:

    def __init__(self, fecha, concepto, tipo, cantidad):

        self.errores = []

        try:
            self.fecha = date.fromisoformat(fecha)

        except ValueError:
            self.fecha = None
            mensaje = f'La fecha {fecha} no es una fecha ISO 8601 válida'
            self.errores.append(mensaje)

        return render_template('nuevo.html') 
    
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad
        #Aquí hay un problema que no entiendo __init__() should return None, not 'str'
        if self.concepto==None or self.tipo==None or self.cantidad==None:
            
            mensaje ="Datos incompletos"
            self.errores.append(mensaje)

        else:
            pass



    @property
    def has_errors(self):

        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}'

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(
                    fila.get('fecha', None),
                    fila.get('concepto', 'Varios'),
                    fila.get('ingreso_gasto', '-'),
                    fila.get('cantidad', 0)
                )
                self.movimientos.append(movimiento)

    def guardar(self):
        with open(RUTA_FICHERO, 'w') as fichero:
            # cabeceras = ['fecha', 'concepto', 'ingreso_gasto', 'cantidad']
            # writer = csv.writer(fichero)
            # writer.writerow(cabeceras)

            cabeceras = list(self.movimientos[0].__dict__.keys())
            cabeceras.remove('errores')

            writer = csv.DictWriter(fichero, fieldnames=cabeceras)
            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                mov_dict.pop('errores')
                writer.writerow(mov_dict)

    def agregarMovimiento(self, movimiento):

        self.leer_desde_archivo()
        self.movimientos.append(movimiento)
        self.guardar()


    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result
