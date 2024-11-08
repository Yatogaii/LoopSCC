from compare import compare
from wsummarizer import WSummarizer as ws


def input_loop(n):
    path = ""
    flag = 1

    while flag > 0:
        if n > 0:
            n = n - 1
            flag = 1
            path += "A"
        else:
            flag = 0
            path += "B"

    return [n, flag, path]


n, flag = ws.create_variables(2)

loop = ws.define_loop([flag > 0], [
    (n > 0, [
        [1, 0, -1],  # n = n - 1
        [0, 0, 1],  # flag = 1
    ]),
    (n <= 0, [
        [1, 0, 0],  # n = n
        [0, 0, 0],  # flag = 0
    ]),
])

all_initial_values = [
    [458248621, ],
    [1697209260, ],
    [-1936923523, ],
    [-1005688832, ],
    [-484847094, ],
    [1600200083, ],
    [-939194118, ],
    [379372529, ],
    [1043515149, ],
    [1532864509, ],
    [2007789245, ],
    [-901956104, ],
    [-2026285821, ],
    [-1785978338, ],
    [210486406, ],
    [797400109, ],
    [354221994, ],
    [-282377649, ],
    [700255887, ],
    [-1488199506, ],
    [-903489517, ],
    [367887345, ],
    [-1982819054, ],
    [-2026983352, ],
    [242553869, ],
    [-1075706234, ],
    [-2030521082, ],
    [1619213302, ],
    [1937041872, ],
    [482246540, ],
    [-732697991, ],
    [1196297476, ],
    [661480097, ],
    [1969641338, ],
    [1619689722, ],
    [2081189784, ],
    [1829383667, ],
    [521155408, ],
    [2126839260, ],
    [-539950826, ],
    [-1278558907, ],
    [-2120548366, ],
    [-978406705, ],
    [260801100, ],
    [-1302281358, ],
    [-139720234, ],
    [1671944467, ],
    [-1145921066, ],
    [-175394641, ],
    [1834119327, ],
    [320538060, ],
    [-142363884, ],
    [1001373513, ],
    [1187229504, ],
    [2134981102, ],
    [2061366878, ],
    [179597405, ],
    [-852385013, ],
    [-1516438164, ],
    [794365374, ],
    [836582685, ],
    [18033114, ],
    [2141012342, ],
    [802451081, ],
    [-1537528150, ],
    [780848147, ],
    [1758596622, ],
    [1231193591, ],
    [-836037502, ],
    [288956639, ],
    [761416907, ],
    [553724280, ],
    [-1588994051, ],
    [144632177, ],
    [-2045661005, ],
    [976437055, ],
    [855528726, ],
    [-374981533, ],
    [1682310821, ],
    [247057593, ],
    [-57455458, ],
    [-1357146406, ],
    [-644261706, ],
    [1050864001, ],
    [-895079451, ],
    [-1030747934, ],
    [1609056819, ],
    [689074726, ],
    [-1507841609, ],
    [-1021984243, ],
    [-1009331087, ],
    [-1428890111, ],
    [-1312175000, ],
    [63325371, ],
    [-245078180, ],
    [-829109663, ],
    [-1715893885, ],
    [1538150929, ],
    [-2090148936, ],
    [-1810895724, ],
]


loop.summarize()

print("RESULT BELOW:")
for initial_values in all_initial_values:
    terminal_values = loop.compute_terminal_values(*initial_values)
    output_str = ''
    for each in terminal_values:
        output_str += f'{each} '
    print(output_str)