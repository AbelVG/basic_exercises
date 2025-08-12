#Convert 12h format into 24h format

timeInput = input("Enter the current time in 12h format(example: 02:14 am)")

#Preprocess the input
timeNoSpaces = timeInput.replace(" ", "")
time = timeNoSpaces.lower()

def time_conversion(time):
    #Check for AM or PM and then process accordingly
    if time.find('pm') != -1:
        timeHold = time.replace('pm', '').split(':')
        timeHold[0] = str(int(timeHold[0]) + 12)
        if timeHold[0] == '24':
            timeHold[0] = '00'
        conversion = ':'.join(timeHold)
        return conversion
    elif time.find('am') != -1:
        conversion = time.replace('am', '')
        return conversion
    else:
        print('Please make sure to use a 12 hr format. Example: ')

print('Time in 24h format: ' + str(time_conversion(time)) + ' hrs')
