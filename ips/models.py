from django.db import models
from supplier.models import Brand


class IpsSeries(models.Model):
    brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.PROTECT)
    name = models.CharField('Название', max_length=200, unique=True)
    image = models.ImageField('Картинка', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return str(f'{self.brand} {self.name}')

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
        ordering = ('brand', 'name')
