from ejemplo.models import Familiar, Mascota, Vehiculos

Familiar(nombre="Mariano", direccion="Peña 298", nacimiento="1982-02-18", numero_pasaporte=11111111).save()
Familiar(nombre="Lorena", direccion="Pueyrredón 977", nacimiento="1976-12-07", numero_pasaporte=22222222).save()
Familiar(nombre="Santino", direccion="Suipacha 246", nacimiento="2006-11-30", numero_pasaporte=33333333).save()
Familiar(nombre="Valentin", direccion="Araos 460", nacimiento="2011-02-09", numero_pasaporte=44444444).save()
Familiar(nombre="Mateo", direccion="9 de Julio 1234", nacimiento="2013-01-09", numero_pasaporte=55555555).save()

Mascota(nombre="Homero", raza="Labrador", nacimiento="2009-04-20").save()
Mascota(nombre="Chop", raza="Rottweiler", nacimiento="2019-07-13").save()
Mascota(nombre="Magui", raza="Gato", nacimiento="2016-08-08").save()


Vehiculos(marca="Chevolet", modelo="Prisma").save()
Vehiculos(marca="Jeep", modelo="Cherokee").save()