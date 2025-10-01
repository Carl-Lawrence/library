from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"
    _order = "name"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('library_book_category_name_uniq', 'unique(name)', 'The category name must be unique.'),
    ]
