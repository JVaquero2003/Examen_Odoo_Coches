from odoo import models, fields, api

class conductor(models.Model):
    _name = 'concesionario.conductor'
    _descripcion = 'Permite definir los datos de un conductor'

    name = fields.Char(string='Nombre')
    descripcion = fields.Char(string='Descripción')
    dni = fields.Char(string='DNI')
    apellidos = fields.Char(string='Apellidos')
    dni = fields.Char(string='DNI')
    #Un conductor ha podido conducir n vehiculos
    vehiculo_ids = fields.One2many('concesionario.vehiculo', 'conductor_id', string='vehiculos')         