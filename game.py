import random

def main():

    print("Rolling dice...")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print("Die 1:" + str(d1))
    print("Die 2:" + str(d2))
    print("Total value: " + str(total))
    if total > 7: print("You won")
    else: print("You lose")


if __name__ == "__main__":
  main()