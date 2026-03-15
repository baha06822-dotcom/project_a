from django.db import models


class Department(models.Model):
    code = models.CharField("Код подразделения", max_length=50, unique=True)
    name = models.CharField("Название подразделения", max_length=255)
    is_active = models.BooleanField("Активно", default=True)

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        # ✅ показываем только название, без кода
        return self.name


class Warehouse(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="warehouses",
        verbose_name="Подразделение",
    )
    code = models.CharField("Код склада", max_length=50)
    name = models.CharField("Название", max_length=255)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
        constraints = [
            models.UniqueConstraint(
                fields=["department", "code"],
                name="uniq_warehouse_department_code",
            )
        ]

    def __str__(self):
        # ✅ показываем только название, без кода
        return self.name