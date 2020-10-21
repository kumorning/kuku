#song lyrics typing pratice tool
#song:Hard to say goodbye_Johnny stimson
import random
import time
import hgtk


WORD_LIST = [
    "You make it hard to say goodbye I die a little every time",
    "I find it impossible to leave you with that look in your eyes Oh, you make it hard to say goodbye",
    "Little tiny Aphrodite I don't wanna wake you up When you smile in your sleep I wonder what you're dreaming of",
    "You got that temporary cherry blossom potion on your lips I wanna swallow up your ocean but I only got a sip",
    "And there's an Uber on the way because my flight is in an hour I still gotta pack a bag and brush my teeth and take a shower",
    "So I take a mental picture 'cause I know I'm gonna need it The hardest part of loving you is leaving",
    "I don't want to But I have to I already feel so lonely I don't want to But I have to I gotta let you go",
    "Supermodel Dalai Lama, you're the lover from above You're that lightning in a bottle I can't ever get enough",
    "It's like my hand is on the throttle but my heart is on the clutch Wishing I could be two places at once"
]

random.shuffle(WORD_LIST)
list_len = len(WORD_LIST)
current_count = 0

while current_count < list_len:
    q = WORD_LIST[current_count]
    current_count += 1

    start_time = time.time()
    user_input = input(q + '\n')
    end_time = time.time() - start_time

    src = hgtk.text.decompose(q)
    tar = hgtk.text.decompose(user_input)

    correct = 1
    for i, c in enumerate(src, start=0):
        try:
            if tar[i] == c:
                correct += 1
        except:
            pass

    src_len = len(src)
    c = correct / src_len * 100
    e = (src_len - correct) / src_len * 100

    speed = float(correct / end_time) * 60
    print("speed: {:0.2f} accuracy: {} %".format(speed, c, e))
    
