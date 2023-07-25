from odoo import models, fields, api
import json
import logging 
import base64

_logger = logging.getLogger(__name__)

class JsonImport(models.TransientModel):
    _name = 'json.import'
    _description = 'JSON Import Wizard'

    json_file = fields.Binary(string="Archivo JSON", required=True)

    def import_data(self):
        # Envia un mensaje de error en la consola si no existe el archivo
        if not self.json_file:
            _logger.error("Archivo JSON vacío")
            
            return

        #Decodifica el contenido del archivo JSON con el modulo base64
        try:
            json_data = base64.b64decode(self.json_file).decode('utf-8')
            json_obj = json.loads(json_data)
            _logger.info(json_obj)
        except json.decoder.JSONDecodeError as e:
            #informa en consola
            _logger.error("Error al decodificar el archivo JSON: %s", e)
            
            return

        # Agregar mensaje de registro para verificar la ejecución del método
        _logger.info("Importando datos del JSON...")
        _logger.info("Contenido del archivo JSON: %s", self.json_file.decode('utf-8'))

        # Crear un registro en el modelo "registro" usando los datos del JSON
        registro_model = self.env['registro']
        nuevo_registro = registro_model.create({
            'nombre': json_obj.get('nombre'),
            'edad': json_obj.get('edad'),
            'sexo': json_obj.get('sexo'),
        })

        

        return {'type': 'ir.actions.act_window_close'}


class Registro(models.Model):
    _name = 'registro'
    _description = 'Registro del JSON'

    nombre = fields.Char(string="Nombre")
    edad = fields.Integer(string="Edad")
    sexo = fields.Selection(selection=[('macho', 'Macho'), ('hembra', 'Hembra')], string='Sexo')


#en este caso solo importaria esos datos
