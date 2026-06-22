import time

lyrics = [
    ("We get married", 0.15),
    ("In our heads", 0.13),
    ("Something to do", 0.11),
    ("While we try to recall", 0.12),
    ("How we met", 0.10),

    ("Do you think I have forgotten?", 0.15),
    ("Do you think I have forgotten?", 0.13),
    
    ("ISHA ISHA ISHA", 0.15),
]

for text, delay in lyrics:
    words = text.split()

    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(delay)

    print()
    time.sleep(1)