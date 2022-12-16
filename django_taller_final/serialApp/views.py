from django.shortcuts import render, redirect
from .serialiazers import ReservaSerializer
from .models import Reserva
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from serialApp.forms import FormReserva

# Create your views here.
def index(request):
    return render(request,'index.html')

def listaReservas(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reserva.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
    res = Reserva.objects.get(id = id)
    res.delete()
    return redirect('/reserva')

def actualizarReserva(request, id):
    res = Reserva.objects.get(id = id)
    form = FormReserva(instance=res)
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=res)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarReserva.html', data)


class ListaInscrito(APIView):
    def get(self, request):
        res = Reserva.objects.all()
        serial = ReservaSerializer(res, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = ReservaSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetalleInscrito(APIView):
    def get_object(self, pk, institucion):
        try:
            return Reserva.objects.get(id=pk)
        except Reserva.DoesNotExist:
            return Http404

    def get(self, request, pk):
        res = self.get_object(pk)
        
        serial = ReservaSerializer(res)
        return Response(serial.data)

    def put(self, request, pk):
        res = self.get_object(pk)
        serial = ReservaSerializer(res, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        res = self.get_object(pk)
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
