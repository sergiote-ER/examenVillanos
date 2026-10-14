"""Menú de consola de la aplicación."""

import logging
from gestion import Gestion

logger = logging.getLogger(__name__)


class Menu:
    def __init__(self, gestion: Gestion):
        self.gestion = gestion

    def mostrar_heroes_villanos(self) -> None:
        """Muestra el menú de heroes y villanos y procesa las opciones."""
        while True:
            print("\n=== HÉROES Y VILLANOS DEL VIRGEN ===")
            print("1. Crear héroe")
            print("2. Crear villano")
            print("3. Listar personajes")
            print("4. Buscar por atributo")
            print("5. Emparejar héroe y villano")
            print("6. Eliminar personaje")
            print("0. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self._crear("heroe")
                elif opcion == "2":
                    self._crear("villano")
                elif opcion == "3":
                    self._listar()
                elif opcion == "4":
                    self._buscar()
                elif opcion == "5":
                    self._emparejar()
                elif opcion == "6":
                    self._eliminar()
                elif opcion == "0":
                    logger.info("Aplicación cerrada por el usuario.")
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def _crear(self, tipo: str) -> None:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        fecha = input("Fecha de nacimiento (AAAA-MM-DD): ").strip()
        personaje = self.gestion.crear_personaje_heroes_villanos(tipo, nombre, apellidos, fecha)
        print(f"Personaje creado: {personaje}")

    def _listar(self) -> None:
        tipo = input("¿Qué quieres listar? (heroe/villano/todos): ").strip()
        personajes = self.gestion.listar_personajes_heroes_villanos(tipo)
        if not personajes:
            print("No hay personajes para mostrar.")
            return
        for personaje in personajes:
            print(personaje)

    def _buscar(self) -> None:
        tipo = input("Tipo (heroe/villano): ").strip()
        print("Atributos: identificador, nombre, apellidos, fecha_nacimiento, edad,")
        print("          puntuacion_total y las cualidades propias de cada tipo.")
        atributo = input("Atributo: ").strip()
        operador = input("Operador (=, !=, >, >=, <, <=, contiene): ").strip()
        valor = input("Valor a buscar: ").strip()
        resultados = self.gestion.buscar_por_atributo_heroes_villanos(tipo, atributo, operador, valor)
        if not resultados:
            print("No se han encontrado coincidencias.")
        else:
            for personaje in resultados:
                print(personaje)

    def _emparejar(self) -> None:
        heroe, villano, diferencia, valoracion = self.gestion.emparejar_aleatoriamente()
        print(f"Héroe: {heroe}")
        print(f"Villano: {villano}")
        print(f"Diferencia de puntuación: {diferencia}")
        print(valoracion)

    def _eliminar(self) -> None:
        tipo = input("Tipo (heroe/villano): ").strip()
        identificador = int(input("Identificador: "))
        if self.gestion.eliminar_personaje(tipo, identificador):
            print("Personaje eliminado.")
        else:
            print("No existe un personaje con ese identificador.")

    def mostrar_plantilla_futbol(self) -> None:
        """Muestra el menú de futbol y procesa las opciones."""
        while True:
            print("\n=== PLANTILLAS DE FÚTBOL ===")
            print("1. Agregar miembro")
            print("2. Listar plantilla")
            print("3. Crear plantilla")
            print("4. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self._crear_miembro("jugador")
                elif opcion == "2":
                    self._listar_plantilla()
                elif opcion == "3":
                    self._crear_plantilla()
                elif opcion == "4":
                    logger.info("Aplicación cerrada por el usuario.")
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def mostrar_menu_aplicaciones(self) -> None:
        while True:
            print("\n=== MENÚ DE APLICACIONES ===")
            print("1. Héroes y villanos")
            print("2. Plantillas de fútbol")
            print("3. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self.mostrar_heroes_villanos()
                elif opcion == "2":
                    self.mostrar_plantilla_futbol()
                elif opcion == "3":
                    logger.info("Aplicación cerrada por el usuario.")
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def _crear_miembro(self, tipo: str) -> None:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        personaje = self.gestion.crear_miembro_plantilla_futbol(tipo, nombre, apellidos)
        print(f"Personaje creado: {personaje}")

    def _listar_plantilla(self) -> None:
        tipo = input("¿Qué quieres listar? (juadores/villano/todos): ").strip()
        miembros = self.gestion.listar_plantilla_miembros(tipo)
        if not miembros:
            print("No hay miembros para mostrar.")
            return
        for miembro in miembros:
            print(miembro)

    def _crear_plantilla(self) -> None:
        pass