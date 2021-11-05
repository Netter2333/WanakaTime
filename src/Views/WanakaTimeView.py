import PySimpleGUI as sg
from datetime import datetime, timedelta


class WanakaTimeView:

    def __init__(self):
        file_list_column = [
            [
                sg.Text("Menu")
                sg.In(size=(25,1), enable_events=True, key="-FOLDER-")
            ]
        ]
        self.active = True
        self.times_cow = []
        self.times_cabbage = []
        self.times_koi = []
        self.times_apple = []

    def menu(self):

        while self.active:

            print(f"Menu \n 1. Plantar \n 2. Guardar \n 3. Listar \n 4. Salir")
            option = input().lower()

            if option == "1":
                self.plant()

            if option == "2":
                self.save()

            if option == '3':
                self.printlist()

            if option == '4':
                self.exit()
            else:
                print()

    def plant(self):

        print("Que desea plantar? (back para regresar)")
        option = input().lower()

        while option != 'back':

            if option == 'cabbage' or option == 'repollo':

                first_watering = datetime.now() + timedelta(hours=2)
                second_watering = datetime.now() + timedelta(hours=4)
                harvest_time = datetime.now() + timedelta(hours=6)

                self.times_cabbage.extend([first_watering.strftime('%H:%M:%S'),
                                           second_watering.strftime('%H:%M:%S'),
                                           harvest_time.strftime('%H:%M:%S')])

                print(f" Riegos: {self.times_cabbage[0]} || {self.times_cabbage[1]}")
                print(f" Cosecha: {self.times_cabbage[2]}")
                print()

            elif option == 'apple' or option == 'manzana':

                first_watering = datetime.now() + timedelta(hours=4)
                second_watering = datetime.now() + timedelta(hours=6)
                third_watering = datetime.now() + timedelta(hours=8)
                harvest_time = datetime.now() + timedelta(hours=12)

                self.times_apple.extend([first_watering.strftime('%H:%M:%S'),
                                         second_watering.strftime('%H:%M:%S'),
                                         third_watering.strftime('%H:%M:%S'),
                                         harvest_time.strftime('%H:%M:%S')])

                print(f" Riegos: {self.times_apple[0]} || {self.times_apple[1]}")
                print(f" Cosecha: {self.times_apple[2]}")
                print()

            elif option == 'cow' or option == 'vaca':

                first_watering = datetime.now() + timedelta(hours=4)
                second_watering = datetime.now() + timedelta(hours=8)
                third_watering = datetime.now() + timedelta(hours=12)
                fourth_watering = datetime.now() + timedelta(hours=16)
                harvest_time = datetime.now() + timedelta(hours=24)

                self.times_cow.extend([first_watering.strftime('%H:%M:%S'),
                                       second_watering.strftime('%H:%M:%S'),
                                       third_watering.strftime('%H:%M:%S'),
                                       fourth_watering.strftime('%H:%M:%S'),
                                       harvest_time.strftime('%H:%M:%S')])

                print(f" Riegos: {self.times_cow[0]} || {self.times_cow[1]} || {self.times_cow[2]} || {self.times_cow[3]}")
                print(f" Cosecha: {self.times_cow[4]}")
                print()

            elif option == 'koi fish' or option == 'fish' or option == 'koi' or option == 'pescado':

                first_watering = datetime.now() + timedelta(hours=4)
                second_watering = datetime.now() + timedelta(hours=8)
                third_watering = datetime.now() + timedelta(hours=12)
                harvest_time = datetime.now() + timedelta(hours=18)

                self.times_koi.extend([first_watering.strftime('%H:%M:%S'),
                                       second_watering.strftime('%H:%M:%S'),
                                       third_watering.strftime('%H:%M:%S'),
                                       harvest_time.strftime('%H:%M:%S')])

                print(f" Riegos: {self.times_koi[0]} || {self.times_koi[1]} || {self.times_koi[2]}")
                print(f" Cosecha: {self.times_koi[3]}")
                print()

            elif option == 'back':
                self.menu()

            print("Que desea plantar? (back para regresar)")
            option = input().lower()

    def save(self):
        with open("wanaka.txt", "a") as file_object:

            if len(self.times_cabbage) > 0:
                file_object.write(
                    f"Repollo: \n Riegos: {self.times_cabbage[0]} || {self.times_cabbage[1]} \n Cosecha: {self.times_cabbage[2]} \n")

            if len(self.times_apple) > 0:
                file_object.write(
                    f"Manzana: \n Riegos: {self.times_apple[0]} || {self.times_apple[1]} \n Cosecha: {self.times_apple[2]} \n")

            if len(self.times_koi) > 0:
                file_object.write(
                    f"Koi: \n Riegos: {self.times_koi[0]} || {self.times_koi[1]} || {self.times_koi[2]} \n Cosecha: {self.times_koi[3]} \n")

            if len(self.times_cow) > 0:
                file_object.write(
                    f"Vaca \n Riegos: {self.times_cow[0]} || {self.times_cow[1]} || {self.times_cow[2]} || {self.times_cow[3]} \n "
                    f"Cosecha: {self.times_cow[4]} \n")

            print(f"\n Guardado satisfactoriamente! \n")

    def printlist(self):
        if len(self.times_koi) > 0:
            print(
                f"Pez Koi: \n Riegos: {self.times_koi[0]} || {self.times_koi[1]} || {self.times_koi[2]} \n Cosecha: {self.times_koi[3]} \n")

        if len(self.times_cow) > 0:
            print(
                f"Vaca: \n Riegos: {self.times_cow[0]} || {self.times_cow[1]} || {self.times_cow[2]} || {self.times_cow[3]} \n Cosecha: {self.times_cow[4]} \n")

        if len(self.times_apple) > 0:
            print(
                f"Manzana: \n Riegos: {self.times_apple[0]} || {self.times_apple[1]} \n Cosecha: {self.times_apple[2]} \n")

        if len(self.times_cabbage) > 0:
            print(
                f"Repollo: \n Riegos: {self.times_cabbage[0]} || {self.times_cabbage[1]} \n Cosecha: {self.times_cabbage[2]} \n")

        else:
            print("Lista vacia")

    def exit(self):
        self.active = False
