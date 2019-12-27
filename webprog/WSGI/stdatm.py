import math

class StdAtm:
    "Performs calculations for the International Standard Atmosphere"
    
    def __init__(self):
        self.names = ("sea-level", 
                       "tropopause", 
                       "stratokink1",
                       "stratokink2",
                       "stratopause",
                       "mesokink1",
                       "mesokink2",
                       "mesopause")
        self.height = (0, 11000, 20000, 32000, 47000, 51000, 71000, 84852)
        self.tempC = (15, -56.5, -56.5, -44.5, -2.5, -2.5, -58.5, -86.2)
        self.tempK = (288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.95)
        self.lapseRate = (-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002, 0)
        self.pressure = [101325, 22625.79, 5471.935, 867.255, 110.76658, 66.848296, 3.94900, 0.372657]
        self.g = 9.80665 # m s^-2
        self.gamma = 1.4
        self.R = 287 # specific gas constant for air
        self.ft2m = 0.3048 # 1 ft == 0.3048 m
        
    def findBase(self, height):
        """Takes a height in m, returns index to various self.xxx arrays"""
        baseHeights = self.height
        for i in range(len(baseHeights)):
            if (baseHeights[i] > height): return i-1
            
    def calcTemp(self, height):
        inx = self.findBase(height)
        return self.tempK[inx] + self.lapseRate[inx] * (height - self.height[inx])
    
    def calcPress(self, height):
        inx = self.findBase(height)
        if self.lapseRate[inx] == 0: # isothermal
            return self.isothermal(height, inx)
        else:
            return self.nonisothermal(height, inx)
    
    def calcDensity(self, T, P):
        "parameters: temperature (K) and pressure (Pa) for current height"
        return P / (self.R * T)
        
    def isothermal(self, height, inx):
        exponent = -self.g / (self.tempK[inx] * self.R) * (height - self.height[inx])
        return self.pressure[inx] * math.exp(exponent)
            
    def nonisothermal(self, height, inx):
        temp = self.calcTemp(height)
        exponent = -self.g / (self.lapseRate[inx] * self.R) 
        return self.pressure[inx] * (temp / self.tempK[inx])**exponent
    
    def calcMach1(self, temp):
        # speed of sound, m/s
        return math.sqrt(self.gamma * self.R * temp)
    
    def getResults(self, data):
        """Requires: dictionary with either data["h_m"] or data["h_ft"] containing numeric height.
           Fills out the dictionary with results for this height.
        """
        
        if "h_m" in data:
            data["h_ft"] = data["h_m"] / self.ft2m
        elif "h_ft" in data:
            data["h_m"] = data["h_ft"] * self.ft2m
        else:
            raise KeyError('Height must be in data["h_m"] or data["h_ft"]')
        
        inx = self.findBase(data["h_m"])
        data["temp_K"] = self.calcTemp(data["h_m"])
        data["temp_C"] = data["temp_K"] - 273.15
        data["pressure"] = self.calcPress(data["h_m"])
        data["rho"] = self.calcDensity(data["temp_K"], data["pressure"])
        data["isothermal"] = True if self.lapseRate[inx] == 0 else False
        data["mach1_si"] = self.calcMach1(data["temp_K"])
        data["mach1_kt"] = data["mach1_si"] / 0.51444

if __name__ == "__main__":
    print("Debugging:")
    atm = StdAtm()
    print(atm.calcTemp(38969))
    print(atm.calcPress(38969))
    print(atm.calcTemp(15000))
    print(atm.calcPress(15000))
    
    data = {}
    data['h_ft'] = 15000
    atm.getResults(data)
    print(data)