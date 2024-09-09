def parse_grammar(k):
    grammar = {}
    for _ in range(k):
        line = input().split()
        nonterminal = line[0]
        productions = line[1:]
        grammar[nonterminal] = productions
    return grammar

def cyk_algorithm(grammar, string):
    n = len(string)
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Fill the base case
    for i in range(n):
        for nonterminal, productions in grammar.items():
            if string[i] in productions:
                table[i][i].add(nonterminal)
    
    # Fill the table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for nonterminal, productions in grammar.items():
                    for production in productions:
                        if len(production) == 2:
                            B, C = production
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(nonterminal)
    
    return 'S' in table[0][n-1]

def main():
    n = int(input())
    for _ in range(n):
        k, m = map(int, input().split())
        grammar = parse_grammar(k)
        
        for _ in range(m):
            string = input()
            result = cyk_algorithm(grammar, string)
            print("yes" if result else "no")

if __name__ == "__main__":
    main()
