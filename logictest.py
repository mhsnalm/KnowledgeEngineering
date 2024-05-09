from logic import *

idea = Symbol("Idea")
product = Symbol("Product")
platform = Symbol("Platform")
team = Symbol("Team")
capital = Symbol("Capital")

knowledge = And(
    Implication(idea, product),
    And(team, platform),
    capital,
)

print(model_check(knowledge, product))
