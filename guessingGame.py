from random import randint

def main():
    larger = int(input("Enter Larger Number"))
    smaller = int(input("Enter Smaller Number"))

    comNumber = randint(smaller,larger)

    while True:
        userInput = int(input("Enter your guess"))
        if userInput > comNumber:
            print("Too large")
        elif userInput < comNumber:
            print("Too small")
        else:
            print("You got it!")
            break
if __name__=="__main__":
    main()
