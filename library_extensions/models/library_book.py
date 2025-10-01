from odoo import models, fields

class LibraryBook(models.Model):
    _inherit = "library.book"

    # Task 2: add author_id
    author_id = fields.Many2one(
        comodel_name="res.partner",
        string="Author",
        required=True,
        ondelete="set null",
    )

    # Task 3: add category_id as Many2many (user requested field name category_id)
    category_id = fields.Many2many(
        comodel_name="library.book.category",
        relation="library_book_category_rel",
        column1="book_id",
        column2="category_id",
        string="Categories",
    )
