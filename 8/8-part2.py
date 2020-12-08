with open('input.txt') as f:
    instructions = f.read().split('\n')
    PROG = list(map(lambda asm: [asm.split(' ')[0], int(asm.split(' ')[1])], instructions))
    terminated = False
    COUNT = 0
    while (not terminated):
        PC = 0
        ACC = 0
        JMP_COUNT = 0
        NOP_COUNT = 0
        visited_locations = []
        while (PC not in visited_locations):
            visited_locations.append(PC)
            [asm, val] = PROG[PC]
            if (asm == 'nop'):
                if (NOP_COUNT*2 == COUNT):
                    PC += val - 1
                NOP_COUNT += 1
            elif (asm == 'jmp'):
                if (JMP_COUNT*2+1 != COUNT):
                    PC += val - 1
                JMP_COUNT += 1
            elif (asm == 'acc'):
                ACC += val
            PC += 1
            if (PC == len(PROG)):
                terminated = True
                break
        COUNT += 1
    print(f"ACC value when terminated: {ACC}")