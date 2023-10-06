
# Create your views here.
from django.shortcuts import render
from .forms import SimulacionForm
from .models import Simulacion
from decimal import Decimal
from .models import Simulacion, HistorialConsulta  # Importa el modelo HistorialConsulta-------borrar solo prueba de historial
from .models import HistorialConsulta# Importa el modelo HistorialConsulta--------borrar solo prueba de historial

def calcular_costo(request):
    if request.method == 'POST':
        form = SimulacionForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cantidad_unidades = datos['cantidad_unidades']
            costo_unitario_usd = Decimal(str(datos['costo_unitario_usd']))  # Convertir a Decimal
            costo_envio_usd = Decimal(str(datos['costo_envio_usd']))  # Convertir a Decimal

            valor_cif_usd = cantidad_unidades * costo_unitario_usd + costo_envio_usd
            tasa_aduana_cif_clp = valor_cif_usd * Decimal('0.06') * Decimal('890')
            iva_cif_clp = valor_cif_usd * Decimal('0.19') * Decimal('890')
            total_pedido_clp = valor_cif_usd * Decimal('890')
            costo_envio_clp = costo_envio_usd * Decimal('890')
            total_impuesto_aduana_clp = tasa_aduana_cif_clp + iva_cif_clp
            costo_total_clp = total_pedido_clp + costo_envio_clp + total_impuesto_aduana_clp
            costo_total_usd = costo_total_clp / Decimal('890')

            simulacion = Simulacion(**datos)
            simulacion.save()

            # Crear un registro en el historial después de guardar la simulación            ---borrar si es necesario intento de historial
            historial = HistorialConsulta(simulacion=simulacion)
            historial.save()

            return render(request, 'resultados.html', {
                'datos': datos,
                'valor_cif_usd': valor_cif_usd,
                'tasa_aduana_cif_clp': tasa_aduana_cif_clp,
                'iva_cif_clp': iva_cif_clp,
                'total_pedido_clp': total_pedido_clp,
                'costo_envio_clp': costo_envio_clp,
                'total_impuesto_aduana_clp': total_impuesto_aduana_clp,
                'costo_total_clp': costo_total_clp,
                'costo_total_usd': costo_total_usd,
            })
    else:
        form = SimulacionForm()

    return render(request, 'calcular_costo.html', {'form': form})

#borrar solo prueba de historial
def historial_consultas(request):
    historial = HistorialConsulta.objects.all()
    return render(request, 'historial_consultas.html', {'historial': historial})