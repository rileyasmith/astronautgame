# Riley SMITH - Astronaut Adventure
# Last updated on: 21 March 2024
# To run this game, use the CS in Schools Code Editor: https://csinschools.io/code-editor

# Currently, you cannot play using IDLE.

from csinsc import *

label .game_start

print(Colour.red + "Houston, we have a problem...")
print(Colour.white + "\nYou are an astronaut lost in space. \nYou slipped off the space station during maintenance.")
print("\nYour goal is to get back to the space station." + Colour.reset)

print(Colour.grey + r'''
        _..._
      .'     '.      _
     /    .-""-\   _/ \
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
  jgs    \   `\  \
          `-._/._/
''')
input(Colour.green + "Press [ENTER] to play!" + Colour.reset)

label .spacestation
print(Colour.cyan + "\nYou slowly drift away from the ISS. With a spanner in hand, you remember a video you watched. \nThe video said if you throw something away from you, the momentum can move you in the opposite direction. \nYou are skeptical but realise it's worth a try." + Colour.reset)
answer = input(Colour.green + "\nDo you risk it? [y/n]: ")

# If the player responds with "y" or "Y" (case-insensitive).
if answer == "y" or "Y" :
    print("\nYou throw your spanner with enough momentum to send you closer to the ISS! Good job astronaut!")
    goto .friend

# If the player responds with "n" or "N"  (case-insensitive).
if answer == "n" or "N" :
    print("\nYou drift further away and try screaming for help. You remember the quote from the movie Alien. 'In space, no one can hear you scream.'")
    goto .spacestation

# If the input the player gives does NOT confine to the y/n or Y/N input keys. (due to our now applied case insensitivity)
if answer2 != "y" or "Y" or "n" or "N" :
        print(Colour.red + Style.bold +  "\nInvalid option. Please use [y/n] input keys.")
        goto .spacestation

print(Colour.grey + r```
                 .       .                   .       .      .     .      .
          .    .         .    .            .     ______
      .           .             .               ////////
                .    .   ________   .  .      /////////     .    .
           .            |.____.  /\        ./////////    .
    .                 .//      \/  |\     /////////
       .       .    .//          \ |  \ /////////       .     .   .
                    ||.    .    .| |  ///////// .     .
     .    .         ||           | |//`,/////                .
             .       \\        ./ //  /  \/   .
  .                    \\.___./ //\` '   ,_\     .     .
          .           .     \ //////\ , /   \                 .    .
                       .    ///////// \|  '  |    .
      .        .          ///////// .   \ _ /          .
                        /////////                              .
                 .   ./////////     .     .
         .           --------   .                  ..             .
  .               .        .         .                       .
                        ________________________
____________------------                        -------------_________
```

label .friend
print(Colour.cyan + "\nYou see your friend Mike on the Space Station. You try flailing your arms and legs to grab his attention. \nThen you try your radio and he hears you. \nHe hears you and tries to grab your arm. You want to try it but you're scared.")
answer2 = input("\nTry grab his hand? [y/n]: ")
if answer2 == "y" or "Y" : 
    print("\nIt's a success! You successfully grab onto Mike's hand and get back on the ISS. Nice job!")

if answer2 == "n" or "N" :
    print("\nHe wonders why you won't grab his hand. He thinks you're kidding and you tell him your skeptical. \nHe calls you crazy and ultimately tries to talk you into him helping you.")
    label .retryfriend
    
if answer2 != "y" or "Y" or "n" or "N" :
    print(Colour.red + Style.bold + "\nInvalid option. Please use [y/n] input keys.")
    goto .friend
    
retry = input("\nTry again? [y/n]: ")
if retry == "y" or "Y" :
    print("\nYou think about it and finally grab his hand. With all of his strength he pulls you back on.")
            
if retry == "n" or "N" :
    print("\nHe wonders again why you won't grab his hand. 'Why don't you just try?' he says. \nHe starts to get frustrated.")
    goto .retryfriend
        
if answer2 != "y" or "Y" or "n" or "N" :
    print(Colour.red + Style.bold + "\nInvalid option. Please use [y/n] input keys.")
    goto .retryfriend
