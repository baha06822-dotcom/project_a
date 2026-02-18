from django.db import models


class Part(models.Model):
    number = models.PositiveIntegerField("№ п/п")

    catalog_number = models.CharField("Каталожный №", max_length=100)
    nom_number = models.CharField("Номенклатурный №", max_length=100)

    name = models.CharField("Наименование", max_length=255)

    price = models.DecimalField("Цена", max_digits=12, decimal_places=2, null=True, blank=True)

    brand = models.CharField("Марка", max_length=100, blank=True)
    model = models.CharField("Модель", max_length=100, blank=True)
    unit = models.CharField("Узел", max_length=100, blank=True)

    months_without_movement = models.IntegerField("Месяцев без движения", default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["number"]
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"

    def __str__(self):
        return f"{self.number}. {self.name} ({self.catalog_number})"
