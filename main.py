import pyttsx3

if __name__ == '__main__':

    intro = "Welcome to Shehryar's Robo Speaker!. Please enter what you want me to speak"
    print("Welcome To Shehryar's RoboSpeaker!!\n")
    engine = pyttsx3.init()
    for i in range (1):
        engine.say(intro)
        engine.runAndWait()
        i=2

    while True:
        x = input("Enter what you want to speak: ")
        if x == 'end chat':
            break
        engine.say(x)
        engine.runAndWait()