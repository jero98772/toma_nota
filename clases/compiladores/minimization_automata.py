class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states
    
    def transition(self, state, symbol):
        return self.transitions[state].get(symbol, None)

#Remove unreachable states
#This ensures that only the states that can be reached from the initial state are considered.
def remove_unreachable_states(dfa):
    reachable = set()
    worklist = [dfa.initial_state]
    while worklist:
        state = worklist.pop()
        if state not in reachable:
            reachable.add(state)
            for symbol in dfa.alphabet:
                next_state = dfa.transition(state, symbol)
                if next_state:
                    worklist.append(next_state)
    return reachable

#Initial partition: The initial division of states into accepting and non-accepting states sets the stage for refinement.
def initial_partition(dfa):
    accepting_states = {state for state in dfa.states if state in dfa.accepting_states}
    non_accepting_states = dfa.states - accepting_states
    return [accepting_states, non_accepting_states]

#Refine partition: This step iteratively splits the groups based on their transitions until no further splits are possible.
def refine_partition(dfa, partition):
    new_partition = []
    for group in partition:
        subgroups = {}
        for state in group:
            signature = tuple(dfa.transition(state, symbol) in partition for symbol in dfa.alphabet)
            if signature not in subgroups:
                subgroups[signature] = set()
            subgroups[signature].add(state)
        new_partition.extend(subgroups.values())
    return new_partition

def minimize_dfa(dfa):
    reachable_states = remove_unreachable_states(dfa)
    partition = initial_partition(dfa)
    
    while True:
        new_partition = refine_partition(dfa, partition)
        if new_partition == partition:
            break
        partition = new_partition
    
    return partition
#Create the minimized DFA: Constructs the new minimized DFA based on the final partition.
def create_minimized_dfa(dfa, partition):
    state_mapping = {}
    new_states = set()
    new_accepting_states = set()
    new_transitions = {}
    for i, group in enumerate(partition):
        representative = next(iter(group))
        for state in group:
            state_mapping[state] = i
        new_states.add(i)
        if representative in dfa.accepting_states:
            new_accepting_states.add(i)
    
    for group in partition:
        representative = next(iter(group))
        new_state = state_mapping[representative]
        new_transitions[new_state] = {}
        for symbol in dfa.alphabet:
            original_next_state = dfa.transition(representative, symbol)
            if original_next_state:
                new_transitions[new_state][symbol] = state_mapping[original_next_state]
    
    new_initial_state = state_mapping[dfa.initial_state]
    return DFA(new_states, dfa.alphabet, new_transitions, new_initial_state, new_accepting_states)

# Example DFA
states = {0, 1, 2, 3}
alphabet = {'a', 'b'}
transitions = {
    0: {'a': 1, 'b': 2},
    1: {'a': 0, 'b': 3},
    2: {'a': 3, 'b': 0},
    3: {'a': 2, 'b': 1}
}
initial_state = 0
accepting_states = {0, 3}

dfa = DFA(states, alphabet, transitions, initial_state, accepting_states)
reachable_states = remove_unreachable_states(dfa)
partition = minimize_dfa(dfa)
minimized_dfa = create_minimized_dfa(dfa, partition)

# Print the minimized DFA
print("Minimized DFA states:", minimized_dfa.states)
print("Minimized DFA transitions:", minimized_dfa.transitions)
print("Minimized DFA initial state:", minimized_dfa.initial_state)
print("Minimized DFA accepting states:", minimized_dfa.accepting_states)
