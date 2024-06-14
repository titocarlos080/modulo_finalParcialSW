import uuid,json
from odoo import http 
from odoo.http import request
from odoo.exceptions import AccessError

class AuthenticationController(http.Controller):
    @http.route('/odoo/auth/login', auth='public', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        ci = kwargs.get('ci')
        keynotificaciones = kwargs.get('keynotificaciones')
        
        return request.make_response(json.dumps({'message': 'No existe el usuario'}), headers={'Content-Type': 'application/json'}, status=404)
    
        user = request.env['oe.school.inscripcion'].sudo().search([('ci', '=', ci)], limit=1)
    
        if user:
            user.keynotificaciones = keynotificaciones
            return request.make_response(json.dumps({ 'id':user.id, 'name': user.name, 'email': user.email,'keynotificaciones': user.keynotificaciones}), headers={'Content-Type': 'application/json'}, status=200)
        else:
            return request.make_response(json.dumps({'message': 'No existe el usuario'}), headers={'Content-Type': 'application/json'}, status=404)
  