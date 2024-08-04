from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA

setinteger2setstrings = lambda int_set: {str(i) for i in int_set}

dict2strdict = lambda input_dict: {str(k): {str(sub_k): str(sub_v) for sub_k, sub_v in v.items()} for k, v in input_dict.items()}

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
    
    def transition(self, state, symbol):
        return self.transitions[state].get(symbol, None)

    def print(self):
        print("States: ", self.states)
        print("Alphabet: ", self.alphabet),
        print("Transitions: ")
        for state, transition in self.transitions.items():
            for symbol, next_state in transition.items():
                print(f"  {state} --({symbol})--> {next_state}")
        print("Initial State: ", self.initial_state)
        print("Accepting States: ", self.accepting_states)

    def plot(self):
        print(self.transitions)
        vdfa = VisualDFA(
            states=setinteger2setstrings(self.states),#{"q0", "q1", "q2", "q3", "q4"},
            input_symbols=setinteger2setstrings(self.alphabet), #{"0", "1"},
            transitions=dict2strdict(self.transitions),
            initial_state=str(self.initial_state),
            final_states=setinteger2setstrings(self.accepting_states),
        )
        vdfa.show_diagram(view=True)

def remove_unreachable_states(dfa):
    reachable = set()
    worklist = [dfa.initial_state]#this is a stack 

    #we search in the automata as a graph with dfs
    while worklist:
        state = worklist.pop()
        if state not in reachable:
            reachable.add(state)
            for symbol in dfa.alphabet:
                next_state = dfa.transition(state, symbol)
                if next_state is not None:
                    worklist.append(next_state)
    return reachable

def initial_partition(dfa):
    accepting_states = {state for state in dfa.states if state in dfa.accepting_states}
    non_accepting_states = dfa.states - accepting_states #set operation
    return [non_accepting_states, accepting_states] if non_accepting_states else [accepting_states]

def refine_partition(dfa, partition):
    new_partition = []
    for group in partition:
        subgroups = {}
        for state in group:
            signature = tuple(next((i for i, p in enumerate(partition) if dfa.transition(state, symbol) in p), None) for symbol in dfa.alphabet)
            if signature not in subgroups:
                subgroups[signature] = set()
            subgroups[signature].add(state)
        new_partition.extend(subgroups.values())
    return new_partition

def minimize_dfa(dfa):
    reachable_states = remove_unreachable_states(dfa)
    dfa.states = reachable_states
    partition = initial_partition(dfa)#Mark pairs where one is a final state and the other is not
    
    while True:
        new_partition = refine_partition(dfa, partition)
        if new_partition == partition:
            break
        partition = new_partition
    
    return partition

def solve():
    states_n = int(input())
    alphabet = input().split()
    accepting_states = set(map(int, input().split()))
    
    transitions = {}
    for _ in range(states_n):
        parts = list(map(int, input().split()))
        state = parts[0]
        transitions[state] = {symbol: parts[i+1] for i, symbol in enumerate(alphabet)}

    initial_state = 0
    states = set(range(states_n))
    dfa = DFA(states, set(alphabet), transitions, initial_state, accepting_states)
    dfa.print()
    dfa.plot()
    partition = minimize_dfa(dfa)
    dfa.print()
    
    # Sort the partition groups and the states within each group
    sorted_partition = sorted([sorted(group) for group in partition if len(group) > 1])
    
    # Format the output
    output = ' '.join(f"({','.join(map(str, group))})" for group in sorted_partition)
    print(output)
    print()

for _ in range(int(input())):
    solve()