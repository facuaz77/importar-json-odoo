# -*- coding: utf-8 -*-
# from odoo import http


# class Colombofiliatest(http.Controller):
#     @http.route('/colombofiliatest/colombofiliatest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/colombofiliatest/colombofiliatest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('colombofiliatest.listing', {
#             'root': '/colombofiliatest/colombofiliatest',
#             'objects': http.request.env['colombofiliatest.colombofiliatest'].search([]),
#         })

#     @http.route('/colombofiliatest/colombofiliatest/objects/<model("colombofiliatest.colombofiliatest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('colombofiliatest.object', {
#             'object': obj
#         })
