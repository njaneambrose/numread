class NumberReader:
    def __init__(self,val):
        self.num = val
        self.ones = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',\
                     8:'eight',9:'nine'}
        self.onea = {10:'ten',11: 'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',\
                     16:'sixteen',17:'seventeen',18:'eigthteen',19:'nineteen'}
        self.tens = {20: 'twenty',30: 'thirty',40:'fourty',50: 'fifty',60:'sixty',70:'seventy'\
                     ,80:'eighty',90:'ninety'}
    def read(self):
        if self.num > 9 and self.num < 20:
            ans = self.onea.get(self.num)
        else:
            d = self.vals(self.num)
            e = len(d)
            if e == 1: ans = self.get_ones(d)
            elif e == 2: ans = self.get_tens(d)
            elif e == 3: ans = self.get_hundrends(d)
            elif e == 4: ans = self.get_thousands(d)
            elif e == 5: ans = self.get_tthousands(d)
            elif e == 6: ans = self.get_hthousands(d)
            elif e == 7: ans = self.get_millions(d)
            elif e == 8: ans = self.get_tmillions(d)
            elif e == 9: ans = self.get_hmillions(d)
            elif e == 10: ans = self.get_billions(d)
            elif e == 11: ans = self.get_tbillions(d)
            elif e == 12: ans = self.get_hbillions(d)
        return ans
    def get_ones(self,val):
        return (self.ones.get(val[0]))
    def get_tens(self,val):
        x = ""
        x = x+"{0}".format(self.tens.get(val[1]))
        if val[0] != 0:
            x = x+" {0}".format(self.ones.get(val[0]))
        return x    
    def get_hundrends(self,val):
        x = ""
        x = x+" {0} hundrend ".format(self.ones.get(val[2]/100))
        s  = val[0]+val[1]
        if s > 9 and s < 20:
                x +="and "
                x = x+self.onea.get(s)
        else:    
            if val[1] != 0:
                x = x+"and {0}".format(self.get_tens([val[0],val[1]]))
            else:
                if val[0] != 0: x = x+" and {0}".format(self.ones.get(val[0]))
        return x        
    def get_thousands(self,val):
        x = ""
        x = x+"{0} thousand".format(self.ones.get(val[3]/1000))
        x = x+self.finalize(val)  
        return x
    def finalize(self,val):
        x = ""
        if val[2] != 0:
            x = x+self.get_hundrends([val[0],val[1],val[2]])
        elif val[2] == 0 and val[1] != 0:
            x = x+" and "
            s = val[1]+val[0]
            if s > 9 and s < 20: 
                x = x+self.onea.get(s)
            else:    
                x = x+self.get_tens([val[0],val[1]])
        elif val[2] == 0 and val[1] == 0 and val[0] != 0 :
            x = x+" and "
            x = x+self.get_ones([val[0],val[1]])    
        return x
    def get_tthousands(self,val):
        x = ""
        w = (val[3]+val[4])/1000
        if w > 9 and w < 20:
            x = x+"{0} thousand".format(self.onea.get(int(w)))
        else:
            x = x+"{0} thousand".format(self.get_tens(self.vals(int(w))))
        x = x+self.finalize(val)
        return x
    def get_hthousands(self,val):
        x = ""
        w = (val[3]+val[4]+val[5])/1000
        x = x+"{0} thousand".format(self.get_hundrends(self.vals(int(w))))
        x = x+self.finalize(val)
        return x
    def get_millions(self,val):
        x = ""
        mil = (val[6])/1000000
        del val[6]
        x = x+"{0} million".format(self.get_ones([int(mil)]))
        try:
            x = x+self.get_hthousands(val)
        except  IndexError:
            pass
        return x
    def get_tmillions(self,val):
        x = ""
        mil = (val[7]+val[6])/1000000
        del val[7]
        del val[6]
        if mil > 9 and mil < 20:
            print(mil)
            x = x+"{0} million".format(self.onea.get(int(mil)))
        else:    
             x = x+"{0} million".format(self.get_tens(self.vals(int(mil))))
        try:
            x = x+self.get_hthousands(val)
        except  IndexError:
            pass
        return x
    def get_hmillions(self,val):
        x = ""
        mil = (val[7]+val[6]+val[8])/1000000
        del val[8]
        del val[7]
        del val[6]  
        x = x+"{0} million".format(self.get_hundrends(self.vals(int(mil))))
        try:
            x = x+self.get_hthousands(val)
        except  IndexError:
            pass
        return x
    def get_billions(self,val):
        x = ""
        bil = (val[9])/1000000000
        x = x+"{0} billion".format(self.get_ones([int(bil)]))
        del val[9]
        try:
            x = x+self.get_hmillions(val)
        except IndexError:
            pass
        return x
    def get_tbillions(self,val):
        x = ""
        bil = (val[9]+val[10])/1000000000
        if bil > 9 and bil < 20:
            x = x+"{0} billion".format(self.onea.get(int(bil)))
        else:    
            x = x+"{0} billion".format(self.get_tens(self.vals(int(bil))))
        del val[10];del val[9]
        try:
            x = x+self.get_hmillions(val)
        except IndexError:
            pass
        return x
    def get_hbillions(self,val):
        x = ""
        bil = (val[9]+val[10]+val[11])/1000000000
        if bil > 9 and bil < 20:
            x = x+"{0} billion".format(self.onea.get(int(bil)))
        else:    
            x = x+"{0} billion".format(self.get_hundrends(self.vals(int(bil))))
        del val[11];del val[10];del val[9]
        try:
            x = x+self.get_hmillions(val)
        except IndexError:
            pass
        return x
    def vals(self,val):
        p = []
        s = str(val)
        x = len(s)
        mul = 1
        while x > 0:
            x -=1
            p.append(int(s[x])*mul)
            mul *=10    
        return p
    def readdigits(self):
        x = ""
        a = str(self.num)
        for s in range(0,len(a)):
            x = x+read(int(a[s]))+" "
        return x    
def read(val):
    c = NumberReader(val)
    return c.read().strip()
def read_per_digit(val):
    c = NumberReader(val)
    return c.readdigits().strip()
