def drive(car, fuel_needed, distance):
    car_fuel = cars[car][1]
    car_mileage = cars[car][0]
    if car_fuel >= fuel_needed:
        cars[car][0] += distance
        cars[car][1] -= fuel_needed
        return f'{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.'
    return f'Not enough fuel to make that ride'


def refuel(car, fuel):
    car_fuel = cars[car][1]
    if car_fuel + fuel <= 75:
        cars[car][1] += fuel
        filled_fuel = fuel
    else:
        filled_fuel = 75 - car_fuel
        cars[car][1] = 75
    return f'{car} refueled with {filled_fuel} liters'


def revert(car, kms):
    cars[car][0] -= kms
    if cars[car][0] < 10000:
        cars[car][0] = 10000
    else:
        print(f"{car} mileage decreased by {kms} kilometers")


num_cars = int(input())
cars = {}

for _ in range(num_cars):
    cars_input = input().split('|')
    car, mileage, available_fuel = cars_input
    mileage = int(mileage)
    available_fuel = int(available_fuel)
    cars[car] = [mileage, available_fuel]

commands = input()
while commands != 'Stop':
    command, *others = commands.split(' : ')
    if command == 'Drive':
        car, distance, fuel = others
        fuel_needed = int(fuel)
        distance = int(distance)
        print(drive(car, fuel_needed, distance))
        if cars[car][0] > 100000:
            print(f'Time to sell the {car}!')
            del cars[car]

    elif command == 'Refuel':
        car, fuel = others
        fuel = int(fuel)
        print(refuel(car, fuel))

    elif command == 'Revert':
        car, kms = others
        kms = int(kms)
        revert(car, kms)

    commands = input()

for car, data in cars.items():
    print(f'{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.')

