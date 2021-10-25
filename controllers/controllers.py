# -*- coding: utf-8 -*-
# from odoo import http


# class Jiaz(http.Controller):
#     @http.route('/jiaz/jiaz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jiaz/jiaz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jiaz.listing', {
#             'root': '/jiaz/jiaz',
#             'objects': http.request.env['jiaz.jiaz'].search([]),
#         })

#     @http.route('/jiaz/jiaz/objects/<model("jiaz.jiaz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jiaz.object', {
#             'object': obj
#         })
