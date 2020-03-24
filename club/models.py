from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class vd_event(models.Model):
    i_days = (('Нет', 'Нет'), ('Да', 'Да'), )
    i_status = (('Проведено', 'Проведено'), ('Дата утверждена', 'Дата утверждена'), ('В разработке', 'В разработке'),)
    i_level = (('Новичок', 'Новичок'), ('Приключенческий', 'Приключенческий'), ('Профи', 'Профи'), (' - ', ' - '),)
    i_type = (('Авто', 'Авто'), ('Английский', 'Английский'), ('Вело', 'Вело'), ('Вечернее', 'Вечернее'), ('Водное', 'Водное'),
        ('ГК', 'ГК'), ('Игры', 'Игры'), ('Комбо', 'Комбо'), ('Коньки', 'Коньки'), ('Лыжи', 'Лыжи'), ('НГ', 'НГ'),
        ('Пешее', 'Пешее'), ('Психолог', 'Психолог'), ('Ролики', 'Ролики'), ('Хоккей', 'Хоккей'), ('ЧГК', 'ЧГК'), ('Эко', 'Эко'),)  
    event_name = models.CharField('Мероприятие', max_length = 255)
    status = models.CharField('Статус', max_length = 25, choices = i_status)
    many_days = models.CharField('Многодневное', max_length = 3, choices = i_days)
    data_plan = models.DateTimeField('Плановая дата', default = timezone.now)
    data_begin = models.DateField('Дата начала', blank = True)
    data_end = models.DateField('Дата окончания', blank = True)
    event_type = models.CharField('Тип мероприятия', max_length = 25, choices =i_type)
    vk_link = models.URLField('Ссылка в vk', blank = True, max_length = 100)
    level = models.CharField('Уровень сложности', max_length = 25, choices = i_level)
    country = models.CharField('Направление', max_length = 50, blank = True, default = ' ')
    comment = models.TextField('Комментарии', blank = True) 


    class Meta:
        verbose_name='Мероприятие'
        ordering = ['-data_plan']
        verbose_name_plural='Мероприятия'

    def __str__(self):
        return self.event_name
    def __unicode__(self):
        return self.event_name


class vd_user_profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    i_role = (('Администратор', 'Администратор'), ('Организатор', 'Организатор'), ('Участник', 'Участник'),)
    last_name = models.CharField('Фамилия', max_length = 100, db_index = True, default = ' ')
    first_name = models.CharField('Имя', max_length = 100, default = ' ')
    middle_name = models.CharField('Отчество', max_length = 100,blank=True, default = ' ')
    role = models.CharField('Роль', max_length = 25, choices = i_role)
    comment = models.CharField('Комментарий',blank=True, max_length = 255, default = ' ')

    class Meta:
        verbose_name='Участник'
        ordering = ['role']
        verbose_name_plural='Участники'

    def __str__(self):
       return " %s  %s  %s " % (self.last_name, self.first_name, self.middle_name)
        
    def __unicode__(self):
        return " %s  %s  %s " % (self.last_name, self.first_name, self.middle_name)


class vd_information_type(models.Model):
    inf_name = models.CharField('Тип информации', max_length = 254, default = ' ')
    is_primary = models.BooleanField('Обязательное поле', default = True)
    
    class Meta:
        verbose_name='Тип информации'
        verbose_name_plural='Типы информации'
        ordering = ['id']

    def __str__(self):
        return self.inf_name
    def __unicode__(self): 
        return self.inf_name

class vd_user_information(models.Model):
    user = models.ForeignKey(vd_user_profile, null = True, on_delete = models.CASCADE, 
        verbose_name = 'Ф.И.О. участника', to_field = 'id')
    inf_type = models.ForeignKey(vd_information_type, null = True, on_delete = models.CASCADE, 
        verbose_name = 'Тип информации', to_field = 'id')
    inf_value = models.CharField('Информация', max_length = 254, default = ' ')
    
    class Meta:
        verbose_name='Информация об участнике'
        verbose_name_plural='Информация об участниках'
        ordering = ['inf_type', 'user']

    def __str__(self):
        return "Информация об участнике"
    def __unicode__(self):
        return "Информация об участнике"

class vd_participent_event(models.Model):
    participant_id=models.ForeignKey(vd_user_profile, null=True, on_delete = models.CASCADE,
    verbose_name = 'Ф.И.О. участника', to_field='id')
    event_id=models.ForeignKey(vd_event, null=True, on_delete=models.CASCADE, 
        verbose_name = 'Мероприятие', to_field='id' )
    
    class Meta:
        verbose_name='Участник мероприятия'
        verbose_name_plural='Участники мероприятий'
        ordering = ['event_id', 'participant_id']
        
    def __str__(self):
        return "Участник мероприятия"
    def __unicode__(self):
        return "Участник мероприятия"


class vd_organizer_event(models.Model):
    organizer_id=models.ForeignKey(vd_user_profile, null=True, on_delete = models.CASCADE,
    verbose_name = 'Ф.И.О. организатора', to_field='id')
    event_id=models.ForeignKey(vd_event, null=True, on_delete = models.CASCADE,
    verbose_name='Мероприятие', to_field='id')
    coeff=models.FloatField('Коэффициент')

    class Meta:
        verbose_name='Организатор мероприятия'
        verbose_name_plural='Организаторы мероприятий'
        ordering = ['event_id','organizer_id']

    def __str__(self):
            return "Организатор мероприятия %s " % self.event_id
    def __unicode__(self):
             return "Организатор мероприятия %s " % self.event_id
    
class vd_club_card(models.Model):
    i_state= (('in_use', 'in_use'), ('not_in_use', 'not_in_use'), ('hidden','hidden'))
    card_number=models.IntegerField('Номер карты', primary_key=True, max_length=10)
    state=models.CharField('Состояние', max_length=100, choices =i_state)
    user_id=models.ForeignKey(vd_user_profile, null=True, on_delete=models.SET_NULL,
    verbose_name = 'Ф.И.О.', to_field='id')
    price=models.IntegerField('Стоимость карты', max_length=10)
    place=models.CharField('Местонахождение карты',blank=True, max_length=255, default = ' ')
        
    class Meta:
        verbose_name='Клубная карта'
        verbose_name_plural='Клубные карты'
        ordering = ['card_number','state']
    def __str__(self):
            return "Клубная карта %s " % (self.card_number)
    def __unicode__(self):
             return "Клубная карта %s " % (self.card_number)

