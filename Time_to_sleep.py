class Alarm(object):
    '''function docstring'''
    def __init__(self,*set_alarm) -> None:
        self._s = [*set_alarm]
    def Time_to_sleep(self)->list:
        '''function docstring'''
        def check(val):
            if val[0] == '0' :
                return int(val[1])
            else :
                return int(val)
        clock = ['0'+str(i) for i in range(0,10)]
        second_half = [str(i) for i in range(10,24)]
        clock.extend(second_half)
        results = list()
        for time in self._s :
            if time[0] == time[1] :
                results.append('00:00')
                continue
            hour , minute = time[0].split(':')[0] , time[0].split(':')[1]
            dhour , dminute = time[1].split(':')[0] , time[1].split(':')[1]
            idx = check(hour) - check(dhour)
            if dminute == '00' :
                results.append(clock[idx] + ':' + minute)
            else :
                idx -= 1
                add = (60 - check(dminute)) + check(minute)
                results.append(clock[idx] + ':' +str(add))
        return results
        
sample = Alarm(["07:50", "07:50"])
print(sample.Time_to_sleep())
sample = Alarm(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
print(sample.Time_to_sleep())
sample = Alarm(["05:45", "04:00"], ["07:10", "04:30"])
print(sample.Time_to_sleep())
exit = input('Enter any key to exit :')