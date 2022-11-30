from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'concesionario.vehiculo'
    _descripcion = 'Permite definir las características de un vehículo'

    name = fields.Char(string='Matrícula')
    descripcion = fields.Char(string='Descripción')
    marca = fields.Char(string='Marca')
    color = fields.Selection([('blanco', 'Blanco'), ('gris', 'Gris'), ('negro', 'Negro')], string='Color')
    transito = fields.Selection([('verde', 'Verde'), ('rojo', 'Rojo')], string='En tránsito')
    cantidad_asientos = fields.Integer(string='Cantidad de asientos')

    #conductores->Un vehículo ha podido ser conducido sólo un conductor
    conductor_id = fields.Many2one('concesionario.conductor', string='conductor')
    #seguro-> un vehiculo puede tener un seguro
    seguro_id = fields.Many2one('concesionario.seguro', string='seguro')
    #viajes->Un vehículo ha podido ser realizar n viajes
    viaje_ids = fields.One2many('concesionario.viaje', 'vehiculo_id', string='viajes')      

    #un campo onchange que mediante un booleano indique si el vehiculo tiene conductor
    # si el vehiculo tiene conductor, el campo booleano debe ser True
    # si el vehiculo no tiene conductor, el campo booleano debe ser False
    @api.onchange('conductor_id')
    def _onchange_conductor_id(self):
        if self.conductor_id:
            self.name = True
        else:
            self.name = False
    #se marcarán de color aquellos vehiculos cuyo seguro haya vencido en plazo.
    @api.onchange('seguro_id','viaje_ids','transito')
    def _onchange_color(self):
        if self.seguro_id.fecha_vecenimiento < self.viaje_ids.fecha_realizacion:
            self.transito = 'rojo'
        else:
            self.transito = 'verde'