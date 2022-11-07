import randomevent

possible_event_list = ["We are watching", "Hello anybody there", "Whoemst dares to disturb the ancient ones"]
rand_event = randomevent(possible_event_list) 

@rand_event.event()
def on_event(event):
    print(event)

rand_event.start()