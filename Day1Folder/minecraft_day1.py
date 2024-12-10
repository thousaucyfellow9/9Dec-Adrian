# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def come():
    agent.teleport_to_player()

player.on_chat("tp", come)

def turn_left():
    agent.turn(LEFT)

def turn_right():
    agent.turn(RIGHT)

player.on_chat("tl", turn_left)
player.on_chat("tr", turn_right)


def forward():
    agent.move(FORWARD,4)
player.on_chat("fw",forward)


def up():
    agent.move(UP, 1)
player.on_chat("up", up)


def down():
    agent.move(DOWN, 1)
player.on_chat("dn", down)



def climb():
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
player.on_chat("cl", climb)



def descend ():
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("de", descend)
