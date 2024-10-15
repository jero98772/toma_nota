from typing import Dict, Set, List, Tuple
from grammar_parser import Grammar, format_set,parse_input  # Assuming the previous code is in grammar_parser.py

class TopDownParser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.first_sets = self.grammar.compute_first_sets()
        self.follow_sets = self.grammar.compute_follow_sets(self.first_sets)
        self.parsing_table: Dict[Tuple[str, str], str] = {}

    def is_ll1(self) -> bool:
        for non_terminal in self.grammar.non_terminals:
            for production in self.grammar.productions[non_terminal]:
                first_of_production = self.grammar.compute_first_of_string(production, self.first_sets)
                for terminal in first_of_production - {'e'}:
                    if (non_terminal, terminal) in self.parsing_table:
                        return False
                if 'e' in first_of_production:
                    for terminal in self.follow_sets[non_terminal]:
                        if (non_terminal, terminal) in self.parsing_table:
                            return False
        return True

    def compute_parsing_table(self):
        for non_terminal in self.grammar.non_terminals:
            for production in self.grammar.productions[non_terminal]:
                first_of_production = self.grammar.compute_first_of_string(production, self.first_sets)
                for terminal in first_of_production - {'e'}:
                    self.parsing_table[(non_terminal, terminal)] = production
                if 'e' in first_of_production:
                    for terminal in self.follow_sets[non_terminal]:
                        self.parsing_table[(non_terminal, terminal)] = production

    def parse(self, input_string: str) -> bool:
        stack = ['$', self.grammar.start_symbol]
        input_string += '$'
        index = 0

        while stack:
            top = stack[-1]
            current_input = input_string[index]

            if top == current_input:
                stack.pop()
                index += 1
            elif top in self.grammar.terminals:
                return False
            elif (top, current_input) not in self.parsing_table:
                return False
            else:
                stack.pop()
                production = self.parsing_table[(top, current_input)]
                if production != 'e':
                    stack.extend(reversed(production))

        return True

def main():
    # Example usage
    grammars = parse_input()
    for grammar in grammars:
        parser = TopDownParser(grammar)
        
        print("Is LL(1):", parser.is_ll1())
        
        parser.compute_parsing_table()
        print("\nParsing Table:")
        for (nt, t), prod in parser.parsing_table.items():
            print(f"({nt}, {t}) -> {prod}")

        test_strings = ['aabcc', 'aaabbbccc', 'abc', 'ac']
        print("\nParsing test strings:")
        for s in test_strings:
            print(f"'{s}': {'Accepted' if parser.parse(s) else 'Rejected'}")

if __name__ == "__main__":
    main()