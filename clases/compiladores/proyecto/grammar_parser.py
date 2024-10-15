from typing import Dict, Set, List, Tuple
import sys


class Grammar:
    def __init__(self):
        self.productions: Dict[str, List[str]] = {}
        self.terminals: Set[str] = set()
        self.non_terminals: Set[str] = set()
        self.start_symbol: str = 'S'

    def add_production(self, non_terminal: str, production: str):
        if non_terminal not in self.productions:
            self.productions[non_terminal] = []
        self.productions[non_terminal].append(production)
        self.non_terminals.add(non_terminal)
        for symbol in production:
            if symbol.islower() or symbol == 'e':
                self.terminals.add(symbol)

    def compute_first_sets(self) -> Dict[str, Set[str]]:
        first: Dict[str, Set[str]] = {nt: set() for nt in self.non_terminals}
        first.update({t: {t} for t in self.terminals})
        first['e'] = {'e'}

        while True:
            updated = False
            for nt in self.non_terminals:
                for production in self.productions[nt]:
                    k = 0
                    for symbol in production:
                        if symbol == 'e':
                            if 'e' not in first[nt]:
                                first[nt].add('e')
                                updated = True
                            break
                        first_symbol = first[symbol]
                        first[nt].update(first_symbol - {'e'})
                        if 'e' not in first_symbol:
                            break
                        k += 1
                    if k == len(production) and 'e' not in first[nt]:
                        first[nt].add('e')
                        updated = True
            if not updated:
                break

        return first

    def compute_follow_sets(self, first: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
        follow: Dict[str, Set[str]] = {nt: set() for nt in self.non_terminals}
        follow[self.start_symbol].add('$')

        while True:
            updated = False
            for nt in self.non_terminals:
                for production in self.productions[nt]:
                    for i, symbol in enumerate(production):
                        if symbol in self.non_terminals:
                            if i == len(production) - 1:
                                if not follow[symbol].issuperset(follow[nt]):
                                    follow[symbol].update(follow[nt])
                                    updated = True
                            else:
                                rest = production[i+1:]
                                first_of_rest = self.compute_first_of_string(rest, first)
                                if not follow[symbol].issuperset(first_of_rest - {'e'}):
                                    follow[symbol].update(first_of_rest - {'e'})
                                    updated = True
                                if 'e' in first_of_rest:
                                    if not follow[symbol].issuperset(follow[nt]):
                                        follow[symbol].update(follow[nt])
                                        updated = True
            if not updated:
                break

        return follow

    def compute_first_of_string(self, string: str, first: Dict[str, Set[str]]) -> Set[str]:
        if not string:
            return {'e'}
        result = set()
        for symbol in string:
            symbol_first = first[symbol]
            result.update(symbol_first - {'e'})
            if 'e' not in symbol_first:
                return result
        result.add('e')
        return result

def parse_input() -> List[Grammar]:
    n = int(input().strip())
    grammars = []

    for _ in range(n):
        m = int(input().strip())
        grammar = Grammar()

        for _ in range(m):
            line = input().strip().split()
            non_terminal, productions = line[0], line[1:]
            for production in productions:
                grammar.add_production(non_terminal, production)

        grammars.append(grammar)

    return grammars

def format_set(s: Set[str]) -> str:
    return '{' + ','.join(sorted(s)) + '}'

def main():
    grammars = parse_input()

    for i, grammar in enumerate(grammars):
        first_sets = grammar.compute_first_sets()
        follow_sets = grammar.compute_follow_sets(first_sets)

        for nt in sorted(grammar.non_terminals):
            print(f"First({nt}) = {format_set(first_sets[nt])}")
        for nt in sorted(grammar.non_terminals):
            print(f"Follow({nt}) = {format_set(follow_sets[nt])}")

        if i < len(grammars) - 1:
            print()

if __name__ == "__main__":
    main()