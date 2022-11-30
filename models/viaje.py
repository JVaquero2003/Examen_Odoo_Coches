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

# Path: views/viaje.xml
# Compare this snippet from views/__init__.py:
# # -*- coding: utf-8 -*-
#
# from . import vehiculo, conductor, seguro, viaje
#
#
# Compare this snippet from views/vehiculo.xml:
# <?xml version="1.0" encoding="utf-8"?>
# <odoo>
#     <data>
#         <record id="vehiculo_tree_view" model="ir.ui.view">
#             <field name="name">Vehículo</field>
#             <field name="model">concesionario.vehiculo</field>
#             <field name="arch" type="xml">
#                 <tree string="Vehículos">
#                     <field name="name"/>
#                     <field name="descripcion"/>
#                     <field name="marca"/>
#                     <field name="color"/>
#                     <field name="cantidad_asientos"/>
#                     <field name="conductor_id"/>
#                     <field name="seguro_id"/>
#                 </tree>
#             </field>
#         </record>
#         <record id="vehiculo_form_view" model="ir.ui.view">
#             <field name="name">Vehículo</field>
#             <field name="model">concesionario.vehiculo</field>
#             <field name="arch" type="xml">
#                 <form string="Vehículos">
#                     <sheet>
#                         <group>
#                             <field name="name"/>
#                             <field name="descripcion"/>
#                             <field name="marca"/>
#                             <field name="color"/>
#                             <field name="cantidad_asientos"/>
#                             <field name="conductor_id"/>
#                             <field name="seguro_id"/>
#                         </group>
#                     </sheet>
#                 </form>
#             </field>
#         </record>
#         <record id="vehiculo_search_view" model="ir.ui.view">
#             <field name="name">Vehículo</field>
#             <field name="model">concesionario.vehiculo</field>
#             <field name="arch" type="xml">
#                 <search string="Vehículos">
#                     <field name="name"/>
#                     <field name="descripcion"/>
#                     <field name="marca"/>
#                     <field name="color"/>
#                     <field name="cantidad_asientos"/>
#                     <field name="conductor_id"/>
#                     <field name="seguro_id"/>
#                 </search>
#             </field>
#         </record>
#         <record id="vehiculo_action" model="ir.actions.act_window">
#             <field name="name">Vehículos</field>
#             <field name="res_model">concesionario.vehiculo</field>
#             <field name="view_mode">tree,form</field>
#             <field name="view_id" ref="vehiculo_tree_view"/>
#             <field name="search_view_id" ref="vehiculo_search_view"/>
#         </record>
#         <menuitem id="vehiculo_menu" name="Vehículos" parent="concesionario_menu" action="vehiculo_action"/>
#     </data>
# </odoo>