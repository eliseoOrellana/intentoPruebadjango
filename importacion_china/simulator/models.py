
# Create your models here.
from django.db import models

class Simulacion(models.Model):
    nombre_articulo = models.CharField(max_length=255)
    codigo_articulo = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=100)
    cantidad_unidades = models.PositiveIntegerField()
    costo_unitario_usd = models.DecimalField(max_digits=10, decimal_places=2)
    costo_envio_usd = models.DecimalField(max_digits=10, decimal_places=2)

    # Nuevos campos para las variables faltantes
    total_pedido_clp = models.PositiveIntegerField(default=0)
    costo_envio_clp = models.PositiveIntegerField(default=0)
    tasa_aduana_clp = models.PositiveIntegerField(default=0)
    iva_clp = models.PositiveIntegerField(default=0)
    total_impuestos_aduana_clp = models.PositiveIntegerField(default=0)
    costo_total_compra_clp = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre_articulo
    
    
    
    
class HistorialConsulta(models.Model):
    
    simulacion = models.ForeignKey(Simulacion, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)