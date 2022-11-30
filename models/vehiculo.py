from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'concesionario.vehiculo'
    _descripcion = 'Permite definir las características de un vehículo'

    name = fields.Char(string='Matrícula')
    descripcion = fields.Char(string='Descripción')

    marca = fields.Char(string='Marca')
    color = fields.Selection([('blanco', 'Blanco'), ('gris', 'Gris'), ('negro', 'Negro')])
    cantidad_asientos = fields.Integer(string='Cantidad de asientos')

    #Un vehículo ha podido ser conducido sólo un conductor
    conductor_id = fields.Many2one('concesionario.conductor', string='Conductor')
    #un vehiculo puede tener un seguro
    seguro_id = fields.One2one('concesionario.seguro', string='Seguro')