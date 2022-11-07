from random import uniform

def eye():
    print("👁")

events = [
    (eye, 0.1, 0.2, 0.3),
    ('Loss', 0.5),
    ('Draw', 0.8)
]

def get_random_event(events):
    random_number = uniform(0., 1.)
    lower_bound = 0
    for event, prob in events:
        if lower_bound <= random_number <= lower_bound + prob:
            return event
        else:
            lower_bound += prob


get_random_event(events)