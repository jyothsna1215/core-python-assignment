def book_seat(booked_seats, seat_number):
    if seat_number not in booked_seats:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} successfully booked.")
    else:
        print(f"Seat {seat_number} is already booked.")
def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} successfully canceled.")
    else:
        print(f"Seat {seat_number} is not booked yet.")
def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
booking=int(input("Enter the seat to be booked"))
cancel=int(input("Enter the seat to be cancelled"))
book_seat(booked_seats,booking)
cancel_seat(booked_seats,cancel)
available = available_seats(total_seats, booked_seats)
print(f"\nAvailable seats: {available}")
