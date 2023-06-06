from django.shortcuts import render,HttpResponse
from appORM.models import *
from django.http import JsonResponse
from django.db.models import Q,Sum, Max, Count, Avg
import matplotlib.pyplot as plt
import numpy as np
import os
from django.conf import settings


# Create your views here.
#consultas a realizar
#1. Cantidad de productos vendidos por Categoria

def consultas(request):
    resultado=Categoria.objects.all().values()

    return HttpResponse(resultado)


#2. Valor total de venta por producto
#3. Valor total de Venta por Categoria
#4. Promedio de Ventas por mes
#5. Máximo valor de una venta
#6. Minimo valor de una venta
#7. Cantidad mayor de un producto vendido

def grafica1(request):
    meses = np.array(["Enero","Febrero","Marzo"])
    ventas = np.array(["1500000","2000000","3000000"])

    plt.title("Ventas primer mes")
    plt.xlabel("Meses")
    plt.ylabel("Valor Ventas")

    plt.bar(meses,ventas)

    rutaImagen = os.path.join(settings.MEDIA_ROOT+"\\"+"grafica.png")

    plt.savefig(rutaImagen)

    return render(request,"graficas.html")

def grafica2(request):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]

    consulta = DetalleVenta.objects.values('detVenta__venFecha__month')\
    .annotate(TotalVentasMes=Sum('detValorDetalle'))

    xMeses=[]
    yVentas=[]
    for datos in consulta:
        mes=datos['detVenta__venFecha__month']
        xMeses.append(meses[mes-1])
        yVentas.append(datos['TotalVentasMes'])


    plt.title("Ventas totales por mes")
    plt.xlabel("Meses")
    plt.ylabel("Valor Ventas")
    
    plt.bar(xMeses,yVentas)
    rutaImagen = os.path.join(settings.MEDIA_ROOT+"\\"+"grafica.png")
    plt.savefig(rutaImagen)
    return render(request,"graficas.html")

def graficaTotalVentaDeLaSemana(request):
        dias = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
        
        consulta = DetalleVenta.objects.values('detVenta__venFecha__week_day'). \
        annotate(TotalVentasPorDiaSemana=Sum('detValorDetalle'))    
        
        consultaCa = DetalleVenta.objects.values('detProducto__proCategoria__catNombre'). \
        annotate(TotalVentasPorCategorias=Sum('detValorDetalle'))

        xDias=[]
        yVentas=[]
        for datos in consulta:
            yVentas.append(datos['TotalVentasPorDiaSemana'])
            dia=datos['detVenta__venFecha__week_day']
            xDias.append(dias[dia-1])
            
        
        plt.title("Ventas totales por dia de la semana")
        
        plt.subplot(2,1,1)
        plt.pie(yVentas, labels = xDias)
        
        xCategorias = []
        yVentasCategorias = []
        
        for datos in consultaCa:
            xCategorias.append(datos['detProducto__proCategoria__catNombre'])
            yVentasCategorias.append(datos['TotalVentasPorCategorias'])
        
        plt.subplot(2,1,2)
        plt.bar(xCategorias, yVentasCategorias)
        plt.title("Total Ventas Por Categoria")
        plt.ylabel("Total Ventas")
        
        
        
        rutaImagen = os.path.join(settings.MEDIA_ROOT+"\\"+"grafica.png")
        plt.savefig(rutaImagen)
        return render(request,"graficas.html")
    
def graficaGoogle(request):
    return render(request,"googleGrafica.html")

def grafica1Google(request):
    
    ventasProducto = DetalleVenta.objects.values('detProducto__proNombre').\
    annotate(TotalVentaProducto=Sum('detDetalleVenta'))
    
    listaDatos = []
    listaDatos.append('Producto', 'ValorVenta')
    
    for datos in ventasProducto:
        listaDatos.append([datos['detProducto__proNombre'], datos['TotalVentaProducto']])
    retorno = {'datos': listaDatos}
    
    return JsonResponse(retorno)