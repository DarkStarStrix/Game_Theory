import random
import matplotlib.pyplot as plt


def prisoner_dilemma_round(strategy1, strategy2, history1, history2):
    choice1 = strategy1 (history1, history2)
    choice2 = strategy2 (history2, history1)
    return choice1, choice2


def tit_for_tat(history1, history2):
    if not history2:
        return 'C'
    return history2 [-1]


def self_preservation_tft(history1, history2):
    if not history2:
        return 'C'
    if history2 [-1] == 'D':
        return 'D'
    return 'C'


def always_cooperate(history1, history2):
    return 'C'


def always_defect(history1, history2):
    return 'D'


def random_strategy(history1, history2):
    return random.choice (['C', 'D'])


def convert_to_numerical(history):
    return [1 if choice == 'C' else 0 for choice in history]


# List of strategies
strategies = [always_cooperate, always_defect, random_strategy]

# Number of rounds
rounds = 10

# Conduct simulations
simulation_results = {}
for strategy in strategies:
    history1, history2 = [], []
    for _ in range (rounds):
        choice1, choice2 = prisoner_dilemma_round (self_preservation_tft, strategy, history1, history2)
        history1.append (choice1)
        history2.append (choice2)
    simulation_results [strategy.__name__] = history1, history2

# Visualize the results
plt.figure (figsize=(15, 10))
for i, (strategy_name, (history1, history2)) in enumerate (simulation_results.items (), 1):
    plt.subplot (3, 1, i)
    numerical_history1 = convert_to_numerical (history1)
    numerical_history2 = convert_to_numerical (history2)
    plt.plot (range (1, 11), numerical_history1, 'o-', label='Self-Preservation + TFT')
    plt.plot (range (1, 11), numerical_history2, 's-', label=strategy_name)
    plt.title (f'Self-Preservation + TFT vs {strategy_name}')
    plt.xlabel ('Round')
    plt.ylabel ('Choice (1 for Cooperate, 0 for Defect)')
    plt.xticks (range (1, 11))
    plt.yticks ([0, 1], ['D', 'C'])
    plt.legend ()
    plt.grid (True)

plt.tight_layout ()
plt.show ()
