from Nomina import nomina as nm
n1 = nm()

salario = float(input('Ingrese el salario base del empleado:\n'))
print('------------------------------------------------------------------------------------------------')
ventasPropiedad=float(input('Ingrese el ventas por propiedades:\n'))
print('------------------------------------------------------------------------------------------------')
ventasVehiculo=float(input('Ingrese el ventas por vehiculos:\n'))
print('------------------------------------------------------------------------------------------------')
ventasMercancia=float(input('Ingrese el ventas por mercancia:\n'))
print('------------------------------------------------------------------------------------------------')
descuentosSeguridadSocial=float(input('Ingrese el % descuento por Seguridad social:\n'))
print('------------------------------------------------------------------------------------------------')
descuentosPrestamo=float(input('Ingrese el % descuento por prestamo :\n'))
print('------------------------------------------------------------------------------------------------')
descuentosFondoEmpleados=float(input('Ingrese el % descuento por fondo de empleados:\n'))
print('------------------------------------------------------------------------------------------------')

comisionPropiedad = n1.CalculoGanancias(ventasPropiedad, 1)
comisionVehiculo = n1.CalculoGanancias(ventasVehiculo, 2)
comisionMercancia = n1.CalculoGanancias(ventasMercancia, 5)

devengado= salario + comisionMercancia + comisionVehiculo + comisionPropiedad

seguridadSocial = n1.CalculoDescuentos(devengado, descuentosSeguridadSocial)
prestamos = n1.CalculoDescuentos(devengado, descuentosPrestamo)
fondoEmpleados = n1.CalculoDescuentos(devengado, descuentosFondoEmpleados)

retencion = n1.CalculoRetencion(devengado)
totalNeto=(devengado-(seguridadSocial+prestamos+fondoEmpleados))

print('Comision por Propiedad--------------', comisionPropiedad)
print('Comision por Vehiculos--------------', comisionVehiculo )
print('Comision por Mercancias-------------', comisionMercancia)
print('Total Comisiones--------------------', (comisionPropiedad+comisionVehiculo+comisionMercancia))
print('------------------------------------------------------------------------------------------------')
print('Descuento por seguridad social--------------', seguridadSocial)
print('Descuento por prestamos       --------------', prestamos)
print('Descuento por fondo empleados -------------',  fondoEmpleados)
print('Total Descuentos---------------------------', (seguridadSocial+prestamos+fondoEmpleados))
print('------------------------------------------------------------------------------------------------')
print('Retenciones-------------------', retencion)
print('------------------------------------------------------------------------------------------------')
print('Total Bruto ----------------------------', devengado)
print('Total Neto  ----------------------------',totalNeto)