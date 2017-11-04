# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models


class ProductBox(models.Model):
    _name = 'product.box'

    name = fields.Char('Box Name', required=True)
    description = fields.Text('Description')
    product_ids = fields.One2many(
        'product.template',
        'product_box_id',
        string='Box Products',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )
    cost = fields.Float('Cost')

    @api.one
    @api.depends('product_ids')
    def _get_products_count(self):
        self.products_count = len(self.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_box_id = fields.Many2one(
        'product.box',
        string='Box',
        help='Select a box for this product'
    )
