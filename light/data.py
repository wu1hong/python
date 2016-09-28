# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:05:44 2016

@author: yihong
"""

class NewtonRing(object):
    
    
    def __init__(self):
        self.primer_data = []
        
        
    def adder(self):
        """print "请依次输入第15环至第6环左侧数据，然后输入第6环至第15环右侧数据,输入end终止输入."
        while True:
            get = raw_input()
            if get == "end":
                break
            else:
                try:
                    get = float(get)
                except ValueError:
                    print "请输入数字"
                self.primer_data.append(get)
        #print self.primer_data"""
          
        
        #------text code---------
        file_str = open("data.txt", "r").read()
        #print file_str
        self.primer_data = map(float, file_str.split())
        #print self.primer_data
        #------text code---------
        
        
        data_list_len = len(self.primer_data)    
        #print self.list_len
        if data_list_len % 2 != 0:
            raise IOError("Please")     
        self.diameter = [abs(self.primer_data[i] - self.primer_data[data_list_len - i -1]) \
        for i in xrange(data_list_len / 2)]
        #print self.diameter
        self.d_list_len = len(self.diameter)
        #print self.d_list_len
        
        
    def result(self):
        if self.primer_data == []:
            print "请首先调用.adder()输入数据"
            raise IOError
        print self.d_list_len
        self.R = [(self.diameter[i] ** 2 - self.diameter[i + self.d_list_len / 2] ** 2) \
        / (4 * self.d_list_len / 2 * 589.3) * 1e6 for i in xrange(self.d_list_len / 2)]
        self.average_R = sum(self.R) / len(self.R)
        #print self.average_R
       
  
    def all_info(self):
        #column = 39
        print "\n"
        print "单位：mm"
        print "+" + "-" * 37  + "+"
        print "| No.|   left   |   right  | diameter |"
        for i in xrange(self.d_list_len):
            print   "-" * 39
            print "|{0:^4}|{1:^10}|{2:^10}|{3:^10}|".format(
              i + self.d_list_len / 2 + 1
            , self.primer_data[self.d_list_len - 1 - i]
            , self.primer_data[self.d_list_len + i]
            , self.diameter[self.d_list_len - 1 -i])
        print "+" + "-" * 37 + "+"
        print "\n"
        print "单位：mm"
        print "+" + "-" * 65 + "+"
        print "|  R  |",
        for i in xrange(len(self.R)):
            print "{:^9.3f}".format(self.R[i]), "|",
        print " "
        print "+" + "-" * 65 + "+"
        print "\n"
        print "The average of R is ", round(self.average_R, 3)
        
        
        
        
class Pijian(object):
    
    
    def __init__(self):
        self.l_data = []
        self.length_data = []
        
        
        #-----------test code---------
        test1 = open("l_data.txt", "r").read().split()
        test1 = map(float, test1[:])
        #print test1
        self.l_data = [[test1[i], test1[i + 1]] for i in xrange(0, len(test1) - 1, 2)]
        #print self.l_data        
        test2 = open("length_data.txt", "r").read().split()
        test2 = map(float, test2[:])
        self.length_data = [[test2[i], test2[i + 1]] for i in xrange(0, len(test2) - 1, 2)]
        #print self.length_data
        #-----------test code---------
        
        
    """def l_adder(self):
        get_ = []
        print "请在这里输入干涉条纹间距的数据\n请依次输入每组实验数据前后读数,输入end终止输入."
        while True:
            get = raw_input()
            if get == "end":
                break
            else:
                try:
                    get = float(get)
                except ValueError:
                    print "请输入数字"
                get_.append(get)
                if len(get_) == 2:
                    self.l_data.append(get_)
                    get_ = [] 
        #print self.d
        
    def length_adder(self):
        get_ = []
        print "请在这里输入劈尖长度的数据\n请依次输入每组实验数据前后读数,输入end终止输入."
        while True:
            get = raw_input()
            if get == "end":
                break
            else:
                try:
                    get = float(get)
                except ValueError:
                    print "请输入数字"
                get_.append(get)
                if len(get_) == 2:
                    self.length_data.append(get_)
                    get_ = []   """                
    def d(self):
        
        def avr(a = []):
            return sum(a) / len (a)
            
        l_comtainer = [10 / abs(self.l_data[i][0] - self.l_data[i][1])\
        for i in xrange(len(self.l_data))]
        #print l_comtainer
        length_comtainer = [abs(self.length_data[i][0] - self.length_data[i][1])\
        for i in xrange(len(self.length_data))]
        l_avr = avr(l_comtainer)
        length_avr = avr(length_comtainer)
        return 589.3 * 1e-6 / 2 * l_avr * length_avr
        
        
        
a = Pijian()
#a.l_adder()
#a.length_adder()  
print a.d()   
    
        
"""s = NewtonRing()
s.adder()
s.result()
s.all_info()"""   
            
        
        