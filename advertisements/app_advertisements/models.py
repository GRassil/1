from django.db import models

class Advertisements(models.Model):
    class Meta:
        db_table = 'advertisements'

    title = models.CharField('Заголовок',max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text="Отметьте если будет уместен торг")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now=True)

    def __str__(self):
        text = f'id = {self.pk} title = {self.title}, price = {float(self.price)}'
        return "%s object (%s)" % (self.__class__.__name__, text)