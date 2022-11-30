from odoo import models, fields, api

class provincia(models.Model):
    _name = 'concesionario.provincia'
    _descripcion = 'Permite definir los datos de una provincia'

    name = fields.Char(string='Nombre')
    descripcion = fields.Char(string='Descripción')