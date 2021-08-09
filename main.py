from time import sleep
from playsound import playsound
from threading import Thread
import os
# import required module
from playsound import playsound

COLORS = {\
"red": "\u001b[31;1m",
"green":"\u001b[32;1m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35;1m",
"cyan": "\u001b[36m",
"white":"\u001b[37;1m",
"bred":"\u001b[31;1m",
"reset":"\u001b[0m",
}
        

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

def printMSG():
 	with open('ascii/msg.txt', 'r') as f:
 		for line in f:
 			colorText(line)
 			print(colorText(line).rstrip())
 			sleep(0.5)
 	f.close()


def printCake():
 	with open('ascii/cake.txt', 'r') as f:
 		for line in f:
 			colorText(line)
 			print(colorText(line).rstrip())
 			sleep(0.5)
 	f.close()

def printWish():
	with open('ascii/1.txt', 'r') as f:
		for line in f:
			colorText(line)
			print(colorText(line).rstrip())
			sleep(0.2)
	f.close()

def mainFun():
	printCake();
	sleep(0.8)
	printMSG();
	sleep(0.8)	
	printWish();
	sleep(3)
	print("\u001b[31;1m","\tFirst of all sorry if i ever give you any trouble...")
	sleep(1)
	print("\tActually UR really special so thought i should wish you in geeky way instead of just text ^_^ ")
	sleep(1)
	print("\tHope you like this! ♥ \u001b[0m")

def playAudio():
	playsound('song.mp3')
	'''if playAudio:
		playsound('music.mp3')'''



os.system('cls' if os.name == 'nt' else 'clear')
Thread(target = playAudio).start()
Thread(target = mainFun).start()

