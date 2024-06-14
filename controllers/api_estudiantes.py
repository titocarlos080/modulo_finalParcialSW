import json
from odoo import http,models
from odoo.http import request


import logging  # Asegúrate de importar el módulo logging
# Configurar el logger
_logger = logging.getLogger(__name__)


class AuthenticationController(http.Controller):
    @http.route('/odoo/auth/login2', auth='public', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        ci = kwargs.get('ci')
        keynotificaciones = kwargs.get('keynotificaciones')
    
        user = request.env['oe.school.padre'].sudo().search([('ci', '=', ci)], limit=1)
                # Registrar los valores específicos en la consola
        _logger.info('CI recibido: %s', ci)
        _logger.info('Keynotificaciones recibido: %s', keynotificaciones)
        _logger.info('id obtenido: %s', user.id)
        
        if user:
            user.keynotificaciones = keynotificaciones
            return request.make_response(json.dumps({ 'id':user.id, 'name': user.name, 'ci': user.ci,'keynotificaciones': user.keynotificaciones}), headers={'Content-Type': 'application/json'}, status=200)
        else:
            return request.make_response(json.dumps({'message': 'No existe el padre'}), headers={'Content-Type': 'application/json'}, status=404)
  
class EstudianteController(http.Controller):
    @http.route('/odoo/estudiante/padre/<int:padre_id>', auth='public', methods=['GET'], csrf=False)
    def listar_estudiantes_por_padre(self, padre_id, **kwargs):
        try:
            # Buscar los estudiantes que tengan como padre o apoderado el ID proporcionado
            estudiantes = request.env['res.partner'].sudo().search([('padre_id', '=', padre_id)])
            estudiantes_data = []
            for estudiante in estudiantes:
                estudiante_data = {
                    'id': estudiante.id,
                    'name': estudiante.name,
                    'rude': estudiante.rude,
                    # Añade más campos si es necesario
                }
                estudiantes_data.append(estudiante_data)
            return request.make_response(json.dumps(estudiantes_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)

    @http.route('/odoo/estudiante/inscripciones/<int:estudiante_id>', auth='public', methods=['GET'], csrf=False)
    def obtener_inscripciones_por_estudiante(self, estudiante_id, **kwargs):
        try:
            # Buscar las inscripciones asociadas al estudiante
            inscripciones = request.env['oe.school.inscripcion'].sudo().search([('student_id', '=', estudiante_id)])

            # Procesar las inscripciones encontradas
            inscripciones_data = []
            for inscripcion in inscripciones:
                inscripcion_data = {
                    'id': inscripcion.id,
                    'gestion': inscripcion.gestion if inscripcion.gestion else None,
                    'nivel_id': inscripcion.nivel_id.name if inscripcion.nivel_id else None,
                    'student_id': inscripcion.student_id.name if inscripcion.student_id else None,
                    'curso': inscripcion.curso_id.name if inscripcion.curso_id else None,
                    'create_uid': inscripcion.create_uid.name if inscripcion.create_uid else None,
                    'write_uid': inscripcion.write_uid.name if inscripcion.write_uid else None,
                    'descripcion': inscripcion.descripcion,
                    'create_date': inscripcion.create_date.isoformat() if inscripcion.create_date else None,
                    'write_date': inscripcion.write_date.isoformat() if inscripcion.write_date else None,
                }
                inscripciones_data.append(inscripcion_data)

            # Devolver la respuesta JSON
            return request.make_response(json.dumps(inscripciones_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
    
    
    @http.route('/odoo/estudiante/notas/<int:estudiante_id>', auth='public', methods=['GET'], csrf=False)
    def obtener_notas_por_estudiante(self, estudiante_id, **kwargs):
        try:
            # Buscar las notas asociadas al estudiante
            notas = request.env['oe.school.notas'].sudo().search([('student_id', '=', estudiante_id)])

            # Procesar las notas encontradas
            notas_data = []
            for nota in notas:
                
                nota_data = {
                    'student': nota.student_id.name if nota.student_id else None,
                    'materia': nota.materia_id.name if nota.materia_id else None,
                    'nota': nota.nota,
                    'gestion': nota.gestion,
                }
                
                notas_data.append(nota_data)

            # Devolver la respuesta JSON
            return request.make_response(json.dumps(notas_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
        
class CursoController(http.Controller):
    @http.route('/odoo/cursos', auth='public', methods=['GET'], csrf=False)
    def listar_cursos(self, **kwargs):
        try:
            cursos = request.env['oe.school.course'].search([])

            cursos_data = []
            for curso in cursos:
                curso_data = {
                    'name': curso.name, 
                    'code': curso.code,
                    'complete_name': curso.complete_name,
                    'active': curso.active,
                    'company_id': curso.company_id.name if curso.company_id else None,
                    # Agregar más campos según sea necesario
                }
                cursos_data.append(curso_data)

            return request.make_response(json.dumps(cursos_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)


 
    @http.route('/odoo/estudiante/materias/<int:estudiante_id>', auth='public', methods=['GET'], csrf=False)
    def obtener_lista_curso_materia(self, estudiante_id, **kwargs):
        try:
            # Buscar los registros de cursomateriaprofesoralumnos asociados al estudiante
            cursos_del_estudiante = request.env['oe.school.cursomateriaprofesoralumnos'].sudo().search([])

            # Procesar los cursos encontrados
            cursos_data = []
            for curso in cursos_del_estudiante:
                curso_data = {
                    'id': curso.id,
                    'name': curso.name,
                    'descripcion': curso.descripcion,
                    'curso_id': curso.curso_id.name,
                    'materia_id': curso.materia_id.name,
                    'teacher_id': curso.teacher_id.name,
                    'hora_inicio': curso.hora_inicio,
                    'hora_fin': curso.hora_fin,
                    'dia_semana': curso.dia_semana,
                }
                cursos_data.append(curso_data)

            # Devolver la respuesta JSON
            return request.make_response(json.dumps(cursos_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
        
        
        
        
class NotificacionController(http.Controller):
    
    @http.route('/odoo/estudiante/comunicados', auth='public', methods=['GET'], csrf=False)
    def obtener_lista_curso_materia(self, **kwargs):
        try:
            comunicados = request.env['oe.school.comunicados'].sudo().search([])

            comunicados_datas = []
            for comunicado in comunicados:
                
                curso_data = {
                    'id': comunicado.id,
                    'name': comunicado.name,
                    'descripcion': comunicado.descripcion,
                     
                }
                comunicados_datas.append(curso_data)

         # Devolver la respuesta JSON
            return request.make_response(json.dumps(comunicados_datas), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
        
        
        
        
        
        
        
        