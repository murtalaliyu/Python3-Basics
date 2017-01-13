import csv  #comma separated variables

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    dates = []
    colors = []

    for row in readCSV:     #will read everything as string so need to convert numbers to int or float
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print('dates:', dates)
    print('colors:', colors)

    whatColor = input('What color do you wish to know the date of?')

    try:
        coldex = colors.index(whatColor)
        theDate = dates[coldex]
        print('The date of', whatColor, 'is', theDate)
    except:
        print(whatColor, 'is not in this list')

