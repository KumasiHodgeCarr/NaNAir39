from Models.airplane import Airplane
from LogicLayer.airplaneLL import AirplaneLL

class AirplaneUI:

    def __init__(self):
        self.__airplaneLL = AirplaneLL()

    def header(self):
        pass

    def register_airplane(self):

        # setja header

        print("Registering a new airplane\n")
        planeInsignia = input("Enter plane insignia: ")
        if self.__airplaneLL.check_airplane(planeInsignia):
            print("\nAirplane already exists.")
        else:
            planeTypeId = input("Enter plane type ID: ")
            manufacturer = input("Enter manufacturer: ")
            model = input("Enter model: ")
            capacity = int(input("Enter capacity: "))

            new_airplane = Airplane(planeInsignia, planeTypeId, manufacturer, model, capacity)
            print("\n{}\n".format(new_airplane))

            if input("Do you want to register this airplane? ").upper() == "Y":
                self.__airplaneLL.register_airplane(new_airplane)
                print("\nNew airplane registered!\n")
            else:
                print("\nAirplane not registered.\n")

if __name__ == "__main__":
    a = AirplaneUI()
    a.register_airplane()