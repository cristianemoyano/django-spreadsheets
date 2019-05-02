from django.conf import settings
from django.db import models
from django.utils import timezone


class Autotest(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link_respuestas = models.CharField(max_length=200, default='')
    link_formulario = models.CharField(max_length=200, default='')
    observaciones = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Responses(models.Model):
    marca_temporal = models.DateTimeField(default=timezone.now)
    nombre_completo = models.CharField(max_length=200)
    dni = models.CharField(max_length=200, unique=True)
    uno_1 = models.BooleanField()
    uno_2 = models.BooleanField()
    uno_3 = models.BooleanField()
    uno_4 = models.BooleanField()
    uno_5 = models.BooleanField()
    uno_6 = models.BooleanField()
    uno_7 = models.BooleanField()
    uno_8 = models.BooleanField()
    uno_9 = models.BooleanField()
    uno_10 = models.BooleanField()

    dos_1 = models.BooleanField()
    dos_2 = models.BooleanField()
    dos_3 = models.BooleanField()
    dos_4 = models.BooleanField()
    dos_5 = models.BooleanField()
    dos_6 = models.BooleanField()
    dos_7 = models.BooleanField()
    dos_8 = models.BooleanField()
    dos_9 = models.BooleanField()
    dos_10 = models.BooleanField()

    tres_1 = models.BooleanField()
    tres_2 = models.BooleanField()
    tres_3 = models.BooleanField()
    tres_4 = models.BooleanField()
    tres_5 = models.BooleanField()
    tres_6 = models.BooleanField()
    tres_7 = models.BooleanField()
    tres_8 = models.BooleanField()
    tres_9 = models.BooleanField()
    tres_10 = models.BooleanField()

    cuatro_1 = models.BooleanField()
    cuatro_2 = models.BooleanField()
    cuatro_3 = models.BooleanField()
    cuatro_4 = models.BooleanField()
    cuatro_5 = models.BooleanField()
    cuatro_6 = models.BooleanField()
    cuatro_7 = models.BooleanField()
    cuatro_8 = models.BooleanField()
    cuatro_9 = models.BooleanField()
    cuatro_10 = models.BooleanField()

    cinco_1 = models.BooleanField()
    cinco_2 = models.BooleanField()
    cinco_3 = models.BooleanField()
    cinco_4 = models.BooleanField()
    cinco_5 = models.BooleanField()
    cinco_6 = models.BooleanField()
    cinco_7 = models.BooleanField()
    cinco_8 = models.BooleanField()
    cinco_9 = models.BooleanField()
    cinco_10 = models.BooleanField()

    seis_1 = models.BooleanField()
    seis_2 = models.BooleanField()
    seis_3 = models.BooleanField()
    seis_4 = models.BooleanField()
    seis_5 = models.BooleanField()
    seis_6 = models.BooleanField()
    seis_7 = models.BooleanField()
    seis_8 = models.BooleanField()
    seis_9 = models.BooleanField()
    seis_10 = models.BooleanField()

    siete_1 = models.BooleanField()
    siete_2 = models.BooleanField()
    siete_3 = models.BooleanField()
    siete_4 = models.BooleanField()
    siete_5 = models.BooleanField()
    siete_6 = models.BooleanField()
    siete_7 = models.BooleanField()
    siete_8 = models.BooleanField()
    siete_9 = models.BooleanField()
    siete_10 = models.BooleanField()

    ocho_1 = models.BooleanField()
    ocho_2 = models.BooleanField()
    ocho_3 = models.BooleanField()
    ocho_4 = models.BooleanField()
    ocho_5 = models.BooleanField()
    ocho_6 = models.BooleanField()
    ocho_7 = models.BooleanField()
    ocho_8 = models.BooleanField()
    ocho_9 = models.BooleanField()
    ocho_10 = models.BooleanField()

    key_max_first = models.CharField(max_length=200, default='')
    val_max_first = models.IntegerField(default=0)
    percent_max_first = models.CharField(max_length=200, default='')
    map_key_first = models.CharField(max_length=200, default='')

    key_max_second = models.CharField(max_length=200, default='')
    val_max_second = models.IntegerField(default=0)
    percent_max_second = models.CharField(max_length=200, default='')
    map_key_second = models.CharField(max_length=200, default='')

    observaciones = models.TextField()
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{id} - {name} - DNI: {dni} - 1ra: {i1} - {p1} - 2da: {i2} - {p2}'.format(
            id=self.pk,
            name=self.nombre_completo,
            dni=self.dni,
            i1=self.key_max_first,
            p1=self.percent_max_first,
            i2=self.key_max_second,
            p2=self.percent_max_second,
        )
