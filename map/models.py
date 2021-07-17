import builtins
from django.db import models
from django.db.models.deletion import DO_NOTHING


class Unit(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта') 
    lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')

    n_mt = models.IntegerField(verbose_name='Идентификатор в MT', unique=True)
    
    class District(models.TextChoices):
        Заводской = 'Заводской'
        Центральный = 'Центральный'
        Куйбышевский = 'Куйбышевский'
        Новоильинский = 'Новоильинский'
        Орджоникидзевский = 'Орджоникидзевский'
        Кузнецкий = 'Кузнецкий'    

        __empty__ = "Выберите район"
        
    district = models.CharField(choices=District.choices, default=District.__empty__, null=True, verbose_name='Район города', max_length=100)
    street = models.CharField(verbose_name='Улица', max_length=100, blank=True, null=True)
    building = models.IntegerField(verbose_name='Номер дома', blank=True, null=True)
    corpus = models.CharField(verbose_name='Корпус', max_length=3, blank=True, null=True)

    def __str__(self):
        return str(self.street) + ", " + str(self.building) + "|" + "#" + str(self.n_mt)

    class Meta:
        verbose_name_plural = "Контейнерные площадки"
        verbose_name = "Контейнерная площадка"
        ordering = ['n_mt']

class Customer(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта') 
    lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')

    unit = models.ForeignKey(Unit, db_column="n_mt", on_delete=models.PROTECT, verbose_name='Контейнерная площадка', blank=True, null=True)

    class District(models.TextChoices):
        Заводской = 'Заводской'
        Центральный = 'Центральный'
        Куйбышевский = 'Куйбышевский'
        Новоильинский = 'Новоильинский'
        Орджоникидзевский = 'Орджоникидзевский'
        Кузнецкий = 'Кузнецкий'    

        __empty__ = "Выберите район"
        
    district = models.CharField(choices=District.choices, default=District.__empty__, null=True, verbose_name='Район города', max_length=100)
    street = models.CharField(verbose_name='Улица', max_length=100, blank=True, null=True)
    building = models.IntegerField(verbose_name='Номер дома', blank=True, null=True)
    corpus = models.CharField(verbose_name='Корпус', max_length=3, blank=True, null=True)

    def __str__(self):
        return str(str(self.district)+" "+str(self.street)+" "+str(self.building)+" "+str(self.corpus))

    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиенты"
        ordering = ['street']

       




