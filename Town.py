En un pueblo pequeño la población es de principios de año. La población regularmente aumenta cada año y, además, nuevos habitantes cada año vienen a vivir a la ciudad. ¿Cuántos años necesita el pueblo para ver su población? mayor o igual a los habitantes?p0 = 10002 percent50p = 1200

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
Parámetros dados de manera más general:

p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

La función debe devolver el número de años enteros necesarios para obtener una población mayor o igual a .nb_yearnp

aug es un número entero, el porcentaje es un número flotante positivo o nulo, p0 y p son números enteros positivos (> 0)

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
Nota:
No olvides convertir el parámetro de porcentaje como un porcentaje en el cuerpo de tu función: si el parámetro de porcentaje es 2, tienes que convertirlo a 0.02.