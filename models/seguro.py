from odoo import models, fields, api

class seguro(models.Model):
    _name = 'concesionario.seguro'
    _descripcion = 'Permite definir los datos de un seguro'

    name = fields.Char(string='Nombre')
    descripcion = fields.Char(string='Descripción')
    fecha_vecenimiento = fields.Date(string='Fecha de vencimiento')
    #vehiculo-> un seguro pertenece a un vehiculo
    vehiculo_id = fields.Many2one('concesionario.vehiculo', string='Vehículo')