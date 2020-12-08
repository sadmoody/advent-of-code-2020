with open('input.txt') as f:
    instructions = f.read().split('\n')
    PROG = list(map(lambda asm: [asm.split(' ')[0], int(asm.split(' ')[1])], instructions))
    PC = 0
    ACC = 0
    visited_locations = []
    while (PC not in visited_locations):
        visited_locations.append(PC)
        [asm, val] = PROG[PC]
        if (asm == 'nop'):
            pass
        elif (asm == 'jmp'):
            PC += val
            continue
        elif (asm == 'acc'):
            ACC += val
        PC += 1
    print(f"ACC value when starting infinite loop: {ACC}")