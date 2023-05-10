def solve_case(case_num, n, r, c, grid, events):
    # Create a data structure to represent the airport
    landing_squares = set()
    parking_spaces = {}
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '..':
                landing_squares.add((i, j))
            elif grid[i][j].isdigit():
                parking_spaces[int(grid[i][j])] = (i, j)
    
    # Simulate the events
    assignments = {}
    for event in events:
        if event > 0:
            # Landing event
            assigned = False
            for square in landing_squares:
                if square not in assignments.values():
                    assignments[event] = square
                    assigned = True
                    break
            if not assigned:
                print(f"Case {case_num}: No")
                return
            landing_squares.remove(square)
        else:
            # Take-off event
            square = assignments[-event]
            landing_squares.add(square)
            assignments.pop(-event)
    
    # Output the results
    print(f"Case {case_num}: Yes")
    for i in range(1, n+1):
        print(f"{parking_spaces[i][0]+1:02d}{parking_spaces[i][1]+1:02d}", end=' ')
    print()
    

# Main loop
case_num = 1
while True:
    n, r, c = map(int, input().split())
    if n == 0:
        break
    grid = [input().split() for _ in range(r)]
    events = list(map(int, input().split()))
    solve_case(case_num, n, r, c, grid, events)
    case_num += 1