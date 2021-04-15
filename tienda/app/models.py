from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre= models.CharField(max_length=80, null= True)

    def __str__(self):         
        return str(self.nombre)


class Producto(models.Model):
    nombre = models.TextField(null=True)
    precio=models.IntegerField(null=True)
    imgPro1 = models.ImageField(upload_to='static/img')
    imgPro2 = models.ImageField(upload_to='static/img')
    imgPro3  = models.ImageField(upload_to='static/img')
    imgPro4  = models.ImageField(upload_to='static/img')
    imgPro5  = models.ImageField(upload_to='static/img')
    categoria = models.ForeignKey(Categoria, related_name="especialidad",on_delete=models.CASCADE, max_length=80, null= True )
    descripcion = models.TextField(max_length=10000,null=True)
    destacados = models.BooleanField(default=False)
    nuevos = models.BooleanField(default=False)
    algunos = models.BooleanField(default=False)



    def __str__(self):         
        return str(self.nombre)
