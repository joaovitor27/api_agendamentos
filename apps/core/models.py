from django.db import models


class Reservation(models.Model):
    work_stations = models.CharField('Estação de Trabalho', max_length=200)
    employee_name = models.CharField('Funcionário', max_length=150)
    shift = models.CharField('Turno', max_length=20)
    appointment_date = models.DateTimeField('Agendamento', default='%d/%m/%Y %H:%M:%S')
    created = models.DateTimeField('Data de criação', auto_now_add=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['created']

    def __str__(self):
        return self.appointment_date


class Workstations(models.Model):
    work_stations = models.CharField('Estação de Trabalho', max_length=200)

    class Meta:
        verbose_name = 'Estação de Trabalho'
        verbose_name_plural = 'Estações de Trabalho'
        ordering = ['work_stations']

    def __str__(self):
        return self.work_stations
