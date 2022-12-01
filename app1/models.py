from datetime import date
from django.db import models
from django.utils.text import slugify

# Create your models here.

class ModeloAuditoria(models.Model):
    fecha_crea = models.DateTimeField(auto_now_add=True) #editable false, blak True
    fecha_modifica = models.DateTimeField(auto_now=True) #Cuado se modifique se auto actualiza
    
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_OPCIONES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices=ESTADO_OPCIONES,
        default=ACTIVO
    )
    
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True
        

class Categoria(ModeloAuditoria):
    descripcion = models.CharField(
        max_length=50,
        unique=True
    )
    
    
    def __str__(self):
        return self.descripcion
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
        
    class Meta:
        verbose_name_plural = 'Categorias'
        

class Persona(ModeloAuditoria):
    nombre = models.CharField(
        max_length = 50
    )
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=False, blank=False)
   
   
    @property 
    def edad(self):
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - \
            ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age
    
    @property #con property podemos agregar una operacion que se quiera hacer sin afectar la bd
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    def save(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        super(Persona, self).save()
        
    class Meta:
        verbose_name_plural = "Personas"
        

class Animal(ModeloAuditoria):
    nombre = models.CharField(max_length=10)
    pata = models.IntegerField(default=2)
    
    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Animal, self).save()
    
    class Meta:
        verbose_name_plural = "Animales"
        

class Libros(ModeloAuditoria):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField(
        default=1,
        help_text='En Dolares'
    )
    peso = models.PositiveIntegerField(
        help_text='En kg'
    )
    
    TIPOS = (
        ('VIRTUAL', 'virtual'), 
        ('FISICO', 'fisico')
    )
    tipo = models.CharField(
        max_length=10, 
        choices=TIPOS,
        default='FISICO'
    )
    
    url_download = models.URLField(default=None)
    
    
    def __str__(self):
        return f'{self.nombre} {self.tipo}'
    
    
    def save(self):
        self.nombre = self.nombre.upper()
        return super(Libros, self).save()
    
    
    class Meta:
        verbose_name_plural = 'Libros'
        """
        unique_together agrega un constrin, que permite definir un unique perzonalisado, en este ejemplo
        No pueden aber 2 registros con el mismo nombre y tipo
        """
        unique_together = ('nombre', 'tipo') 
        

class Progenitor(ModeloAuditoria):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    padre = models.CharField(max_length=50)
    madre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.persona} - {self.padre} - {self.madre}'
    
    class Meta:
        verbose_name_plural = 'Progenitores'
        

class Padre(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}'
    

class Hijo(models.Model):
    padre = models.ForeignKey(Padre, on_delete=models.PROTECT) #? PROTECT evita que se elimne el padre si hay hijos
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} hijo de {self.padre}'
    
# SLUG REVISAR MAS A FONDO NO QUEDO CLARO
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, default='')
    
    def __str__(self):
        return f'{self.titulo}'
    
    def save(self):
        self.slug = slugify(self.titulo)
        super(Publicacion, self).save()

class Articulo(models.Model):
    titular = models.CharField(max_length=100)
    publicaciones = models.ManyToManyField(Publicacion)
    
    def __str__(self):
        return f'{self.titular}'
    
"""
Nota de los Many to Many

desde articulo puedo acceder a todas las publicaciones relacionadas con

articulo.publicaciones.all()
y puedo agregar mas con  add(), quitar con remove() o limpiar con clear()


Pero para acceder de manera inversa, y saber todas las los articulos que tienen ligada una publicacion
En otras palabras, desde publicacion saber que articulos tiene relacion con el
en este caso se usa

el nombre del modelo en minscula segido de un _set

publicacion.articulo_set.all()

y desde aqui tambien se pueden agregar relaciones
"""

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    supervisor = models.ForeignKey(
        'self',  #Colocando self se puede hacer una llave foranea a si misma
        null=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return self.nombre


class Employe(models.Model):
    nombre = models.CharField(max_length=100)
    supervisor = models.ForeignKey(
        'app1.Employe',  #Es  otra manera de referenciar asi mismo
        null=True,
        on_delete=models.DO_NOTHING
    )
    
    def __str__(self):
        return self.nombre
    
hola = models.BooleanField()
Edad = models.IntegerField()
asdfa = models.DateTimeField(auto_now=False, auto_now_add=False)


#Acceder a una vista que se cree en la bd directamente (NO SE CREA EN DJANGO)
# select ap.id as idpadre, ap.nombre as nombrepadre, ah.id as idhijo, ah.nombre as nombrehijo from  app1_padre  ap inner join app1_hijo ah on ap.id = ah.padre_id
class ViewPadreHijo(models.Model):
    idpadre = models.IntegerField(primary_key=True)
    nombrepadre = models.CharField(max_length=50)
    idhijo = models.IntegerField()
    nombrehijo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombrepadre} -> {self.nombrehijo}'
    
    class Meta:
        managed = False
        db_table = "view_padrehijo"
        

# Personalizar nombre de la tabla que se crea en Django
class NuevoNombre(models.Model):
    nombre = models.CharField(max_length=50)
    a = models.CharField(
        max_length=50,
        db_column="otro_nombre", #Con esto se puede especificar el nombre que queremos que tebnga en la bd
        default=""
        )
        
    class Meta:
        db_table = "nuevo_nombre"


#null=True permite que se cree en null
#blank=True Especifica que en el formulario no es necesario