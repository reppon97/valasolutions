from django.db import models


# Company model that contains only "name" field
class Company(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ("-pk",)

    def __str__(self):
        return self.name


# Person model linked to our company model
class Person(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    class Meta:
        ordering = ("-pk",)
        verbose_name_plural = "Persons"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
