class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label=='inv':
            return 'db_inv'
        return 'default'
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label=='inv':
            return 'db_inv'
        return 'default'
    
    
    def allow_relation(self, elem1, elem2, **hints):
        #if elem1.app_label == 'app1' and
        #   elem2.app_label == 'inv:
        #   return True
        return True
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True