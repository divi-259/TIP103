'''
In your time travel adventures, you have been collecting data on the usage of different time portals by various travelers. The data is represented by an array usage_records, where usage_records[i] = [traveler_name, portal_number, time_used] indicates that the traveler traveler_name used the portal portal_number at the time time_used.

Return the adventure's "display table". The "display table" is a table whose row entries denote how many times each portal was used at each specific time. The first column is the portal number and the remaining columns correspond to each unique time in chronological order. The first row should be a header whose first column is "Portal", followed by the times in chronological order. Note that the traveler names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

def display_time_portal_usage(usage_records):
    pass
Example Usage:

usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))
Example Output:

[['Portal','10:00','10:15','10:30','11:00'],['3','2','0','1','0'],['5','1','0','0','1'],
 ['10','0','1','0','0']]
[['Portal','09:00','11:00'],['1','2','0'],['12','0','3']]
[['Portal','08:00','08:15','08:30'],['2','1','1','1']]
'''


def display_time_portal_usage(usage_records):
    usage_records.sort(key=lambda x : (x[1],x[2]))
    n = len(usage_records)
    ans = []
    temp = ['Portal']
    times = set()
    portals = {}
    for i in range(n):
        times.add(usage_records[2])
        portals[usage_records[1]] = portals.get(usage_records[1],0) + 1
    list1 = list(times)
    temp.append(list1)
    ans.append(temp)
    for i in range(len(portals)):
        row = []
        row.append(portals[i])

    



usage_records1 = [["David","3","10:00"],
["Corina","10","10:15"],
            ["David","3","10:30"],
                ["Carla","5","11:00"],
                ["Carla","5","10:00"],
                ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                ["Ratesh","12","11:00"],
                ["Amadeus","12","11:00"],
                ["Adam","1","09:00"],
                ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                ["Jhon","2","08:15"],
                ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))