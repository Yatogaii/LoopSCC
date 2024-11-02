from compare import compare
from wsummarizer import WSummarizer as ws


def input_loop(x, z):
    path = ""

    while x < 100:
        if z > x:
            x = x + 1
            path += "A"
        else:
            z = z + 1
            path += "B"
    return [x, z, path]


x, z = ws.create_variables(2)

loop = ws.define_loop(x < 100, [
    ([z > x], [
        [1, 0, 1],  # x = x + 1
        [0, 1, 0],  # z = z
    ]),
    ([z <= x], [
        [1, 0, 0],  # x = x
        [0, 1, 1],  # z = z + 1
    ]),
])

all_initial_values = [
    [95827032, 910493864, ],
    [-2114695566, 1739837639, ],
    [397125133, 1112887137, ],
    [1085711942, -1346962089, ],
    [1344572457, 1915127082, ],
    [585878108, 939848563, ],
    [618858243, -1296433075, ],
    [-414044090, 726763819, ],
    [706858415, -485590847, ],
    [1122154397, -1995942286, ],
    [-753082572, -1254869069, ],
    [89581696, 2047363596, ],
    [-1190685373, -1644545008, ],
    [304908852, -1751901568, ],
    [-771112283, 1853669113, ],
    [985575261, -1325718803, ],
    [463636047, -1023805185, ],
    [-536482110, -1212508807, ],
    [311912839, -993073444, ],
    [693067114, -978127633, ],
    [1799511031, 850775724, ],
    [1488631158, -1514594647, ],
    [-537760681, 1051852708, ],
    [-928268960, -68384531, ],
    [-8115255, -1987454984, ],
    [1085270885, 473773522, ],
    [-458316349, -868178153, ],
    [-832191026, -175032048, ],
    [-53462623, 1128309653, ],
    [453574568, 2022731280, ],
    [-1798495044, -1746362629, ],
    [350755261, -746826329, ],
    [1614731166, -1637797099, ],
    [158069633, 552220882, ],
    [-1281555888, 729866381, ],
    [407802174, 747043089, ],
    [-1720394935, 1714078878, ],
    [-1219750779, -550247212, ],
    [220768125, -444222588, ],
    [1548926053, -2030619561, ],
    [-1317610795, 839885362, ],
    [-382663810, -499106647, ],
    [-1627839428, 1439363901, ],
    [-1777368923, 1011149091, ],
    [374974830, 1049506655, ],
    [-1749143475, -1686357389, ],
    [1998870305, 1496316129, ],
    [-1971209351, -933218434, ],
    [808169588, -1820673636, ],
    [1853142017, -1715945675, ],
    [-1837310675, 870301549, ],
    [-1544524461, -1960874566, ],
    [-856007720, -2020660960, ],
    [-72210068, 1162413220, ],
    [-1722844879, 606361988, ],
    [-1242537882, 1848603394, ],
    [329546403, 1957062736, ],
    [-769511818, -1617259063, ],
    [-926171050, 1267543002, ],
    [1290138745, 1289425350, ],
    [854437188, -712582896, ],
    [-768578449, -2018660282, ],
    [1677670576, -202236084, ],
    [2101193163, -1563640433, ],
    [-507235779, 632102624, ],
    [1183208243, -767153646, ],
    [-1932621387, -1738538479, ],
    [-209197604, 1318683841, ],
    [-1386857687, 1584605028, ],
    [1836306749, 1340690355, ],
    [286095815, 738335639, ],
    [727468434, 296878569, ],
    [1374867850, -784522161, ],
    [-1774762903, 1504069590, ],
    [1642940029, 605294268, ],
    [-1856126051, -981475023, ],
    [-500089451, -1080812139, ],
    [1249740963, -226066015, ],
    [-1532289130, -374022544, ],
    [1270821243, 688611135, ],
    [1574320365, 533855263, ],
    [1020811671, 1801053568, ],
    [-716985362, -1541300718, ],
    [-1565586072, 1889200926, ],
    [1689217338, 1979682528, ],
    [-1823347327, 1414284671, ],
    [-1572808793, -2014015548, ],
    [-1132742308, -478554528, ],
    [328365535, 1523700057, ],
    [1006571447, -142173973, ],
    [-250089649, -1807146203, ],
    [-2136386075, -1532833180, ],
    [-2139357418, 206713568, ],
    [1426587651, 1922530950, ],
    [1375687013, -1087050660, ],
    [1334623146, 660812638, ],
    [2000872763, 28488211, ],
    [1530467979, -1808213063, ],
    [-548817865, -911074371, ],
    [-1279381101, -1732321736, ],
]

loop.summarize()

print("RESULT BELOW:")
for initial_values in all_initial_values:
    terminal_values = loop.compute_terminal_values(*initial_values)
    output_str = ''
    for each in terminal_values:
        output_str += f'{each} '
    print(output_str)