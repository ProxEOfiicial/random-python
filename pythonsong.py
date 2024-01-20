import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds")
        time.sleep(1)
    
    print("Blast off!")

def sing_python_song():
    print("I'm a little Python, short and stout")
    print("Here is my script, here is my output")
    print("When I get all worked up, hear me shout")
    print("Run me now and see what I'm about!")

def main():
    print("Welcome to the Python Countdown and Song Extravaganza!")
    
    try:
        seconds = int(input("Enter the countdown duration in seconds: "))
        countdown(seconds)
    except ValueError:
        print("Oops! That's not a valid number. Let's just sing a Python song instead.")
    
    sing_python_song()

if __name__ == "__main__":
    main()
