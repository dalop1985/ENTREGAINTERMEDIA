from django.db import models

# Create your models here.
class Tios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    proveniente=models.CharField(max_length=10)
    edad=models.IntegerField()
    nacimiento=models.DateField()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.proveniente+" "+str(self.edad)+" "+str(self.nacimiento)

class Hermanos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+str(self.nacimiento)


class Primos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+str(self.nacimiento)


class Viven(models.Model):
    ciudad=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)

    def __str__(self):
        return self.ciudad+" "+self.estado

class Trabajo(models.Model):
    profesion=models.CharField(max_length=50)
    titulo=models.CharField(max_length=30)
    mail=models.EmailField()
    activo=models.BooleanField()

    def __str__(self):
        return self.profesion+" "+self.titulo+" "+self.mail+" "+str(self.activo)


