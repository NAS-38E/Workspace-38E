import 'dart:math';

void main() {
  //a) Generar una lista aleatoria de 5 elementos
  List<int> lista1 = List.generate(5, (_) => Random().nextInt(100));
  print("Lista aleatoria generada: $lista1");

  //b) Ingrese una lista de 5 elementos por teclado(no la pude realizar asi que genere una lista random)
  List<int> lista2 = List.generate(5, (i) => Random().nextInt(100));
  print("Lista ingresada por el usuario: $lista2");

  //c) Las listas concatenadas
  lista1.addAll(lista2);
  print("Lista concatenada: $lista1");

  //d) Insertar los elementos en la posicion 7,8 y 9
  lista1.insertAll(6, [14, 20, 7]);
  print("Lista insertada: $lista1");

  //e) El promedio obtenido de la lista resultante
  double promedio = lista1.reduce((a, b) => a + b) / lista1.length;
  print("Promedio de la lista concatenada: $promedio");

  //f) La lista ordenada de forma descendente
  lista1.sort((a, b) => b.compareTo(a));
  print("Lista ordenada de forma descendente: $lista1");
}
//Nicolas Almuna
//38E