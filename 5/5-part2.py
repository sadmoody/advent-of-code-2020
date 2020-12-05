with open('input.txt') as f:
    seats = f.read().split('\n')
    lowest_seat_id = 9999999999999
    highest_seat_id = 0
    sum_of_id = 0
    for seat in seats:
        row = 0
        for i in range(7):
            row += 1 << (6-i) if seat[i]=='B' else 0
        column = 0
        for i in range(7,10):
            column += 1 << (9-i) if seat[i]=='R' else 0
        seat_id = row * 8 + column
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
        if seat_id < lowest_seat_id:
            lowest_seat_id = seat_id
        sum_of_id += seat_id
    # Gauss formula for sum of consecutive numbers = n(low+high)/2
    # Gauss sum - current sum = missing seat id
    missing_id = (((len(seats) + 1) * (lowest_seat_id + highest_seat_id)) // 2) - sum_of_id
    print(f"Your seat ID is: {missing_id}")