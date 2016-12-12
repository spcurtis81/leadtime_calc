# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta


now = datetime.now()
wdlt = 50
cdlt = (wdlt / 5) * 7
    
due = now + timedelta(days=cdlt)
    
weekday = (due.weekday())
    
if weekday == 0:
    due = due + timedelta(days=4)
elif weekday == 1:
    due = due + timedelta(days=3)
elif weekday == 2:
    due = due + timedelta(days=2)
elif weekday == 3:
    due = due + timedelta(days=1)
elif weekday == 4:
    due = due + timedelta(days=0)
elif weekday == 5:
    due = due + timedelta(days=-1)
elif weekday == 6:
    due = due + timedelta(days=-2)
else:
    TypeError("Possible Error: Unrecognised Week Day")

expected = str("{}/{}/{}".format(due.day, due.month, due.year))
#print("End of week due date...")
#print(expected)
#print()
#print("Nice text...")
#print(due.strftime("%a %d %b %Y"))
