class States():
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

    def cleanup(self):
        pass

    def startup(self):
        pass
    
    def handle_events(self, events):
        pass

    def handle_collisions(self):
        pass

    def handle_keys(self, keys):
        pass

    def update(self, screen):
        pass
