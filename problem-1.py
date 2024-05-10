from logic import *


# Consider these logical sentences:

# 1. If Hermione is in the library, then Harry is in the library.
# 2. Hermione is in the library.
# 3. Ron is in the library and Ron is not in the library.
# 4. Harry is in the library.
# 5. Harry is not in the library or Hermione is in the library.
# 6. Ron is in the library or Hermione is in the library.

# Which of the following logical entailments is true?

# a. Sentence 6 entails Sentence 2 - result false
# b. Sentence 1 entails Sentence 4 - result false
# c. Sentence 6 entails Sentence 3 - result false
# d. Sentence 2 entails Sentence 5 - result true
# e. Sentence 1 entails Sentence 2 - result false
# f. Sentence 5 entails Sentence 6 - result false


hermioneLibrary = Symbol("HermioneLibrary")
harryLibrary = Symbol("HarryLibrary")
ronLibrary = Symbol("RonLibrary")

# a
# knowledge = Or(ronLibrary, hermioneLibrary)
# print(model_check(knowledge, hermioneLibrary))

# b
# knowledge = Implication(hermioneLibrary, harryLibrary)
# print(knowledge.formula())
# print(model_check(knowledge, harryLibrary))

# c
# knowledge = Or(ronLibrary, hermioneLibrary)
# print(knowledge.formula())
# print(model_check(knowledge, And(Not(ronLibrary),ronLibrary)))

# d
# knowledge = (hermioneLibrary)
# print(knowledge.formula())
# print(model_check(knowledge, Or(Not(harryLibrary),hermioneLibrary)))

# e
# knowledge = Implication(hermioneLibrary, harryLibrary)
# print(knowledge.formula())
# print(model_check(knowledge, hermioneLibrary))

# f
knowledge = Or(Not(harryLibrary),hermioneLibrary)
print(knowledge.formula())
print(model_check(knowledge, Or(ronLibrary, hermioneLibrary)))