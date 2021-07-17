import builtins
from django.db import models
from django.db.models.deletion import DO_NOTHING


class Unit(models.Model):
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name='Широта')
    lon = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name='Долгота')

    n_mt = models.IntegerField(verbose_name='Идентификатор в MT', unique=True)

    class District(models.TextChoices):
        Заводской = 'Заводской район'
        Центральный = 'Центральный район'
        Куйбышевский = 'Куйбышевский район'
        Новоильинский = 'Новоильинский раон'
        Орджоникидзевский = 'Орджоникидзевский район'
        Кузнецкий = 'Кузнецкий район'
        Алексеевка = 'Алексеевка'
        Анисимово = 'Анисимово'
        Апанас = 'Апанас'
        Атаманово = 'Атаманово'
        Баевка = 'Баевка'
        Бардина = 'Бардина'
        Бедарево = 'Бедарево'
        Безруково = 'Безруково'
        Бенжереп_1 = 'Бенжереп 1-й'
        Березово = 'Березово'
        Боровково = 'Боровково'
        Букино = 'Букино'
        Верхний_Калтан = 'Верхний Калтан'
        Веселый = 'Веселый'
        Гавлировка = 'Гавриловка'
        Елань = 'Елань'
        Ерунаково = 'Ерунаково'
        Есаулка = 'Есаулка'
        Звгорский = 'Загорский'
        Зеленый_Луг = 'Зеленый Луг'
        Иганино = 'Иганино'
        Ильинка = 'Ильинка'
        Казанково = 'Казанково'
        Калтан = 'Калтан'
        Керегешь = 'Керегешь'
        Ключи = 'Ключи'
        Костенково = 'Костенково'
        Красинск = 'Красинск'
        Красная_Орловка = 'Красная Орловка'
        Красулино = 'Красулино'
        Кругленькое = 'Кругленькое'
        Крутая = 'Крутая'
        Кузедеево = 'Кузедеево'
        Кульчаны = 'Кульчаны'
        Куртуково = 'Куртуково'
        Лыс = 'Лыс'
        Малиновка = 'Малиновка'
        Малышев_лог = 'Малышев лог'
        Металлургов = 'Металлургов'
        Мир = 'Мир'
        Митино = 'Митино'
        Михайловка = 'Михайловка'
        Мостовая = 'Мостовая'
        Мунай = 'Мунай'
        Недорезово = 'Недорезово'
        Осинники = 'Осинники'
        Осиновое_Плесо = 'Осиновое Плесо'
        Подгорный = 'Подгорный'
        Подкорчияк = 'Подкорчияк'
        Постоянный = 'Постоянный'
        Пушкино = 'Пушкино'
        Рассвет = 'Рассвет'
        Сарбала = 'Сарбала'
        Сары_Чумыш = 'Сары-Чумыш'
        Северный = 'Северный'
        Сметанино = 'Сметанино'
        Сосновка = 'Сосновка'
        Староабашево = 'Староабашево'
        Степной = 'Степной'
        Тайлеп = 'Тайлеп'
        Тальжино = 'Тальжино'
        Таргай = 'Таргай'
        Таргайский_Дом_Отдыха = 'Таргайский Дом Отдыха'
        Терехино = 'Терехино'
        Увал = 'Увал'
        Усково = 'Усково'
        Успенка = 'Успенка'
        Усть_Аскарлы = 'Усть-Аскарлы'
        Федоровка = 'Федоровка'
        Черемза = 'Черемза'
        Черный_Калтан = 'Черный Калтан'
        Чистая_Грива = 'Чистая Грива'
        Чистогорский = 'Чистогорский'
        Чичербаево = 'Чичербаево'
        Шорохово = 'Шорохово'
        Шушталеп = 'Шушталеп'
        Южный = 'Южный'
        
        __empty__ = "Выберите район"

    district = models.CharField(choices=District.choices, default=District.__empty__, null=True, verbose_name='Район города', max_length=100)
    
    address = models.CharField(verbose_name='Адрес', max_length=200, blank=True, null=True)   
  

    def __str__(self):
        return str(self.address) + " | " + "#" + str(self.n_mt)

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

       




