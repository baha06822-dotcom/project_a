# stock/models.py
from django.db import models
from warehouse.models import Department, Warehouse


class CurrentStock(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="stocks",
        verbose_name="Подразделение",
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="stocks",
        verbose_name="Склад",
    )

    nomenclature_no = models.CharField("Номенкл №", max_length=32, db_index=True)
    bso = models.CharField("БСО", max_length=64, blank=True)

    name = models.CharField("Наименование", max_length=512, blank=True)
    uom = models.CharField("Ед. изм.", max_length=32, blank=True)

    qty = models.DecimalField("Количество", max_digits=18, decimal_places=3, null=True, blank=True)
    price = models.DecimalField("Цена", max_digits=18, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField("Сумма", max_digits=20, decimal_places=2, null=True, blank=True)

    date_in = models.DateField("Дата прихода на склад", null=True, blank=True)
    date_out = models.DateField("Дата расхода", null=True, blank=True)
    date_in_ngmk = models.DateField("Дата прихода в НГМК", null=True, blank=True)

    months_no_move = models.DecimalField(
        "Месяцев без движения",
        max_digits=6,
        decimal_places=1,
        null=True,
        blank=True,
    )

    loaded_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Остаток (текущий)"
        verbose_name_plural = "Остатки (текущие)"
        indexes = [
            models.Index(fields=["department", "warehouse"], name="idx_stock_dep_wh"),
            models.Index(fields=["nomenclature_no"], name="idx_stock_nom"),
            models.Index(fields=["months_no_move"], name="idx_stock_months"),
            models.Index(fields=["price"], name="idx_stock_price"),
            models.Index(fields=["amount"], name="idx_stock_amount"),
        ]

    def __str__(self):
        return f"{self.department.code} {self.warehouse.code} {self.nomenclature_no}"