class radio():
   def __init__(self, name, channel, nowplaying, priceofmin):
        """ """
        self.name = name
        self.channel = channel
        self.nowplaying = nowplaying
        self.priceofmin = priceofmin

   def rekl_calculator(self, days, mins):
        answer = self.priceofmin * days * mins
        return answer

ardaidardo = radio("FortunaPlus", "103.4", "Justin Timberlake - Mirrors", 37.5)
print(ardaidardo.rekl_calculator(3,4))
print("axla usment:\" %s \"arxze %s , %s" %(ardaidardo.nowplaying, ardaidardo.name, ardaidardo.channel))
