# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER


def come():
    agent.teleport_to_player()

player.on_chat("tp", come)

def turn_left():
    agent.turn(LEFT)

def turn_right():
    agent.turn(RIGHT)

player.on_chat("tl", turn_left)
player.on_chat("tr", turn_right)


def forward(steps):
    agent.move(FORWARD, steps)
player.on_chat("fw",forward)


def up(steps):
    agent.move(UP, steps)
player.on_chat("up", up)


def down(steps):
    agent.move(DOWN, steps)
player.on_chat("dn", down)


def back(steps):
    agent.move(BACK, steps)
player.on_chat("bk", back)



def climb():
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
player.on_chat("cl", climb)



def descend ():
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("de", descend)


def choptree(tall):
    for count in range(tall):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, tall)
    agent.collect_all()

player.on_chat("chop", choptree)




def Dig(length):
    for count in range(length):
    
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("dig", Dig)


def build(length):
    for count in range(length):
        agent.place(FORWARD)
        agent.move(RIGHT, 1)

player.on_chat("bu", build)



def pillar(length):
    for count in range(4):
        agent.place(FORWARD)
        agent.move(UP, 1)

player.on_chat("pi", pillar)


