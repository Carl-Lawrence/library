{
    "name": "Library Extensions",
    "version": "1.0.0",
    "category": "Library",
    "summary": "Extensions for the library module: author and categories",
    "description": "Adds author (res.partner) to books and a book category model + views + menu.",
    "depends": ["library"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_category_views.xml",
        "views/library_book_views.xml",
        "views/library_menus.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
