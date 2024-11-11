from odoo import models, fields, api


class NewOrder(models.Model):
    _name = 'my.new.order'
    name = fields.Char(string="Customer Name")
    order_number = fields.Integer()
    order_date = fields.Datetime(string="Order Date")  # تاريخ الطلب
    delivery_address = fields.Char(string="Delivery Address")  # عنوان التسليم
    contact_number = fields.Char(string="Contact Number")  # رقم الاتصال


class CompletedOrder(models.Model):
    _name = 'my.completed.order'
    name = fields.Char(string='Order Name')
    item = fields.One2many('my.main.dishes', 'Completed_orders')
    completion_date = fields.Datetime(string="Completion Date")  # تاريخ إكمال الطلب
    delivered_by = fields.Char(string="Delivered By")  # اسم الشخص الذي قام بتسليم الطلب
    total_amount = fields.Float(string="Total Amount")  # إجمالي المبلغ المدفوع


class CanceledOrder(models.Model):
    _name = 'my.canceled.order'
    name = fields.Char(string='Order Name')
    cancellation_date = fields.Datetime(string="Cancellation Date")  # تاريخ إلغاء الطلب
    canceled_by = fields.Char(string="Canceled By")  # اسم الشخص الذي قام بإلغاء الطلب (موظف أو عميل)
    is_refundable = fields.Boolean(string="Is Refundable", default=True)  # هل الطلب مسترد أم لا

