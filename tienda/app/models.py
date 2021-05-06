from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre= models.CharField(max_length=80, null= True)

    def __str__(self):         
        return str(self.nombre)


class Producto(models.Model):
    nombre = models.TextField(null=True)
    precio = models.IntegerField(null=True)
    imagen1 = models.ImageField(upload_to='static/img')
    imagen2 = models.ImageField(upload_to='static/img')
    imagen3  = models.ImageField(upload_to='static/img')
    imagen4  = models.ImageField(upload_to='static/img')
    imagen5  = models.ImageField(upload_to='static/img')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, max_length=80, null= True )
    descripcion = models.TextField(max_length=10000,null=True)
    destacados = models.BooleanField(default=False)
    nuevos = models.BooleanField(default=False)
    algunos = models.BooleanField(default=False)
    portada = models.BooleanField(default=False)




    def __str__(self):         
        return str(self.nombre)
