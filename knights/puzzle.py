from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Implication(And(AKnight, AKnave), AKnight),
    Implication(Not(And(AKnight, AKnave)), AKnave)
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(And(AKnave, BKnave), AKnight),
    Implication(Not(And(AKnave, BKnave)), AKnave),
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnave, BKnight),
    Implication(AKnight, BKnave)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnight, Biconditional(BKnight, AKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnight, Biconditional(AKnight, BKnave)),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    Implication(And(AKnave, CKnave), BKnight),
    Implication(And(AKnight, CKnight), BKnave),
    Implication(AKnave, Not(AKnave)),
    Implication(CKnave, Not(CKnave)),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(CKnave, Not(CKnight)),
    Or(And(And(AKnave, CKnave), BKnight), And(And(AKnight, CKnight), BKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
