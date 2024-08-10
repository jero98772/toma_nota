from automata.fa.dfa import DFA
import time
from visual_automata.fa.dfa import VisualDFA #pip install visual-automata
import itertools

setinteger2setstrings = lambda int_set: {str(i) for i in int_set}
dict2strdict = lambda input_dict: {str(k): {str(sub_k): str(sub_v) for sub_k, sub_v in v.items()} for k, v in input_dict.items()}

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

class DFA:
    """
    class deterministic finite automata to hanlde more easy
    """
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def get_transition(self, state, symbol):
        return self.transitions.get((state, symbol), None)

    def print(self):
        print("States: ", self.states)
        print("Alphabet: ", self.alphabet),
        print("Transitions: ",self.transitions)
        print("Initial State: ", self.initial_state)
        print("Accepting States: ", self.accepting_states)

    def plot(self):
        print(self.transitions)
        vdfa = VisualDFA(
            states=setinteger2setstrings(self.states),#{"q0", "q1", "q2", "q3", "q4"},
            input_symbols=setinteger2setstrings(self.alphabet), #{"0", "1"},
            transitions=convert_transitions(self.transitions),#dict2strdict(self.transitions),
            initial_state=str(self.initial_state),
            final_states=setinteger2setstrings(self.accepting_states),
        )
        vdfa.show_diagram(view=True)
        time.sleep(1)

def generate_combinations(elements, combination_length):
    return list(itertools.combinations(elements, combination_length))



def convert_transitions(input_dict):
    """
    function for format data
    """
    transitions = {}
    for (state, symbol), next_state in input_dict.items():
        state_str = str(state)
        next_state_str = str(next_state)
        if state_str not in transitions:
            transitions[state_str] = {}
        transitions[state_str][symbol] = next_state_str
    
    return transitions

def remove_unreachable_states(dfa):
    reachable = set()
    worklist = [dfa.initial_state]#this is a stack 

    #we search in the automata as a graph with dfs
    while worklist:
        state = worklist.pop()
        if state not in reachable:
            reachable.add(state)
            for symbol in dfa.alphabet:
                next_state = dfa.get_transition(state, symbol)
                if next_state is not None:
                    worklist.append(next_state)
    return reachable

def parse_transitions(input_data,headers):
    lines = input_data.strip().split('\n')
    #headers = lines[0].split()
    transitions = {}
    
    for line in lines:
        values = line.split()
        state = int(values[0])
        for i, header in enumerate(headers):
            transitions[(state, header)] = int(values[i + 1])
    
    return transitions

def minimize_dfa(dfa,gui=False):
    # Initialize the table of unmarked pairs
    pairs = [(p, q) for p in dfa.states for q in dfa.states if p != q]
    if gui:
        print(f"{GREEN}Initialize the table of unmarked pairs{RESET}")
        for i in pairs:
            print(f"{BLUE}{i}{RESET}")

    marked = set()

    # Step 2: Mark pairs with different acceptance status
    for (p, q) in pairs:
        if (p in dfa.accepting_states) != (q in dfa.accepting_states):
            #if not( (p, q) in marked or (q,p) in marked ):
            marked.add((p, q))

    if gui:         
        print(f"{GREEN}Step 2: Mark pairs with different acceptance status{RESET}")
        for i in marked:
            print(f"{BLUE}{i}{RESET}")

    # Step 3: Propagate markings
    changes = True
    while changes:
        changes = False
        new_marked = set(marked)
        for (p, q) in pairs:
            if (p, q) in marked:
                continue
            for symbol in dfa.alphabet:
                p_next = dfa.get_transition(p, symbol)
                q_next = dfa.get_transition(q, symbol)
                if p_next is not None and q_next is not None:
                    if (p_next, q_next) in marked:
                        new_marked.add((p, q))
                        changes = True
                        break
        marked = new_marked
    if gui:
        print(f"{GREEN}Step 3: Propagate markings{RESET}")
        for i in marked:
            print(f"{BLUE}{i}{RESET}")

    # Step 4: Determine equivalent states
    equivalence_classes = []
    for (p, q) in pairs:
        if (p, q) not in marked:
            found = False
            for eq_class in equivalence_classes:
                if p in eq_class or q in eq_class:
                    eq_class.add(p)
                    eq_class.add(q)
                    found = True
                    break
            if not found:
                equivalence_classes.append({p, q})
    for i in equivalence_classes:
        if len(i)>2:
            equivalence_classes.remove(i)
            for ii in generate_combinations(i,2):
                equivalence_classes.append(ii)

    if gui:
        print(f"{GREEN}Step 4: Determine equivalent states{RESET}")
        for i in equivalence_classes:
            print(f"{BLUE}{i}{RESET}")
    
    return equivalence_classes


def solve(gui=True):
    states_n = int(input())
    alphabet = input().split()
    accepting_states = set(map(int, input().split()))
    
    transitions = ""
    for _ in range(states_n):
        transitions+=input()+"\n"
    transitions=parse_transitions(transitions,alphabet)
    #print(transitions)

    initial_state = 0
    states = set(range(states_n))
    dfa = DFA(states, set(alphabet), transitions, initial_state, accepting_states)
    states=remove_unreachable_states(dfa)
    dfa.states=states
    if gui:
        dfa.print()
        dfa.plot()

    partition = minimize_dfa(dfa,gui=True)
    if gui:
        print(partition)

    
    # Sort the partition groups and the states within each group
    sorted_partition = sorted([sorted(group) for group in partition if len(group) > 1])
    
    # Format the output
    output = ' '.join(f"({','.join(map(str, group))})" for group in sorted_partition)
    print(output)
    if gui:print()

for _ in range(int(input())):
    print("test #",_)
    solve(gui=False)
