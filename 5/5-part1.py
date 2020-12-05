with open('input.txt') as f:
    seats = f.read().split('\n')
    highest_seat_id = 0
    for seat in seats:
        seat_id = int(seat.replace('B', r'1').replace('F', r'0').replace('R', r'1').replace('L', r'0'), base=2)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    print(f"Highest seat ID: {highest_seat_id}")