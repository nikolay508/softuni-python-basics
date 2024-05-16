sum_tickets = 0
all_tickets = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0

command = input()
while command != "Finish":
    name_movie = command
    free_seats = int(input())
    ticket = input()
    while ticket != "End":
        sum_tickets += 1
        all_tickets += 1

        if ticket == "student":
            student_ticket += 1
        elif ticket == "standard":
            standard_ticket += 1
        elif ticket == "kid":
            kids_ticket += 1

        if sum_tickets >= free_seats:
            break

        ticket = input()
    print(f"{name_movie} - {(sum_tickets /  free_seats) * 100:.2f}% full.")   #error
    sum_tickets = 0
    command = input()

if command == "Finish":
    print(f"Total tickets: {all_tickets}")
    print(f"{(student_ticket / all_tickets) * 100:.2f}% student tickets.")
    print(f"{(standard_ticket / all_tickets) * 100:.2f}% standard tickets.")
    print(f"{(kids_ticket / all_tickets) * 100:.2f}% kids tickets.")
