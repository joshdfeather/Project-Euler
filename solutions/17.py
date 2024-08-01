dictionary = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
    '1000': 'thousand'
}

counter = 0

for i in range(1, 1001):

    j = str(i)

    if i == 1000:
        counter += 11

    elif len(j) == 3:

        counter += len(dictionary[j[0]]) + 7

        if j[-2:] != '00':

            counter += 3

            if int(j[-2:]) < 20:
                counter += len(dictionary[str(int(j[-2:]))])

            else:

                if j[1] == '0':
                    counter += 0
                else:
                    counter += len(dictionary[j[1] + '0'])

                if j[2] == '0':
                    counter += 0
                else:
                    counter += len(dictionary[j[2]])



    elif len(j) == 2:

        if int(j) < 20:
            counter += len(dictionary[str(int(j))])
            
        else:

            if j[0] == '0':
                counter += 0
            else:
                counter += len(dictionary[j[0] + '0'])

            if j[1] == '0':
                counter += 0
            else:
                counter += len(dictionary[j[1]])

    if len(j) == 1:
        counter += len(dictionary[j])

print(counter)

# Solution: 21124
