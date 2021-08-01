from time import sleep
from playsound import playsound
from threading import Thread
import os
from termcolor import colored
from colorama import init, Fore, Back, Style

audio='bday_song.wav'


def playAudio():
    if playAudio:
       playsound(audio)

def printWish():
 	with open('ascii/cake.txt', 'r') as f:
 		for line in f:
 		#print("\u001b[31m.".rstrip())
 			print(line.rstrip())
 			sleep(0.04)
 	f.close()

 	sleep(1)

 	with open('ascii/msg.txt', 'r') as f:
 		for line in f:
 		#print("\u001b[31m.".rstrip())
 			print(line.rstrip())
 			sleep(0.5)
 	f.close()

 	'''with open('ascii/1.txt', 'r') as f:
 		for line in f:
 		#print("\u001b[31m.".rstrip())
 			print(line.rstrip())
 			sleep(0.04)
 	f.close()'''


os.system('cls' if os.name == 'nt' else 'clear')
Thread(target = playAudio).start()
Thread(target = printWish).start()