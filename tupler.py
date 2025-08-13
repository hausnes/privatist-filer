# Eksempel på at tupler er uforanderlige (immutable) i Python

# Oppretter en tuple
min_tuple = (1, 2, 3)

# Prøver å endre et element i tuplen
try:
    min_tuple[0] = 10
except TypeError as e:
    print("Feil:", e)

# Output:
# Feil: 'tuple' object does not support item assignment