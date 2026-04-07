# Make a class about a hospital patient check-in.
# A patient arrives, gets registered with their name, age, and condition. A nurse assigns them a priority level. They wait, get called in, get treated, and get discharged.
# Simple, professional, real world. Go.

# class Hospital_CheckIn():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.condition = None
#         self.priority = None
#         self.status = "Arrived"


#     def __str__(self):
#         if self.condition is None and self.priority is None:
#             return f"{self.name}, {self.age}"
#         else:
#             return f"{self.name}, {self.age}, {self.condition}, {self.priority}, Status: {self.status}"


#     def T1(self):
#         self.condition = "T1 — Immediate, life threatening, needs treatment now"
#         self.priority = "Emergency"
#     def T2(self):
#         self.condition = "T2 — Urgent, serious but can wait short time"
#         self.priority = "Urgent"
#     def T3(self):
#         self.condition = "T3 — Delayed, minor injuries, can wait longer"
#         self.priority = "Normal"
#     def T4(self):
#         self.condition = "T4 — Expectant, too critical to save, comfort only"
#         self.priority = "Low"
#     def T0(self):
#         self.condition = "T0 — Deceased"
#         self.priority = "Low"

#     def waiting(self):
#         self.status = "waiting"
#     def called_in(self):
#         self.status = "called in"
#     def getting_treated(self):
#         self.status = "getting treated"
#     def discharged(self):
#         self.status = "discharged"


# def main():
#     patient1 = Hospital_CheckIn("Amelia", 31)
#     print(patient1)
#     patient1.T3()
#     print(patient1)
#     patient1.waiting()
#     print(patient1)
#     patient1.called_in()
#     print(patient1)
#     patient1.getting_treated()
#     print(patient1)
#     patient1.discharged()
#     print(patient1)



# if __name__ == "__main__":
#     main()
