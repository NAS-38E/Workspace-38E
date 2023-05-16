import 'dart:math';

void main() {
  List<int> lista1 = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];
  List<int> lista2 = List.generate(10, (index) => -Random().nextInt(5));
  print("Lista 1: $lista1");
  print("Lista 2: $lista2");

  List<int> listaSuma = [];
  for (int i = 0; i < lista1.length; i++) {
    listaSuma.add(lista1[i] + lista2[i]);
  }
  print("Lista suma: $listaSuma");

  listaSuma.removeRange(6, 8);
  print("Removiendo el séptimo y octavo elemento de la lista : $listaSuma");
}
