# The script of the game goes in this file.

init:
    $ flash = Fade(.25, 0, .75, color="#fff")
    $ glowing = Fade(.25, 0, .50, color="#FFFF00")
    $ yellowatk = Fade(.05, 0, .05, color="#FFFF00")
    $ dark = Fade(.50, 0, .50, color="#A020F0")
    $ darkness = Fade(.10, 0, .10, color="#A020F0")
    $ healglow = Fade(.25, 0, .50, color="#00FF00")
    $ blueglow = Fade(.25, 0, .50, color="#87CEEB")
    $ blueatk = Fade(.10, 0, .10, color="#87CEEB")
    $ redglow = Fade(.25, 0, .50, color="#FF0000")

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define s = Character('Sistermon Blanc', color="#CD0000")
define d = Character('Dobermon', color="#B5B5B5")
define flagbattle = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    s "You've created a new Ren'Py game."
    call battles_dober
    if flagbattle == 0:
        jump ending
    else: 
        pass

return
