class Award(object):
    def __init__(self, name=None, expires_in=None, quality=None):
        self.name = name
        self.expires_in = expires_in
        self.quality = quality


    def update_award(self):
        if self.name != 'Blue Distinction Plus':
            self.expires_in -= 1

        if self.name == 'Blue First':
            if self.expires_in > 0:
                self.quality = min(50, self.quality + 1)
            else:
                self.quality = min(50, self.quality + 2)

        elif self.name == 'Blue Distinction Plus':
            pass #Not changing anything for blue distinction

        elif self.name == 'Blue Compare':
            if self.expires_in < 0:
                self.quality = 0
            elif self.expires_in < 5:
                self.quality = min(50, self.quality + 3)
            elif self.expires_in < 10:
                self.quality = min(50, self.quality + 2)
            else:
                self.quality = min(50, self.quality + 1)

        elif self.name == 'Blue Star':
            if self.expires_in > 0:
                self.quality = max(0, self.quality - 2)
            else:
                self.quality = max(0, self.quality - 4)

        else: #Normal Reward 
            if self.expires_in > 0:
                self.quality = max(0, self.quality - 1)
            else:
                self.quality = max(0, self.quality - 2)