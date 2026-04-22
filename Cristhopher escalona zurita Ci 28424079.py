
# 1 para bolívar 2 para dólar en el menú
#el monto a retirar debe ser numero entero 
#tipo de cuenta, 1 para Ahorro, 2 para corriente
# cajero solo dispone de billetes de 10,20,50 y 100

#para calcular el desglose
define desglose(a)

billetes[10,20,50,100]
billertescantidad=[]
resto=a

se utilizara un bucle for que va a calcular la cantidad de billetes para utilizar guardado cada cantidad el array billetescantidad
for billete in billetes:
cantidad=resto//billetes #aqui cantidad utiliza para guardar el numero de billetes que se utilizara
billetescantidad.append(cantidad) 

return billetescantidad #retornamos con la cantidad de billetes para el desglose

tipodecuenta=0
tipodemoneda=0
monto=0

print("welcome al cajero")
#el usuario elige tipo de cuemta que se usa y valida la opcion
print(que tipo de moneda desea retirar)
tipodemoneda=int(imput("bolivar","dolares")

#se calcula el monto que se puede elegir del tipo de moneda con una condicion basica
if tipodemoneda=1:
montomaximo=1000

tipobillete = imput("tipo de billete(1para bolivares,2 para doalres):")
monto=int(input(montoa retirar:))
if monto % 10 =0:
print("error: monto no disponible)
tipodecuenta=int(imput(tipo de cuenta(2 para ahorro,1 para corriente):
if tipobillete==1
moneda="bolivares"
elif tipobillete==2
moneda = "dolares"
else(error:tipo de billete no valido")
if tipodecuenta==1:
    cuenta = "ahorro"
elif tipodecuenta ==2
cuenta = "corriente"
else:
    print("error: tipo de cuenta no valido")
    if tipobillete ==1:
    else monto>10000:
    print("transaaccion denegada")
    elif tipobillete == 2:
        if monto> 500:
    print(transaaccion denegada)
    if tipodecuenta == 2:
        comision = monto 0.05