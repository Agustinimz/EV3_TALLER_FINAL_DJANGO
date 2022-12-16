from serialApp.models import Reserva
from django import forms

class FormReserva(forms.ModelForm):
    
    nombre = forms.CharField(min_length=5, max_length=20)
    telefono = forms.CharField(min_length=9, max_length=9)
    fecha = forms.DateField(label='Fecha Inscripcion', widget= forms.SelectDateWidget)
    Horas = [
             ('08:00', '08:00'),('08:30', '08:30'),
             ('09:00', '09:00'),('09:30', '09:30'),
             ('10:00', '10:00'),('10:30', '10:30'),
             ('11:00', '11:00'),('11:30', '11:30'),
             ('12:00', '12:00'),('12:30', '12:30'),
             ('13:00', '13:00'),('13:30', '13:30'),
             ('14:00', '14:00'),('14:30', '14:30'),
             ('15:00', '15:00'),('15:30', '15:30'),
             ('16:00', '16:00'),('16:30', '16:30'),
             ('17:00', '17:00'),('17:30', '17:30'),
             ('14:00', '14:00'),('14:30', '14:30'),
             ('15:00', '15:00'),('15:30', '15:30'),
             ('16:00', '16:00'),('16:30', '16:30'),
             ('17:00', '17:00'),('17:30', '17:30'),
             ('18:00', '18:00'),('18:30', '18:30'),
             ('19:00', '19:00'),('19:30', '19:30'),
             ('20:00', '20:00'),('20:30', '20:30'),
             ('21:00', '21:00'),('21:30', '21:30'),
             ('22:00', '22:00'),('22:30', '22:30'),
             ('23:00', '23:00'),('23:30', '23:30')] 
    hora = forms.TimeField(label= 'Hora Inscripcion',widget=forms.Select(choices=Horas))
    Estados = [('completada', 'COMPLETADA'),('reservado', 'RESERVADO'),('anulada', 'ANULADA'),('no asisten', 'NO ASISTEN')] 
    estado = forms.CharField(widget=forms.Select(choices=Estados))
    observacion = forms.CharField(required=False)
    
    
    
    
    class Meta:
        model = Reserva
        fields = '__all__'