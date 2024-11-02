from compare import compare
from wsummarizer import WSummarizer as ws


def input_loop1(x, y):
    path = ""

    while x > y:
        x = x - 1
        x = x + 1000
        y = y + 1000
        path += "A"

    return [x, y, path]


def input_loop2(x, y):
    path = ""

    while y > 0:
        y = y - 1
        path += "A"

    return [x, y, path]


def input_loop3(x, y):
    path = ""

    while x < 0:
        x = x + 1
        path += "A"

    return [x, y, path]


x, y = ws.create_variables(2)

loop1 = ws.define_loop([x > y], [
    (x == x, [
        [1, 0, 1001],  # x = x + 1001
        [0, 1, 1000],  # y = y + 1000
    ]),
])

loop2 = ws.define_loop(y > 0, [
    (x == x, [
        [1, 0, 0],  # x = x
        [0, 1, -1],  # y = y - 1
    ]),
])

loop3 = ws.define_loop(x < 0, [
    (x == x, [
        [1, 0, 1],  # x = x + 1
        [0, 1, 0],  # y = y
    ]),
])

all_initial_values = [
    [-1719660815, 1789276501, ],
    [-246084630, 976291584, ],
    [1669312514, -1350698351, ],
    [-1039637214, 1279152416, ],
    [-1999842547, -663640572, ],
    [-1365796093, -266438721, ],
    [-1899709769, -132676210, ],
    [851185600, 1640032875, ],
    [311334607, -1660873299, ],
    [89117536, -1352134545, ],
    [-557052742, 887783640, ],
    [1055259704, -1591624388, ],
    [1826475510, 1167992578, ],
    [-1597509929, 1261780968, ],
    [-972909429, -1842082196, ],
    [-1462410164, 1437078727, ],
    [1211491860, -2103863845, ],
    [-1410148734, 834389926, ],
    [-566818549, 1946992102, ],
    [-960092951, 1671851133, ],
    [-651323502, -503392419, ],
    [-584454398, -1652710600, ],
    [-118579722, 71795790, ],
    [-103201829, -626208102, ],
    [-1007489817, -1776407726, ],
    [1272902189, -1530288670, ],
    [-1341857858, 761494905, ],
    [1891924284, -2017419413, ],
    [-197899178, 1430898316, ],
    [-1283803034, -539850342, ],
    [-1369736970, 2101162309, ],
    [428936481, 1575422550, ],
    [-1909047053, 2120297174, ],
    [1299248378, -1516430581, ],
    [-291280653, -551910122, ],
    [-927851598, 1340409555, ],
    [141604391, -737245980, ],
    [220935193, 507784410, ],
    [-1746408375, -293492715, ],
    [1460271867, -352960721, ],
    [1545859417, -69084947, ],
    [1117068772, 552067004, ],
    [-871979907, 551045768, ],
    [635886653, -1484456771, ],
    [-1801787682, 614467901, ],
    [810441029, -1269636415, ],
    [582405152, 882963765, ],
    [1031199132, 956873918, ],
    [769383716, -2062983524, ],
    [-1159400254, -475648556, ],
    [701591168, 2127194887, ],
    [-1962302382, -1111369721, ],
    [-373891040, 1357388589, ],
    [2122667855, -973242058, ],
    [1612525811, -1985897293, ],
    [-66895843, 211319568, ],
    [-1217093924, 844670010, ],
    [1315868863, -353212504, ],
    [-1173497104, 754434520, ],
    [-1507222093, -1818990546, ],
    [-433728148, 1068882627, ],
    [1457394798, 152223805, ],
    [337784355, -721074166, ],
    [-758535907, -467137256, ],
    [484686226, -820495512, ],
    [1950699767, -1281361732, ],
    [-2081838862, 1555839665, ],
    [-1304390691, 218894543, ],
    [-1088803235, 381472275, ],
    [-252778426, 789011764, ],
    [-1205916533, -1992659548, ],
    [-810738166, 2096270932, ],
    [-167422566, -371043058, ],
    [-1660532278, 1595941500, ],
    [1323188377, -1670718653, ],
    [688170175, -1740055306, ],
    [1549731793, -424337314, ],
    [1984865253, -505083622, ],
    [-1802087781, 1568496784, ],
    [-549858002, -1650258752, ],
    [-1360172271, -826388347, ],
    [1220420659, 195999882, ],
    [1779673057, 1747908696, ],
    [1822835818, -340104623, ],
    [1100628282, 1883854712, ],
    [-17118507, -1072397894, ],
    [-927118377, -95493596, ],
    [-297742395, -212184093, ],
    [-1479639658, -1695955572, ],
    [528515209, -247602585, ],
    [-2068179822, 723270609, ],
    [1865659032, 2129349138, ],
    [-1257967561, 1391870766, ],
    [2049258855, -584957357, ],
    [-1180733284, 534244201, ],
    [152825799, 1422082064, ],
    [1920961690, -1710276190, ],
    [166766480, -1404086176, ],
    [2137904345, -1686354764, ],
    [551772254, 82364584, ],
]

loop1.summarize()
loop2.summarize()
loop3.summarize()

print("RESULT BELOW:")
for initial_values in all_initial_values:
    mid_value1 = loop1.compute_terminal_values(*initial_values)
    print(mid_value1)
    mid_value2 = loop2.compute_terminal_values(*mid_value1)
    print(mid_value2)
    terminal_values = loop2.compute_terminal_values(*mid_value2)
    output_str = ''
    for each in terminal_values:
        output_str += f'{each} '
    print(output_str)