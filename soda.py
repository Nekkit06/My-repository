class Soda:
    def __init__(self, damn_it):
        if isinstance(damn_it, str):
            self.damn_it = damn_it
        else:
            self.damn_it = None

    def what_is_that(self):
        if self.damn_it:
            print(f'Soda and {self.damn_it}')
        else:
            print("Just soda")