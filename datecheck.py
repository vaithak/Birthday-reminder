from collections import defaultdict
import datetime


suffix = {'1':'st', '2':'nd', '3':'rd', '21':'st', '22':'nd', '23':'rd'}
suffix = defaultdict(lambda : 'th', suffix)

month = {'1':'January',
         '2':'February',
         '3':'March',
         '4':'April',
         '5':'May',
         '6':'June',
         '7':'July',
         '8':'August',
         '9':'September',
         '10':'October',
         '11':'November',
         '12':'December'
         }

def validate(Date):
    length = len(Date)
    try:
        if length == 3:
            if Date[1] == '/':
                datetime.datetime(2008, int(Date[0]), int(Date[2]))
                Date = Date[0] + suffix[Date[0]] + " " + month[Date[2]]
            else:
                Date ='FALSE'
        elif length == 4:
            if Date[1] == '/':
                datetime.datetime(2008, int(Date[2:]), int(Date[0]))
                Date = Date[0] + suffix[Date[0]] + " " + month[Date[2:]]
            elif Date[2] == '/':
                datetime.datetime(2008, int(Date[3]), int(Date[0:2]))
                Date = str(int(Date[0:2])) + suffix[Date[0:2]] + " " + month[Date[3]]
            else:
                Date = 'FALSE'
        elif length == 5:
            if Date[2] == '/':
                datetime.datetime(2008, int(Date[3:]), int(Date[0:2]))
                Date = str(int(Date[0:2])) + suffix[Date[0:2]] + " " + month[Date[3:]]
            else:
                Date = 'FALSE'
        else:
            Date = 'FALSE'
    except:
        Date = 'FALSE'
    return Date
