import sys
def parse_input():
    input = sys.stdin.read
    data = input().splitlines()
    
    c = int(data[0])
    cases = []
    index = 1
    
    for _ in range(c):
        n = int(data[index])
        index += 1
        alphabet = data[index].split()
        index += 1
        final_states = list(map(int, data[index].split()))
        index += 1
        transitions = []
        for _ in range(n):
            transitions.append(list(map(int, data[index].split())))
            index += 1
        cases.append((n, alphabet, final_states, transitions))
    
    return cases

def find_equivalent_states(n, alphabet, final_states, transitions):
    # Step 1: Initialize table
    distinguishable = [[False] * n for _ in range(n)]
    
    # Step 2: Mark distinguishable pairs
    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                distinguishable[i][j] = True
    
    # Step 3: Iteratively mark pairs
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not distinguishable[i][j]:
                    for symbol in alphabet:
                        idx = alphabet.index(symbol)
                        ti = transitions[i][idx]
                        tj = transitions[j][idx]
                        if ti != tj and (distinguishable[max(ti, tj)][min(ti, tj)]):
                            distinguishable[i][j] = True
                            changed = True
                            break
    
    # Step 4: Collect equivalent pairs
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not distinguishable[i][j]:
                equivalent_pairs.append((i, j))
    
    return equivalent_pairs

def main():
    cases = parse_input()
    results = []
    
    for case in cases:
        n, alphabet, final_states, transitions = case
        equivalent_pairs = find_equivalent_states(n, alphabet, final_states, transitions)
        results.append(" ".join(f"({p}, {q})" for p, q in equivalent_pairs))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
