import random

def main():
    print("What is your name?")
    name = input()
    print("Hello," + name + "!")

    print("Rolling dice...")
    
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print("Die 1:" + str(d1))
    print("Die 2:" + str(d2))
    print("Total value: " + str(total))


if __name__ == "__main__":
  main()