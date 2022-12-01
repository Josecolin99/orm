# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App1Animal(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_crea = models.DateTimeField()
    fecha_modifica = models.DateTimeField()
    estado = models.CharField(max_length=8)
    activo = models.BooleanField()
    nombre = models.CharField(max_length=10)
    pata = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_animal'


class App1Articulo(models.Model):
    id = models.BigAutoField(primary_key=True)
    titular = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app1_articulo'


class App1ArticuloPublicaciones(models.Model):
    id = models.BigAutoField(primary_key=True)
    articulo = models.ForeignKey(App1Articulo, models.DO_NOTHING)
    publicacion = models.ForeignKey('App1Publicacion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_articulo_publicaciones'
        unique_together = (('articulo', 'publicacion'),)


class App1Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)
    activo = models.BooleanField()
    fecha_crea = models.DateTimeField()
    fecha_modifica = models.DateTimeField()
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'app1_categoria'


class App1Empleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app1_empleado'


class App1Employe(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app1_employe'


class App1Hijo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    padre = models.ForeignKey('App1Padre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_hijo'


class App1Libros(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_crea = models.DateTimeField()
    fecha_modifica = models.DateTimeField()
    estado = models.CharField(max_length=8)
    activo = models.BooleanField()
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    peso = models.IntegerField()
    tipo = models.CharField(max_length=10)
    url_download = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'app1_libros'
        unique_together = (('nombre', 'tipo'),)


class App1Padre(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'app1_padre'


class App1Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_crea = models.DateTimeField()
    fecha_modifica = models.DateTimeField()
    estado = models.CharField(max_length=8)
    activo = models.BooleanField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    class Meta:
        managed = False
        db_table = 'app1_persona'


class App1Progenitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_crea = models.DateTimeField()
    fecha_modifica = models.DateTimeField()
    estado = models.CharField(max_length=8)
    activo = models.BooleanField()
    padre = models.CharField(max_length=50)
    madre = models.CharField(max_length=50)
    persona = models.OneToOneField(App1Persona, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_progenitor'


class App1Publicacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'app1_publicacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
