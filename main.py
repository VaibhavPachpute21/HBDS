from time import 	sleep
from playsound import playsound
from threading import Thread
import os
from termcolor import colored
from colorama import init, Fore, Back, Style

audio='bday_song.wav'

cake=""" 

                   \\\ ,
                    \ `|
                     ) (   .-""-.
                     | |  /_  {  '.
                     | | (/ `\   } )
                     | |  ^/ ^`}   {
                     \  \ \=  ( {   )
                      \  \ '-, {   {{
                       \  \_.'  ) }  )
                        \.-'   (     (
                        /'-.'_. ) (  }
                        \_(    {   _/\
                         ) '--' `-;\  \
                     _.-'       /  / /
              <\/>_.'         .'  / /
          <\/></\>/.  '      /<\// /
          </\>  _ |\`- _ . -/|<// (
       <\/>    - _- `  _.-'`_/- |  \
       </\>        -  - -  -     \\\
        }`<\/>                <\/>`{
        { </\>-<\/>_<\/>_<\/>-</\> }
        }      </\> </\> </\>      {
     <\/>.                         <\/>
     </\>                          </\>
      {`<\/>                     <\/>`}
      } </\>-<\/>_<\/>_<\/>_<\/>-</\> {
      {      </\> </\> </\> </\>      }
      }                               }
      {           H A P P Y           {
   <\/>        B I R T H D A Y        <\/>
   </\>                               </\>
     `<\/>                          <\/>'
  jgs </\>-<\/>_<\/>_<\/>_<\/>_<\/>-</\>
           </\> </\> </\> </\> </\>

"""

def playAudio():
    if playAudio:
       playsound(audio)

def printWish():
	sleep (.5)

	print(Fore.RED+ "  	happy          happy       happyhappy    happyhappyhappyhap     happyhappyhappyhap     happy         happy" )
	sleep (.5)
	print(Fore.RED+ "	happy          happy      happy happy    happyhappyhappyhapp    happyhappyhappyhapp     happy       happy")
	sleep (.5)
	print(Fore.RED+ "	happy          happy     happy   happy   happy          happy   happy          happy     happy     happy")
	sleep (.5)
	print(Fore.RED+ "	happy          happy    happy     happy  happy          happy   happy          happy      happy   happy")
	sleep (.5)
	print(Fore.RED+ "	happyhappyhappyhappy    happyhappyhappy  happyhappyhappyhapp    happyhappyhappyhapp        happyhappy")
	sleep (.5)
	print(Fore.RED+ "	happyhappyhappyhappy    happyhappyhappy  happyhappyhappyhap     happyhappyhappyhap          happyhap")
	sleep (.5)
	print(Fore.RED+ "	happy          happy    happy     happy  happy                  happy                         happy")
	sleep (.5)
	print(Fore.RED+ "	happy          happy    happy     happy  happy                  happy                         happy")
	sleep (.5)
	print(Fore.RED+ "	happy          happy    happy     happy  happy                  happy                         happy")
	sleep (.5)
	print(Fore.RED+ "	happy          happy    happy     happy  happy                  happy                         happy")
	sleep (.5)
	print(Fore.RED+ "	happy          happy    happy     happy  happy                  happy                         happy")
	sleep (.5)
	print(Fore.RED+ "	bbbbbbbbbbbbbbbbbb   iii  rrrrrrrrrrrrrr    TTTT        TTTT HHHHHHHHHHHHHHHH DDDDDDDDDDDDDDD            AAAAAA   YYY        YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbbbbbbbbbbbbbbbb  iii  rrrrrrrrrrrrrrr   TTTT        TTTT HHHHHHHHHHHHHHHH DDDDDDDDDDDDDDDDD         AAAA AAA   YYY      YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbb          bbbbb      rrrr        rrrr  TTTT        TTTT       HHHH           DDDD      DDDD       AAAA  AAAA   YYY    YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbb          bbbbb iii  rrrr        rrrr  TTTT        TTTT       HHHH           DDDD       DDDD     AAAA    AAAA    YYY YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbb          bbbbb iii  rrrr        rrrr  TTTT        TTTT       HHHH           DDDD        DDDD    AAAA     AAAA    YYYYYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbbbbbbbbbbbbbbb   iii  rrrrrrrrrrrrrrr   TTTTTTTTTTTTTTTT       HHHH           DDDD         DDDD  AAAAAAAAAAAAAA     YYYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbbbbbbbbbbbbbbb   iii  rrrrrrrrrrrrrrr   TTTTTTTTTTTTTTTT       HHHH           DDDD         DDDD  AAAAAAAAAAAAAA     YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbb          bbbbb iii  rrrr        rrrr  TTTT        TTTT       HHHH           DDDD        DDDD   AAAA      AAAA     YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbb          bbbbb iii  rrrr        rrrr  TTTT        TTTT       HHHH           DDDD       DDDD    AAAA      AAAA     YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbb          bbbbb iii  rrrr        rrrr  TTTT        TTTT       HHHH           DDDD      DDDD     AAAA      AAAA     YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbbbbbbbbbbbbbbbb  iii  rrrr        rrrr  TTTT        TTTT       HHHH       DDDDDDDDDDDDDDDDD      AAAA      AAAA     YYY")
	sleep (.5)
	print(Fore.RED+ "	bbbbbbbbbbbbbbbbbb   iii  rrrr        rrrr  TTTT        TTTT       HHHH       DDDDDDDDDDDDDDDD       AAAA      AAAA     YYY")
	print (cake)

os.system('cls' if os.name == 'nt' else 'clear')
Thread(target = playAudio).start()
Thread(target = printWish).start()