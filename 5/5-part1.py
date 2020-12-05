with open('input.txt') as f:
    seats = f.read().split('\n')
    highest_seat_id = 0
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
    print(f"Highest seat ID: {highest_seat_id}")