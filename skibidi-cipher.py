def skibidi():

    table = {
        'a':'ski',
        'b':'bi',
        'c':'di',
        'd':'rizz',
        'e':'livdun',
        'f':'cap',
        'g':'fanum',
        'h':'bbygronk',
        'i':'hi',
        'j':'bomboclat',
        'k':'ohio',
        'l':'gyat',
        'm':'alpha',
        'n':'beta',
        'o':'sigma',
        'p':'gas',
        'q':'male',
        'r':'topg',
        's':'blud',
        't':'gyatt',
        'u':'edge',
        'v':'lowk',
        'w':'deadahh',
        'x':'fire',
        'y':'goober',
        'z':'bussing',
        '1':'nonchalant',
        '2':'dreadhead',
        '3':'drake',
        '4':'grimace',
        '5':'lightskin',
        '6':'thuggshaker',
        '7':'gta6',
        '8':'mewing',
        '9':'21',
        '0':'uwu',
        '.':'pog',
        '-':'glizzy',
        "'":'nah',
        '?':'sus',
        '!':'imposter',
        ',':'bands',
        ' ':'galaxyg'
    }

    inp = str(input('Enter the string you would like encrypted: ')).lower()

    ls = []

    for i in inp:
        
        ls.append(i)

    newStr = ''

    while len(ls) > 0:

        cur = table[ls[0]]

        newStr += cur

        ls.pop(0)
    print(newStr)
skibidi()