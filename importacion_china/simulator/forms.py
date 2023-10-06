from django import forms

class SimulacionForm(forms.Form):
    nombre_articulo = forms.CharField(max_length=255)
    codigo_articulo = forms.CharField(max_length=20)
    proveedor = forms.CharField(max_length=100)
    cantidad_unidades = forms.IntegerField(min_value=1)
    costo_unitario_usd = forms.DecimalField(min_value=0.01)
    costo_envio_usd = forms.DecimalField(min_value=0.01)