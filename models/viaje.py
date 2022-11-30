from odoo import models, fields, api

class viaje(models.Model):
    _name = 'concesionario.viaje'
    _descripcion = 'Permite definir los datos de un viaje'

    name = fields.Char(string='Nombre')
    descripcion = fields.Char(string='Descripción')
    fecha_realizacion = fields.Date(string='Fecha de realización')
    duracion = fields.DateTime(string='Duración')
    #un viaje puede ser realizado por un vehiculo
    vehiculo_id = fields.Many2one('concesionario.vehiculo', 'viaje_id', string='Vehículo')
    #un viaje puede ser realizado por un conductor
    conductor_id = fields.Many2one('concesionario.conductor', 'viaje_id', string='Conductor')
    #provincia origen -> 1:1 Relación con el modelo provincia
    provincia_origen_id = fields.Many2one('concesionario.provincia', 'viaje_id', string='Provincia de origen')
    #provincia destino -> 1:1 Relación con el modelo provincia
    provincia_destino_id = fields.Many2one('concesionario.provincia', 'viaje_id', string='Provincia de destino')

    #un campo onchange que mediante un booleano indique si la duración ha sido mayor a 2 horas
    @api.onchange('duracion')
    def _onchange_duracion(self):
        if self.duracion > 2:
            self.name = True
        else:
            self.name = False
    
    #se debe mostrar un aviso si el vehiculo del viaje tiene el seguro caducado
    @api.onchange('vehiculo_id')
    def _onchange_vehiculo_id(self):
        if self.vehiculo_id.seguro_id.fecha_vecenimiento < self.fecha_realizacion:
            self.name = True
        else:
            self.name = False
