from typing import Dict, Set, List, Tuple
from grammar_parser import Grammar, format_set, parse_input  # Importing Grammar class and helper functions from grammar_parser module

# Top-Down Parser class for LL(1) grammar
class TopDownParser:
    def __init__(self, grammar: Grammar):
        # Initialize parser with grammar, compute FIRST and FOLLOW sets
        self.grammar = grammar
        self.first_sets = self.grammar.compute_first_sets()
        self.follow_sets = self.grammar.compute_follow_sets(self.first_sets)
        self.parsing_table: Dict[Tuple[str, str], str] = {}  # Parsing table mapping (non-terminal, terminal) pairs to production rules

    # Check if the grammar is LL(1) by ensuring there are no conflicts in the parsing table
    def is_ll1(self) -> bool:
        for non_terminal in self.grammar.non_terminals:
            for production in self.grammar.productions[non_terminal]:
                # Calculate the FIRST set of the current production
                first_of_production = self.grammar.compute_first_of_string(production, self.first_sets)
                
                # Ensure no conflicting entries in parsing table for FIRST terminals
                for terminal in first_of_production - {'e'}:  # 'e' represents epsilon (empty string)
                    if (non_terminal, terminal) in self.parsing_table:
                        return False  # Conflict found, not LL(1)
                
                # If epsilon is in the FIRST set, add FOLLOW set terminals to parsing table
                if 'e' in first_of_production:
                    for terminal in self.follow_sets[non_terminal]:
                        if (non_terminal, terminal) in self.parsing_table:
                            return False  # Conflict found, not LL(1)
        return True  # No conflicts, grammar is LL(1)

    # Compute the parsing table based on FIRST and FOLLOW sets
    def compute_parsing_table(self):
        for non_terminal in self.grammar.non_terminals:
            for production in self.grammar.productions[non_terminal]:
                # Calculate the FIRST set of the current production
                first_of_production = self.grammar.compute_first_of_string(production, self.first_sets)
                
                # Add entries to the parsing table for terminals in the FIRST set
                for terminal in first_of_production - {'e'}:
                    self.parsing_table[(non_terminal, terminal)] = production
                
                # If epsilon is in the FIRST set, add FOLLOW set terminals to parsing table
                if 'e' in first_of_production:
                    for terminal in self.follow_sets[non_terminal]:
                        self.parsing_table[(non_terminal, terminal)] = production

    # Parse an input string using the parsing table to validate if it belongs to the language
    def parse(self, input_string: str) -> bool:
        stack = ['$', self.grammar.start_symbol]  # Initialize stack with end-of-input symbol and start symbol
        input_string += '$'  # Append end-of-input symbol to input string
        index = 0  # Index to track position in input string

        while stack:
            top = stack[-1]  # Top of the stack
            current_input = input_string[index]  # Current input symbol

            # If stack top matches current input symbol, consume both
            if top == current_input:
                stack.pop()
                index += 1
            elif top in self.grammar.terminals:  # If stack top is a terminal and doesn't match input, reject
                return False
            elif (top, current_input) not in self.parsing_table:  # If no matching production in table, reject
                return False
            else:
                # Apply production rule from parsing table
                stack.pop()
                production = self.parsing_table[(top, current_input)]
                if production != 'e':  # If production is not epsilon, push it onto stack
                    stack.extend(reversed(production))  # Reverse production for correct parsing order

        return True  # Accepted if input fully parsed and stack is empty

# Main function for testing the parser
def main():
    # Parse grammar input
    grammars = parse_input()
    for grammar in grammars:
        parser = TopDownParser(grammar)
        
        # Check if grammar is LL(1)
        print("Is LL(1):", parser.is_ll1())
        
        # Compute and display parsing table
        parser.compute_parsing_table()
        print("\nParsing Table:")
        for (nt, t), prod in parser.parsing_table.items():
            print(f"({nt}, {t}) -> {prod}")

        # Test parser on example strings
        test_strings = ['aabcc', 'aaabbbccc', 'abc', 'ac']
        print("\nParsing test strings:")
        for s in test_strings:
            print(f"'{s}': {'Accepted' if parser.parse(s) else 'Rejected'}")


if __name__ == "__main__":
    main()