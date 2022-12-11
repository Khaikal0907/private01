# -*- coding: utf-8 -*-
# from odoo import http


# class KhaikalAcademy(http.Controller):
#     @http.route('/khaikal_academy/khaikal_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/khaikal_academy/khaikal_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('khaikal_academy.listing', {
#             'root': '/khaikal_academy/khaikal_academy',
#             'objects': http.request.env['khaikal_academy.khaikal_academy'].search([]),
#         })

#     @http.route('/khaikal_academy/khaikal_academy/objects/<model("khaikal_academy.khaikal_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('khaikal_academy.object', {
#             'object': obj
#         })
