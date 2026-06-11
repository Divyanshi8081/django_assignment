class ProductsRouter:
    """
    Routes all database operations for the 'products' app
    to the 'products_db' database.
    Everything else goes to 'default' (users app).
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'products':
            return 'products_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'products':
            return 'products_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'products':
            return db == 'products_db'
        return db == 'default'
