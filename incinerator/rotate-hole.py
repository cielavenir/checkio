rotate=lambda state,pipe_numbers: [i for i in range(len(state)) if all(state[j%len(state)] or (i+j)%len(state) not in set(pipe_numbers) for j in range(len(state)))]