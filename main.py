"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
ASCENDING_ORDER = True


def sort_list(items, ascending=True):
    if not isinstance(items, list):
       # raise RuntimeError(f"No puede ordenar {type(items)}")
       raise RuntimeError(f"products are not available {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = ASCENDING_ORDER
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        if len(sys.argv) == 4:
           ascending_order = sys.argv[3].lower() == "asc"
           # Cambiar a order descendente si el tercer argumento es "desc"
           if sys.argv[3].lower() == "desc"
               ascending_order = False
    else:
        feature/rsmrg/cambios-relacionados-a-la-primera-practica-EIEC
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("The third argument (optional) indicates the order: 'asc' for ascending or 'desc' for descending")
      
        #print("Se debe indicar el fichero como primer argumento")
        print("please provide filename as first argument")
        #print("El segundo argumento indica si se quieren eliminar duplicados")
        print("second argument is marked to delete duplicates")
        main
        sys.exit(1)

    #print(f"Se leerán las palabras del fichero {filename}")
    print(f"words will be readed from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        #print(f"El fichero {filename} no existe")
        print(f"the file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending_order))
