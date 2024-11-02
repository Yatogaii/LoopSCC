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


x = ws.create_variables(1)[0]

loop1 = ws.define_loop([x > 100], [
    (x > 100, [
        [1, -1],  # x = x + 1001
    ]),
])

loop2 = ws.define_loop(x >= 0, [
    (x >= 0, [
        [1, -1],  # x = x
    ]),
])

all_initial_values = [
    [1161983176, -710317365, ],
    [-763545825, -1022117274, ],
    [545938580, -991845360, ],
    [903298371, -641860670, ],
    [-1143141732, -77869613, ],
    [-26000342, 1205677842, ],
    [-252915809, -1989005962, ],
    [-200735356, 880245600, ],
    [-1095803977, 829877156, ],
    [990232336, -746942045, ],
    [594324488, 1770402459, ],
    [2122779062, -850060287, ],
    [-1055536526, 1975702348, ],
    [-738237114, -1452497184, ],
    [302619643, -1575203288, ],
    [962210096, -170728981, ],
    [-247373942, 703396461, ],
    [-627192621, 668785300, ],
    [1136445554, 537027509, ],
    [-993235048, -1128020470, ],
    [-1437773647, -1786414976, ],
    [-1871876462, -517605255, ],
    [1401340372, 27476313, ],
    [-855743950, -567810392, ],
    [686574020, -2121808420, ],
    [347622879, -2055430665, ],
    [54255945, 973637921, ],
    [62139663, 1570363446, ],
    [1086401525, 1559102113, ],
    [-1079717877, -776410554, ],
    [-2113742152, 852782010, ],
    [-1936133153, 716348617, ],
    [1035518666, -1756840513, ],
    [-1529820560, 648921459, ],
    [1642729910, 410515640, ],
    [684349681, 477712666, ],
    [-1485734163, -1361465669, ],
    [1042819792, -704099823, ],
    [-1759312121, 1985249342, ],
    [170710609, -703922219, ],
    [-1943889885, -1137292913, ],
    [656871505, -2024703998, ],
    [-1124831837, -1610399017, ],
    [1932697730, 5507291, ],
    [1610011604, -1502581215, ],
    [-1294455533, -1724131237, ],
    [1700813303, 51532539, ],
    [-72888598, -171411198, ],
    [972530465, -1103203841, ],
    [-706676994, -41179698, ],
    [-572994543, 58033186, ],
    [-1625079149, 1154018793, ],
    [-1916141977, -1368061501, ],
    [29679277, -1980027586, ],
    [-387368856, -1168394110, ],
    [-1889501315, 1398155847, ],
    [1087028980, -1630137706, ],
    [-747100259, 1888059360, ],
    [1641956324, 158851072, ],
    [2014612926, -1446159264, ],
    [1836308484, -308362641, ],
    [270984158, 1380572632, ],
    [16429758, -1592735893, ],
    [-2070574919, 1811119234, ],
    [1836150639, 1045848215, ],
    [-186941400, 355631091, ],
    [1095189112, -451852132, ],
    [-1647525468, -2002598242, ],
    [1871782402, -1077111483, ],
    [1254520796, 1448396505, ],
    [-2096491419, -711155526, ],
    [-1596822322, 1308147730, ],
    [1644125296, 732523941, ],
    [-1396444929, 828777904, ],
    [898368306, -1574395664, ],
    [-1162760923, 1032983643, ],
    [108057253, -1454131116, ],
    [-454643585, 1606298283, ],
    [-1634933264, -1435841309, ],
    [592992030, 1674196998, ],
    [1335535839, -1155239649, ],
    [-242389745, -1873563324, ],
    [2094538442, 2136004890, ],
    [326416234, 1877706534, ],
    [-154894686, -838222515, ],
    [-1200899566, 951700122, ],
    [-1612595511, 2026929635, ],
    [183518420, -331338126, ],
    [-308736348, -1660036942, ],
    [-1253840720, -1100064880, ],
    [1843040189, -2014168623, ],
    [820491754, -1270436893, ],
    [344144666, 882533669, ],
    [812936493, 1179027426, ],
    [-994889219, 134924321, ],
    [2135439855, 678364345, ],
    [-781078955, 1862498542, ],
    [754330486, -707782598, ],
    [1658050481, -450152382, ],
    [1318681200, -629812284, ],
]

input_all_initial_values = []
for each in all_initial_values:
    input_all_initial_values.append([each[0]])

loop1.summarize()
loop2.summarize()


print("RESULT BELOW:")
for initial_values in all_initial_values:
    mid_value1 = loop1.compute_terminal_values(initial_values[0])
    i_mid_value = int(str(mid_value1[0]))
    mid_value1[0] = i_mid_value + initial_values[1] + 50
    terminal_values = loop2.compute_terminal_values(mid_value1[0])
    output_str = ''
    for each in terminal_values:
        output_str += f'{each} '
    print(output_str)