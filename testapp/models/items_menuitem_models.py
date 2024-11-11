from odoo import models, fields, api


class MainDishes(models.Model):
    _name = 'my.main.dishes'
    name = fields.Char(string="Dish Name")  # اسم الطبق
    Completed_orders = fields.Many2one('my.completed.order', string='Completed_orders')
    description = fields.Text(string="Description")  # وصف الطبق
    price = fields.Float(string="Price")  # سعر الطبق
    size = fields.Selection([('small', 'Small'), ('medium', 'Medium'),
                             ('large', 'Large')], string="Size")  # حجم الطبق
    preparation_time = fields.Integer(string="Preparation Time (mins)")  # وقت التحضير بالدقائق
    is_spicy = fields.Boolean(string="Is Spicy")  # هل الطبق حار
    available = fields.Boolean(string="Available", default=True)  # هل الطبق متوفر
    image = fields.Binary(string="Image")  # صورة الطبق


class Drinks(models.Model):
    _name = 'my.drinks'
    name = fields.Char(string="Drink Name")  # اسم المشروب
    description = fields.Text(string="Description")  # وصف المشروب
    price = fields.Float(string="Price")  # سعر المشروب
    size = fields.Selection([('small', 'Small'), ('medium', 'Medium'),
                             ('large', 'Large')], string="Size")  # حجم المشروب
    is_alcoholic = fields.Boolean(string="Is Alcoholic")  # هل المشروب كحولي
    available = fields.Boolean(string="Available", default=True)  # هل المشروب متوفر
    image = fields.Binary(string="Image")  # صورة المشروب


class Desserts(models.Model):
    _name = 'my.desserts'
    name = fields.Char(string="Dessert Name")  # اسم الحلوى
    description = fields.Text(string="Description")  # وصف الحلوى
    price = fields.Float(string="Price")  # سعر الحلوى
    size = fields.Selection([('single', 'Single'), ('family', 'Family')], string="Size")  # حجم الحلوى
    ingredients = fields.Text(string="Ingredients")  # مكونات الحلوى
    is_vegan = fields.Boolean(string="Is Vegan")  # هل الحلوى نباتية
    available = fields.Boolean(string="Available", default=True)  # هل الحلوى متوفرة
    image = fields.Binary(string="Image")  # صورة الحلوى