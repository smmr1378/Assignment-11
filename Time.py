class Time:
    def __init__(self, hh ,mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()
    
    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        return result

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        return result
    
    def fix(self):

         if self.second >= 60:
            self.second -= 60
            self.minute += 1

         if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

         if self.second < 0:
             self.second += 60
             self.minute -= 1

         if self.minute < 0:
             self.minute += 60
             self.hour -= 1

    def to_second(self):
        x = self.hours * 3600 + self.minute * 60 + self.seconds
        return x

