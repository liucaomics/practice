class Solution:
    out = []
    def state2time(self,state):
        hour = 0
        minutes = 0
        for i in range(4):
            hour += state[i]*2**i
        if hour > 11:
            return
        for i in range(6):
            minutes += state[4+i]*2**i
        if minutes >= 60:
            return
        if minutes <= 9:
            return str(hour)+':0'+ str(minutes)
        else:
            return str(hour)+':'+str(minutes)

    def readBinaryWatch(self, num):
        self.out = []
        self.readBinaryWatch_util(num, [])
        return self.out

    def readBinaryWatch_util(self, num, state):
        if num == 0:
            ti = self.state2time(state+[0]*(10-len(state)))
            if ti:
                self.out.append(ti)
            return
        if 10 - len(state) < num:
            return
        if 10 - len(state) == num:
            ti = self.state2time(state+[1]*num)
            if ti:
                self.out.append(ti)
                return
        self.readBinaryWatch_util(num,state+[0])
        self.readBinaryWatch_util(num-1,state+[1])
        
        