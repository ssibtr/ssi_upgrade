from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
import werkzeug
import json


class WebsiteSale(WebsiteSale):

    @http.route(['/api/test'], type='json', auth="public", methods=['GET'], website=True, multilang=False, csrf=False)
    def ssibtr_test_api(self,  **args):
        # input_data = request.httprequest.data
        # ref = json.loads(input_data.decode("utf-8"))['ref']
        data = {'message': 'Success'}
        # try:
        #     product = request.env['product.product'].sudo().search([('default_code', '=', ref.upper())], limit=1)
        #     if product:
        #         data = {'message': 'found', 'ref': ref.upper(), 'product': product.name}
        #     else:
        #         data = {'message': 'not found', 'ref': ref.upper()}
        # except Exception:
        #     pass
        return data
