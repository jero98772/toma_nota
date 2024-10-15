from typing import Dict, Set, List, Tuple
from grammar_parser import Grammar, format_set,parse_input  # Assuming the previous code is in grammar_parser.py

class Item:
    def __init__(self, left: str, right: str, dot_position: int):
        self.left = left
        self.right = right
        self.dot_position = dot_position

    def __eq__(self, other):
        return (self.left, self.right, self.dot_position) == (other.left, other.right, other.dot_position)

    def __hash__(self):
        return hash((self.left, self.right, self.dot_position))

    def __str__(self):
        return f"{self.left} -> {self.right[:self.dot_position]}.{self.right[self.dot_position:]}"

class BottomUpParser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.first_sets = self.grammar.compute_first_sets()
        self.follow_sets = self.grammar.compute_follow_sets(self.first_sets)
        self.canonical_collection: List[Set[Item]] = []
        self.goto_table: Dict[Tuple[int, str], int] = {}
        self.action_table: Dict[Tuple[int, str], str] = {}

    def closure(self, items: Set[Item]) -> Set[Item]:
        result = set(items)
        while True:
            new_items = set()
            for item in result:
                if item.dot_position < len(item.right) and item.right[item.dot_position] in self.grammar.non_terminals:
                    next_symbol = item.right[item.dot_position]
                    for production in self.grammar.productions[next_symbol]:
                        new_item = Item(next_symbol, production, 0)
                        if new_item not in result:
                            new_items.add(new_item)
            if not new_items:
                break
            result.update(new_items)
        return result

    def goto(self, items: Set[Item], symbol: str) -> Set[Item]:
        result = set()
        for item in items:
            if item.dot_position < len(item.right) and item.right[item.dot_position] == symbol:
                new_item = Item(item.left, item.right, item.dot_position + 1)
                result.add(new_item)
        return self.closure(result)

    def compute_canonical_collection(self):
        start_item = Item(self.grammar.start_symbol, self.grammar.productions[self.grammar.start_symbol][0], 0)
        initial_set = self.closure({start_item})
        self.canonical_collection.append(initial_set)
        
        symbols = self.grammar.terminals.union(self.grammar.non_terminals)
        
        i = 0
        while i < len(self.canonical_collection):
            for symbol in symbols:
                goto_set = self.goto(self.canonical_collection[i], symbol)
                if goto_set and goto_set not in self.canonical_collection:
                    self.canonical_collection.append(goto_set)
                    self.goto_table[(i, symbol)] = len(self.canonical_collection) - 1
                elif goto_set in self.canonical_collection:
                    self.goto_table[(i, symbol)] = self.canonical_collection.index(goto_set)
            i += 1

    def compute_parsing_table(self):
        self.compute_canonical_collection()
        
        for i, state in enumerate(self.canonical_collection):
            for item in state:
                if item.dot_position < len(item.right):
                    symbol = item.right[item.dot_position]
                    if symbol in self.grammar.terminals:
                        self.action_table[(i, symbol)] = f"shift {self.goto_table.get((i, symbol), -1)}"
                    elif symbol in self.grammar.non_terminals:
                        self.goto_table[(i, symbol)] = self.goto_table.get((i, symbol), -1)
                else:
                    if item.left == self.grammar.start_symbol:
                        self.action_table[(i, '$')] = "accept"
                    else:
                        for terminal in self.follow_sets[item.left]:
                            self.action_table[(i, terminal)] = f"reduce {item.left} -> {item.right}"

    def parse(self, input_string: str) -> bool:
        stack = [0]
        input_string += '$'
        index = 0

        while True:
            state = stack[-1]
            current_input = input_string[index]

            if (state, current_input) not in self.action_table:
                return False

            action = self.action_table[(state, current_input)]

            if action.startswith("shift"):
                stack.append(int(action.split()[1]))
                index += 1
            elif action.startswith("reduce"):
                production = action.split()[1]
                left, right = production.split(" -> ")
                for _ in range(len(right)):
                    stack.pop()
                stack.append(self.goto_table.get((stack[-1], left), -1))
            elif action == "accept":
                return True
            else:
                return False

def main():
    grammars = parse_input()

    for grammar in grammars:
        parser = BottomUpParser(grammar)
        parser.compute_parsing_table()

        print("Canonical Collection:")
        for i, state in enumerate(parser.canonical_collection):
            print(f"{i}: " + " ".join(str(item) for item in state))

        print("\nAction Table:")
        for (state, symbol), action in parser.action_table.items():
            print(f"({state}, {symbol}) -> {action}")

        print("\nGoto Table:")
        for (state, symbol), target in parser.goto_table.items():
            print(f"({state}, {symbol}) -> {target}")

        # Example parse
        input_string = input("Enter a string to parse: ")
        if parser.parse(input_string):
            print("String accepted.")
        else:
            print("String rejected.")

if __name__ == "__main__":
    main()
