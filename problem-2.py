from logic import *


# Let propositional variable R be that “It is raining,” 
# the variable C be that “It is cloudy,” 
# and the variable S be that “It is sunny.” 

# Which of the following a propositional logic representation of the sentence “If it is raining, then it is cloudy and not sunny.”?

# (R → C) ∧ ¬S
# R → C → ¬S
# R ∧ C ∧ ¬S
# R → (C ∧ ¬S)
# (C ∨ ¬S) → R

raining = Symbol("R")
cloudy = Symbol("C")
sunny = Symbol("S")

knowledge = Implication(raining, And(cloudy, Not(sunny)))

print(knowledge.formula())
