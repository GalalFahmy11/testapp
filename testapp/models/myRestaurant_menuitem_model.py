# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TestApp(models.Model):
    _name = 'my.app'
    _description = 'hello world'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    value1 = fields.Float(default=30)
    value2 = fields.Float()
    description = fields.Text(default="Enter the Description")
    true_false = fields.Boolean()
    html = fields.Html()
    date = fields.Date()
    date_time = fields.Datetime(string='this is date and time')
    binary = fields.Binary()
    selection = fields.Selection([('1', 'one'), ('2', 'two')], default='1')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
    ], string='Status', default='draft', tracking=True)

    def action_send_email(self):
        self.state = 'sent'
    def action_confirm(self):
        self.state = 'sale'
    def action_reset(self):
        self.state = 'draft'

    _sql_constraints = [
        ('unique_name_constraint', 'unique(name)', 'The name must be unique. Please choose a different name.')
    ]

    # price = fields.Integer(string="Price")
    # quantity = fields.Integer(string="Quantity")
    # subtotal = fields.Integer(string="Subtotal", compute='_compute_subtotal')
    # tax = fields.Float(string="Tax Amount", compute='_compute_tax')
    # total_with_tax = fields.Float(string="Total with Tax", compute='_compute_total_with_tax')
    # discount = fields.Float(string='Discount Amount', compute='_compute_discount')
    # total_after_disc = fields.Float(string='Total After Discount', compute='_compute_total_after_disc')
    #
    #
    # @api.depends('price', 'quantity')
    # def _compute_subtotal(self):
    #     for record in self:
    #         # حساب المبلغ الكلي بدون ضريبه
    #         record.subtotal = record.price * record.quantity
    #
    # @api.depends('subtotal')
    # def _compute_tax(self):
    #     tax_rate = 0.14  # نسبة الضريبة
    #     for record in self:
    #         # حساب مبلغ الضريبة
    #         record.tax = record.subtotal * tax_rate

    # @api.depends('subtotal', 'tax')
    # def _compute_total_with_tax(self):
    #     for record in self:
    #         # حساب المبلغ الكلي + مبلغ الضريبه
    #         record.total_with_tax = record.subtotal + record.tax
    #
    # @api.depends('total_with_tax')
    # def _compute_discount(self):
    #     discount_rate = 10  # نسبة الخصم 10%
    #     for record in self:
    #         # حساب مبلغ الخصم بناءً على total_with_tax
    #         record.discount = record.total_with_tax * (discount_rate / 100)
    #
    # @api.depends('total_with_tax', 'discount')
    # def _compute_total_after_disc(self):
    #     for record in self:
    #         # حساب المجموع بعد الخصم
    #         record.total_after_disc = record.total_with_tax - record.discount
    #

    price = fields.Integer(string="Price",tracking=True)
    quantity = fields.Integer(string="Quantity",tracking=True)
    subtotal = fields.Integer(string="Subtotal", compute='_compute_totals')
    tax = fields.Float(string="Tax Amount", compute='_compute_totals', store=True)
    total_with_tax = fields.Float(string="Total with Tax", compute='_compute_totals')
    discount = fields.Float(string='Discount Amount', compute='_compute_totals', store=True)
    total_after_disc = fields.Float(string='Total After Discount', compute='_compute_totals')


    @api.depends('price', 'quantity')
    def _compute_totals(self):
        tax_rate = 0.14  # نسبة الضريبة
        discount_rate = 0.10  # نسبة الخصم

        for record in self:
            # حساب المبلغ الكلي بدون ضريبة
            record.subtotal = record.price * record.quantity

            # حساب مبلغ الضريبة
            record.tax = record.subtotal * tax_rate

            # حساب المبلغ الكلي بعد الضريبة
            record.total_with_tax = record.subtotal + record.tax

            # حساب الخصم
            record.discount = record.total_with_tax * discount_rate

            # حساب المجموع بعد الخصم
            record.total_after_disc = record.total_with_tax - record.discount


