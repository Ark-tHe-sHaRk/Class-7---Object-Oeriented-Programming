#Create Class
class vehical:
    #Create init method
    def __init__(self, max_speed, mileage):
        pass
    #Bind The arguements
        self.max_speed = max_speed
        self.mileage = mileage
#Obeject Creation 
ModelStormbreaker = vehical(356, 15000)
#access the variables inside init method
print('Max Speed of ModelStormbreaker: ', ModelStormbreaker.max_speed)
print('The Mileage of ModelStormbreaker: ', ModelStormbreaker.mileage)