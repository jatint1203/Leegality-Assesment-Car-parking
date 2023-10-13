class car_park:
    def __init__(self):
        self.spots = {}  # In-memory storage for parking spots
        self.available_places = {'A' : [i for i in range(1,21)], 'B' : [j for j in range(21,41)]} 

    def assign_spot(self, vehicle_number):
        if not self.available_places['A'] and not self.available_places['B']:
            return "Parking lot is full."

        level, spot_number = None, None
        if self.available_places['A']:
            level = 'A'
            spot_number = self.available_places['A'].pop(0)
        else:
            level = 'B'
            spot_number = self.available_places['B'].pop(0)

        self.spots[vehicle_number] = {'level': level, 'spot': spot_number}
        return f"Assigned spot: {{'level': {level}, 'spot': {spot_number}}}"

    def retrieve_spot(self, vehicle_number):
        if vehicle_number in self.spots:
            return self.spots[vehicle_number]
        else:
            return "Vehicle not found in the parking lot."

    def print_parking_lot_status(self):
        print("Parking Lot Status:")
        print("Level A:", self.available_places['A'])
        print("Level B:", self.available_places['B'])
        print("Occupied Spots:", self.spots)


def main():
    parking_lot = car_park()
    
    while True:
        print("\n##################### Choose Below Options: #####################")
        print("1. Assign a parking spot")
        print("2. Retrieve parking spot of a vehicle")
        print("3. Print Parking Lot Status")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.assign_spot(vehicle_number)
            print(result)
        elif choice == '2':
            vehicle_number = input("Enter the vehicle number: ")
            spot_info = parking_lot.retrieve_spot(vehicle_number)
            print(spot_info)
        elif choice == '3':
            parking_lot.print_parking_lot_status()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
