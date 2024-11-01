from typing import Dict, Set, List, Tuple
import sys


class Grammar:
    """
    A class representing a context-free grammar.

    Attributes:
        productions (Dict[str, List[str]]): A dictionary mapping each non-terminal to a list of its productions.
        terminals (Set[str]): A set of terminal symbols in the grammar.
        non_terminals (Set[str]): A set of non-terminal symbols in the grammar.
        start_symbol (str): The starting non-terminal symbol of the grammar, default is 'S'.
    """
    def __init__(self):
        """
        Initializes a new instance of the Grammar class.

        Sets up empty productions, terminals, and non-terminals. Initializes the start symbol to 'S'.
        """
        self.productions: Dict[str, List[str]] = {}
        self.terminals: Set[str] = set()
        self.non_terminals: Set[str] = set()
        self.start_symbol: str = 'S'
    def add_production(self, non_terminal: str, production: str):
        """
        Adds a production rule to the grammar.

        Args:
            non_terminal (str): The non-terminal symbol that generates the production.
            production (str): The production string, which can consist of terminals and non-terminals.

        If the non-terminal does not already exist in the productions dictionary, it is added.
        The production is then appended to the list of productions for that non-terminal.
        Additionally, the non-terminal is added to the set of non-terminals, and each symbol in
        the production is checked. If it is a terminal (lowercase letter) or ε (epsilon),
        it is added to the set of terminals.
        """
        if non_terminal not in self.productions:
            self.productions[non_terminal] = []
        self.productions[non_terminal].append(production)
        self.non_terminals.add(non_terminal)
        for symbol in production:
            if symbol.islower() or symbol == 'e':
                self.terminals.add(symbol)

    def compute_first_sets(self) -> Dict[str, Set[str]]:
        """
        Computes the FIRST sets for a given context-free grammar.

        The FIRST set of a non-terminal is the set of terminals that begin the strings derivable from that non-terminal.
        If a non-terminal can derive the empty string (ε), ε is also included in its FIRST set.

        The function processes each production rule of the grammar and iteratively updates the FIRST sets until no more changes occur.

        Returns:
            Dict[str, Set[str]]: A dictionary where keys are non-terminals and terminals, and values are sets containing
            the corresponding FIRST sets.
        """
        first: Dict[str, Set[str]] = {nt: set() for nt in self.non_terminals}
        first.update({t: {t} for t in self.terminals})
        
        # Epsilon represented by 'e' should be in first of 'e' itself
        first['e'] = {'e'}

        # Repeat until no changes
        while True:
            updated = False
            for nt in self.non_terminals:
                for production in self.productions[nt]:
                    all_nullable = True
                    for symbol in production:
                        # Add FIRST(symbol) to FIRST(nt), except for epsilon
                        first_set_before = first[nt].copy()
                        first[nt].update(first[symbol] - {'e'})
                        
                        # Check if symbol can derive epsilon
                        if 'e' not in first[symbol]:
                            all_nullable = False
                            break

                        # Continue only if symbol can derive epsilon
                    # If all symbols in production can derive epsilon, add epsilon to FIRST(nt)
                    if all_nullable:
                        first[nt].add('e')
                    
                    if first_set_before != first[nt]:
                        updated = True
                        
            # Stop if no changes were made
            if not updated:
                break

        return first

def compute_follow_sets(self, first: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """
    Computes the FOLLOW sets for a given context-free grammar.

    The FOLLOW set of a non-terminal is the set of terminals that can appear immediately to the right 
    of that non-terminal in some sentential form. It also includes the end-of-input marker '$' 
    for the start symbol.

    Args:
        first (Dict[str, Set[str]]): A dictionary where keys are non-terminals and terminals, 
        and values are sets containing their corresponding FIRST sets.

    Returns:
        Dict[str, Set[str]]: A dictionary where keys are non-terminals and values are sets 
        containing the corresponding FOLLOW sets.
    """

    # Initialize the FOLLOW sets for each non-terminal to be empty
    follow: Dict[str, Set[str]] = {nt: set() for nt in self.non_terminals}
    # Add the end-of-input marker '$' to the FOLLOW set of the start symbol
    follow[self.start_symbol].add('$')

    while True:  # Loop until no more updates are made to FOLLOW sets
        updated = False  # Flag to track if any FOLLOW set has been updated

        # Iterate through each non-terminal
        for nt in self.non_terminals:
            # Iterate through each production of the current non-terminal
            for production in self.productions[nt]:
                # Iterate through each symbol in the production
                for i, symbol in enumerate(production):
                    # Check if the symbol is a non-terminal
                    if symbol in self.non_terminals:
                        # If the symbol is the last one in the production
                        if i == len(production) - 1:
                            # Update the FOLLOW set of the non-terminal if it does not already contain FOLLOW(nt)
                            if not follow[symbol].issuperset(follow[nt]):
                                follow[symbol].update(follow[nt])
                                updated = True  # Mark that an update occurred
                        else:
                            # Get the rest of the production after the current symbol
                            rest = production[i + 1:]
                            # Compute the FIRST set of the rest of the production
                            first_of_rest = self.compute_first_of_string(rest, first)
                            
                            # Update FOLLOW set with FIRST of the rest (excluding ε)
                            if not follow[symbol].issuperset(first_of_rest - {'e'}):
                                follow[symbol].update(first_of_rest - {'e'})
                                updated = True  # Mark that an update occurred
                            
                            # If the FIRST of the rest contains ε (epsilon)
                            if 'e' in first_of_rest:
                                # Update the FOLLOW set with FOLLOW(nt)
                                if not follow[symbol].issuperset(follow[nt]):
                                    follow[symbol].update(follow[nt])
                                    updated = True  # Mark that an update occurred
        
        # If no updates were made in this iteration, break the loop
        if not updated:
            break

    # Return the computed FOLLOW sets
    return follow
def compute_first_of_string(self, string: str, first: Dict[str, Set[str]]) -> Set[str]:
    """
    Computes the FIRST set for a given string (sequence of symbols) in a context-free grammar.

    The FIRST set of a string is the set of terminals that can appear as the first symbol 
    in any string derived from that string. If the string can derive ε (the empty string), 
    it is also included in the FIRST set.

    Args:
        string (str): A sequence of symbols (non-terminals and terminals) for which to compute the FIRST set.
        first (Dict[str, Set[str]]): A dictionary where keys are non-terminals and terminals, 
        and values are sets containing their corresponding FIRST sets.

    Returns:
        Set[str]: A set containing the terminals that can appear as the first symbol of the input string, 
        including 'e' if the string can derive the empty string.
    """

    if not string:  # If the string is empty, return the set containing ε
        return {'e'}
    
    result = set()  # Initialize the result set for the FIRST set
    for symbol in string:  # Iterate through each symbol in the string
        symbol_first = first[symbol]  # Get the FIRST set of the current symbol
        result.update(symbol_first - {'e'})  # Add all terminals except ε to the result set
        if 'e' not in symbol_first:  # If ε is not in the FIRST set of the symbol, stop here
            return result
    
    result.add('e')  # If all symbols can derive ε, add ε to the result set
    return result  # Return the computed FIRST set for the string


def parse_input() -> List[Grammar]:
    """
    Parses a series of grammars from user input and returns a list of Grammar objects.

    The function expects input in the following format:
    - The first line contains an integer `n`, representing the number of grammars.
    - For each grammar:
      - The first line contains an integer `m`, representing the number of non-terminal symbols.
      - The next `m` lines define the production rules for each non-terminal.
          - Each line starts with a non-terminal symbol followed by one or more productions, separated by spaces.
          - Each production is a sequence of terminal and/or non-terminal symbols without spaces.

    For example:
        3
        2
        S AS A
        A a
        3
        S AB
        A aA a
        B bBc bc
        2
        S A
        A A b

    Returns:
        List[Grammar]: A list of Grammar objects, each representing a parsed grammar with its production rules.
    
    """
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