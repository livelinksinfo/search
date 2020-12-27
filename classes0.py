class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.persengers=[]

    def add_persenger(self, name):
        if not self.open_seat():
            return False
        self.persengers.append(name)
        return True

    def open_seat(self):
        return self.capacity - len(self.persengers)
flight= Flight(3)


people = ["Ron", "Harry","Hermione" , "Ginny"]
for i in people:
    success = flight.add_persenger(i)
    if success:
        print(f"Added {i} to flight successfully.")
    else:
        print(f"No available space for {i}")