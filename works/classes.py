class Radio():
   def __init__(self, name, channel, now_playing, priceofmin):
        """ """
        self.name = name
        self.channel = channel
        self.now_playing = nowplaying
        self.priceofmin = priceofmin

   def rekl_calculator(self, days, mins):
        answer = self.priceofmin * days * mins
        return answer

ardaidardo = Radio("FortunaPlus", "103.4", "Justin Timberlake - Mirrors", 37.5)
print(ardaidardo.rekl_calculator(3,4))
print("axla usment:\" %s \"arxze %s , %s" %(ardaidardo.now_playing, ardaidardo.name, ardaidardo.channel))
