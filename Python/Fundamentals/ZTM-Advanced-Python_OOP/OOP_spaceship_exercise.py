# You're the captain of a spaceship called Odyssey-7.
# Before you can launch, the ground crew checks that you have enough fuel and crew on board. Once you launch, you enter orbit. While in space you burn through fuel, so you need to refuel at a space station before you can make another trip. When you're ready to come home, you initiate landing — but only if you're actually in orbit, you can't land if you never left.
# Now model that in a class.



# before launch, crew check if enough fuel and crew
# once launch, you enter orbit
# while in space you burn trough fuel
# need refuel at space station
# when going home, you enter orbit again
# initiate landing


# class Spaceship:
#     def __init__(self, name, crew, fuel, status):
#         self.name = name
#         self.crew = crew
#         self.fuel = fuel
#         self.status = status


#     def __str__(self):
#         crew_names = ", ".join([member.name for member in self.crew])
#         return f"Spaceship: {self.name}, crew: {crew_names}, Fuel: {self.fuel} Liters, Operation: {self.status} Mode."

#     def standby(self):
#         self.status = "standby"
#     def launch(self):
#         self.status = "launch"
#     def thrust(self):
#         self.status = "thrust"
#     def coasting(self):
#         self.status = "coasting"
#     def reentry(self):
#         self.status = "reentry"
#     def landing(self):
#         self.status = "landing"



# space_crew_data = {
#     "01": {
#         "name": "brand",
#         "age": 32,
#         "sex": "M",
#         "specialization": "pilot",
#         "status": "active"
#     },
#     "02": {
#         "name": "alexa",
#         "age": 28,
#         "sex": "F",
#         "specialization": "engineer",
#         "status": "active"
#     },
#     "03": {
#         "name": "nelly",
#         "age": 35,
#         "sex": "F",
#         "specialization": "medic",
#         "status": "standby"
#     },
#     "04": {
#         "name": "ibrahim",
#         "age": 40,
#         "sex": "M",
#         "specialization": "commander",
#         "status": "active"
#     }
# }

# class CrewMember:
#     def __init__(self, crew_id, name, age, sex, specialization, status):
#         self.crew_id = crew_id
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.specialization = specialization
#         self.status = status

# crew = []
# for crew_id, details in space_crew_data.items():
#     member = CrewMember(
#         crew_id,
#         details["name"],
#         details["age"],
#         details["sex"],
#         details["specialization"],
#         details["status"]
#     )
#     crew.append(member)



# def main():
#     pass
#     #MainClass
#     spaceship_7 = Spaceship("Odyssey-7",  crew, 485000, "standby") #MainClass
#     print(f"This is Captain Ibrahim, id number 4. Commander chief of the {spaceship_7.name}")
#     print(f"Final check before take off.")
#     print(spaceship_7)
#     print(f"Launch in T-10")
#     print("Operation Mode: " + spaceship_7.status)
#     spaceship_7.launch()
#     print("Initiate Operation Mode: " + spaceship_7.status)
#     spaceship_7.thrust()
#     print("Initiate Operation Mode: " + spaceship_7.status)
#     spaceship_7.coasting()
#     print(f"{spaceship_7.name} has entered the Orbit and is coupling with the ISS space-station for refuel, shutting of Engine.")
#     spaceship_7.standby()
#     print("Initiate Operation Mode: " + spaceship_7.status)
#     print(f"{spaceship_7.name} has refueled ready to return to earth.")
#     spaceship_7.coasting()
#     print("Initiate Operation Mode: " + spaceship_7.status)
#     print(f"{spaceship_7.name} is leaving the orbit returning to earth, brace for resistance!")
#     spaceship_7.reentry()
#     print("Initiate Operation Mode: " + spaceship_7.status)
#     spaceship_7.landing()
#     print("Initiate Operation Mode: " + spaceship_7.status)
#     print(f"{spaceship_7.name} has succesfully landed, {spaceship_7.name} is safe and secure!")




# if __name__ == "__main__":
#     main()
