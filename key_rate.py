# Picker's log : calculates the time required to pick an order 
import time, datetime
import console
 
# Set default values for the variables used in the script
day_performance = [] 
shops_total = []
bar = '-' * 40
running = True
 
ambient = 157.0
chill = 185.0
freezer = 185.0
 
#Print the title
console.clear()
console.set_font('Futura',18)
title = 'Picker\'s logger'
print title
print bar
 
def rate(chamber,cases):
    print "It takes",round((cases/chamber) * 60),"minutes to pick this order" 
    return (cases/chamber) * 60
 
def f_time (chamber, cases):
    now = time.strftime("%H:%M", time.localtime())
    data = raw_input("Enter a start time:\n>>>")
    fmt = '%H:%M'
    if data in ['now','n']:    
        data = time.localtime()[3:5]
        data = str(data[0])+':'+str(data[1])
        print "It's",now,"now."
    print bar
    dt = datetime.datetime(*time.strptime(data,fmt)[:6])+datetime.timedelta(minutes=rate(chamber,cases))
    finish_time = dt.strftime ('%H:%M')
    print "Finish this order by",finish_time
    print bar
 
def choice():
    chamber = raw_input("What chamber?\n >>>")
 
    if chamber in ['c','chill']:
        chamber = chill
    elif chamber in ['a','ambient', 'd', 'dry']:
        chamber = ambient
    elif chamber in ['f','frozen','freezer']:
        chamber = freezer
    else:
        print "Chamber does NOT exist, you're probably lost"
        choice()
    
    cases = int(raw_input("How many cases? \n >>>"))
 
    f_time(chamber,cases)
    
    record = raw_input("Would you like to add these cases to your daily performance record?\n >>>")
 
    if record in ['yes', 'y', 'Y']:
        day_performance.append(cases)
        print cases, "cases have been added to your daily performance record.\nYour daily total is now",sum(day_performance),"cases."
    else:
        print("This order hasn't been recorded.")
    shops = int(raw_input ("How many shops are going on this journey? \n>>>"))
    shops_total.append(shops)
    print shops, "shops have been added to your daily performance record. You've picked", sum(shops_total),"shops so far."
 
while running == True:
 
    quest = raw_input("Ready to do some work?\n>>>")
 
    if quest in ['yes', 'y']:
        choice()
    elif quest == 'total':
        print "Your daily total is", sum(day_performance),"cases on", sum(shops_total),"shops."
        choice()
    elif quest in ['quit','q','no','n']:
        break   
    
print "You've picked %d cases: %d shops on %d journeys\n Bye, bye! " % (sum(day_performance),sum(shops_total),len(day_performance))
