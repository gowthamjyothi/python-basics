total_seats= 5
tickets_sold = 0
total_bookings = 0
rejected_bookings = 0

while total_seats > 0:
    n = int(input("Enter number of tickets (0 to exit): "))

    if n == 0:
        break

    # this is for checking no.of tickets(there must be a max of only 15 tickets given at a time) 
    if n < 1 or n > 15:
        print("BOOKING REJECTEDt")
        rejected_bookings += 1
        continue

    if n > total_seats:
        print("BOOKING REJECTED(No enough seats)")
        rejected_bookings += 1
        continue

    invalid_age = False

    # Checking age limit which sould  be above 12 years old
    for i in range(n):
        age = int(input(f"Enter age of person {i+1}: "))  # here we used {i+1} because to ask age of each person in a numerical order like person1,person2....person<=15

        if age < 12:
            invalid_age = True
            continue   # if the age is below 12 then it just ask the age  but do not execute code because we used continue and invalid_age becomes true 

       
    if invalid_age:
        print("BOOKING REJECTED due to Age restriction")
        rejected_bookings += 1
    else:
        print(f"BOOKING CONFIRMED - {n} tickets")
        total_seats -= n
        tickets_sold += n
        total_bookings += 1

    # if all the seats are booked then this is executed
    if total_seats == 0:
        break

# printing all the variables to show all the data
print("\nFINAL REPORT")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", total_seats)