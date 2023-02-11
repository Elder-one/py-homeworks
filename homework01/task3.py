ticket_number = input('Введите номер билета в формате ХХХХХХ --> ')

if len(ticket_number) == 6:
    print(
        int(ticket_number[0]) + int(ticket_number[1])
        + int(ticket_number[2]) == int(ticket_number[3])
        + int(ticket_number[4]) + int(ticket_number[5])
        )

else:
    print('Неверный формат')
