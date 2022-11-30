from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'concesionario.vehiculo'
    _descripcion = 'Permite definir las características de un vehículo'

    name = fields.Char(string='Matrícula')
    descripcion = fields.Char(string='Descripción')

    marca = fields.Char(string='Marca')
    color = fields.Selection([('blanco', 'Blanco'), ('gris', 'Gris'), ('negro', 'Negro')])
    cantidad_asientos = fields.Integer(string='Cantidad de asientos')

    #conductores->Un vehículo ha podido ser conducido sólo un conductor
    conductor_id = fields.Many2one('concesionario.conductor', 'vehiculo_id', string='Conductor')
    #seguro-> un vehiculo puede tener un seguro
    seguro_id = fields.Many2one('concesionario.seguro', string='Seguro')
    #viajes->Un vehículo ha podido ser realizar n viajes
    viaje_ids = fields.One2many('concesionario.viaje', 'vehiculo_id', string='Viajes')
