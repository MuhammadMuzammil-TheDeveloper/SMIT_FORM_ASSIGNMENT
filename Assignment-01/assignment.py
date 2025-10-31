def get_regex_and_dfa(choice, alphabet):
    """Return the Regular Expression, Transition Table, and Final States based on user choice."""
    if choice == 1:  # Starts with 'a'
        regex = f"a({'|'.join(alphabet)})*"
        transitions = {
            "q0": {"a": "q1", "b": "q_dead"},
            "q1": {"a": "q1", "b": "q1"},
            "q_dead": {"a": "q_dead", "b": "q_dead"}
        }
        final_states = ["q1"]

    elif choice == 2:  # Ends with 'a'
        regex = f"({'|'.join(alphabet)})*a"
        transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q1", "b": "q0"}
        }
        final_states = ["q1"]

    elif choice == 3:  # Contains 'a'
        regex = f"({'|'.join(alphabet)})*a({'|'.join(alphabet)})*"
        transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q1", "b": "q1"}
        }
        final_states = ["q1"]

    elif choice == 4:  # Has exactly one 'a'
        regex = "b*a b*".replace(" ", "")
        transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q_dead", "b": "q1"},
            "q_dead": {"a": "q_dead", "b": "q_dead"}
        }
        final_states = ["q1"]

    elif choice == 5:  # Has even number of 'a'
        regex = "(b*(a b* a b*)*)".replace(" ", "|")
        transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q0", "b": "q1"}
        }
        final_states = ["q0"]

    elif choice == 6:  # Has odd number of 'a'
        regex = "(b*(a b* a b*)* a b*)".replace(" ", "|")
        transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q0", "b": "q1"}
        }
        final_states = ["q1"]

    elif choice == 7:  # Alternate a and b
        regex = "(ab|ba)*"
        transitions = {
            "q0": {"a": "q1", "b": "q2"},
            "q1": {"a": "q_dead", "b": "q0"},
            "q2": {"a": "q0", "b": "q_dead"},
            "q_dead": {"a": "q_dead", "b": "q_dead"}
        }
        final_states = ["q0"]

    elif choice == 8:  # Even a and b
        regex = "(a|b)*(aa|bb)*(a|b)*"
        transitions = {
            "q0": {"a": "q1", "b": "q2"},
            "q1": {"a": "q0", "b": "q3"},
            "q2": {"a": "q3", "b": "q0"},
            "q3": {"a": "q2", "b": "q1"}
        }
        final_states = ["q0"]

    elif choice == 9:  # Contains aa
        regex = f"({'|'.join(alphabet)})*aa({'|'.join(alphabet)})*"
        transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q2", "b": "q0"},
            "q2": {"a": "q2", "b": "q2"}
        }
        final_states = ["q2"]

    elif choice == 10:  # Contains bb
        regex = f"({'|'.join(alphabet)})*bb({'|'.join(alphabet)})*"
        transitions = {
            "q0": {"b": "q1", "a": "q0"},
            "q1": {"b": "q2", "a": "q0"},
            "q2": {"a": "q2", "b": "q2"}
        }
        final_states = ["q2"]

    else:
        return None, None, None

    return regex, transitions, final_states


def display_transition_table(transitions, alphabet):
    """Display the DFA transition table."""
    print("\n╔══════════════════════════════════╗")
    print("║          TRANSITION TABLE         ║")
    print("╚══════════════════════════════════╝")
    header = "State\t" + "\t".join(alphabet)
    print(header)
    print("-" * len(header.expandtabs()))
    for state, paths in transitions.items():
        row = state + "\t" + "\t".join(paths.get(symbol, "-") for symbol in alphabet)
        print(row)
    print("-" * len(header.expandtabs()))


def simulate_dfa(transitions, final_states, input_string):
    """Simulate DFA for a given input string."""
    current_state = "q0"
    print("\n╔══════════════════════════════════╗")
    print("║        DFA SIMULATION STEPS       ║")
    print("╚══════════════════════════════════╝")

    for i, symbol in enumerate(input_string, 1):
        if symbol not in transitions[current_state]:
            print(f"❌ Invalid symbol '{symbol}' for state {current_state}")
            return False
        next_state = transitions[current_state][symbol]
        print(f"Step {i}: δ({current_state}, {symbol}) → {next_state}")
        current_state = next_state

    print(f"\nFinal State: {current_state}")
    result = current_state in final_states
    print("════════════════════════════════════")
    print("✅ Result: ACCEPTED" if result else "❌ Result: REJECTED")
    print("════════════════════════════════════")
    return result


def add_custom_dfa():
    """Allow user to define their own DFA (update functionality)."""
    print("\n--- Add Your Own Custom DFA ---")
    states = input("Enter states (comma separated): ").split(",")
    alphabet = input("Enter alphabet (comma separated): ").split(",")
    transitions = {}

    print("\nDefine transitions:")
    for state in states:
        transitions[state] = {}
        for symbol in alphabet:
            next_state = input(f"δ({state}, {symbol}) = ")
            transitions[state][symbol] = next_state

    final_states = input("Enter final states (comma separated): ").split(",")
    return transitions, final_states, alphabet


if __name__ == "__main__":
    print("\n🎯 DFA & REGEX SIMULATOR 🎯")
    print("───────────────────────────────")

    alphabet = input("Enter the alphabet (comma separated, e.g. a,b): ").replace(" ", "").split(",")

    print("\nAvailable Conditions:")
    conditions = [
        "Starts with a",
        "Ends with a",
        "Contains a",
        "Has exactly one a",
        "Has even number of a",
        "Has odd number of a",
        "Alternate a and b",
        "Even a and b",
        "Contains aa",
        "Contains bb",
        "➕ Add your own DFA (custom)"
    ]

    for i, cond in enumerate(conditions, 1):
        print(f"{i}. {cond}")

    try:
        choice = int(input("\nEnter the number of your chosen condition (1–11): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 11.")
        exit()

    if choice == 11:
        transitions, final_states, alphabet = add_custom_dfa()
        regex = "Custom DFA (user-defined)"
    else:
        regex, transitions, final_states = get_regex_and_dfa(choice, alphabet)

    if not regex:
        print("Invalid choice entered.")
    else:
        print(f"\n📘 Selected Condition: {conditions[choice - 1]}")
        print(f"📗 Regular Expression: {regex}")
        display_transition_table(transitions, alphabet)
        input_string = input("\nEnter a string to test: ")
        simulate_dfa(transitions, final_states, input_string)
