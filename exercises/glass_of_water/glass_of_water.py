class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, added):
        if added+self.amount<=self.capacity:
            self.amount+=added
        else:
            self.amount=self.capacity

    def pour_out(self, taken):
        if self.amount-taken>=0:
            self.amount-=taken
        else:
            self.amount=0
