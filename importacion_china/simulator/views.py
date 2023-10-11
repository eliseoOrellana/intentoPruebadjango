
# Create your views here.
from django.shortcuts import render
from .forms import SimulacionForm
from .models import Simulacion
from decimal import Decimal
from .models import HistorialConsulta# Importa el modelo HistorialConsulta--------borrar solo prueba de historial

def calcular_impuestos(datos):
    cantidad_unidades = datos['cantidad_unidades']
    costo_unitario_usd = Decimal(str(datos['costo_unitario_usd']))
    costo_envio_usd = Decimal(str(datos['costo_envio_usd']))
    tipo_de_cambio = Decimal('890')

    # Calcular el valor CIF en USD
    valor_cif_usd = cantidad_unidades * costo_unitario_usd + costo_envio_usd    # correcto

    # Calcular los impuestos
    tasa_aduana_cif_clp = valor_cif_usd * Decimal('0.06') * tipo_de_cambio
    iva_cif_clp = valor_cif_usd * Decimal('0.19') * tipo_de_cambio

    # Calcular otros valores requeridos
    total_pedido_clp = valor_cif_usd * tipo_de_cambio        # cambios de dolares a peso correcto
    costo_envio_clp = costo_envio_usd * tipo_de_cambio
    
    total_impuesto_aduana_clp = tasa_aduana_cif_clp + iva_cif_clp
    
    costo_total_clp = total_pedido_clp + total_impuesto_aduana_clp  #aqui realice el cambio le quite la suma del envio 
    costo_total_usd = costo_total_clp / tipo_de_cambio
    
    simulacion = Simulacion(**datos)
    
    # Asignar los nuevos valores al objeto simulacion
    simulacion.total_pedido_clp = int(total_pedido_clp)
    simulacion.costo_envio_clp = int(costo_envio_clp)
    simulacion.tasa_aduana_clp = int(tasa_aduana_cif_clp)
    simulacion.iva_clp = int(iva_cif_clp)
    simulacion.total_impuestos_aduana_clp = int(total_impuesto_aduana_clp)
    simulacion.costo_total_compra_clp = int(costo_total_clp)
    
    simulacion.save()  # Guardar el objeto Simulacion en la base de datos
    
    simulacion.save()
    
    # Crear un registro en el historial después de guardar la simulación            
    historial = HistorialConsulta(simulacion=simulacion)
    historial.save()
    
    return {
        'total_pedido_clp': int(total_pedido_clp),  
        'costo_envio_clp': int(costo_envio_clp),    
        'tasa_aduana_clp': int(tasa_aduana_cif_clp),  
        'iva_clp': int(iva_cif_clp),               
        'total_impuestos_aduana_clp': int(total_impuesto_aduana_clp),  
        'costo_total_compra_clp': int(costo_total_clp),             
        'costo_total_compra_usd': int(costo_total_usd),       
        
    }

def calcular_costo(request):
    if request.method == 'POST':
        form = SimulacionForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            # Calcular impuestos y otros valores requeridos
            resultados = calcular_impuestos(datos)

            return render(request, 'resultados.html', {
                'datos': datos,
                **resultados,  # Agregar los resultados al contexto
            })
    else:
        form = SimulacionForm()

    return render(request, 'calcular_costo.html', {'form': form})



#borrar solo prueba de historial
def historial_consultas(request):
    historial = HistorialConsulta.objects.all()
    return render(request, 'historial_consultas.html', {'historial': historial})