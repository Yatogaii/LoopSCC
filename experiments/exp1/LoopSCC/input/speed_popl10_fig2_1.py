from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < 100]], [
    [
        ([[y < 30]], [
            (
                (y, y + 1),
            )
        ]),
        ([[y >= 30]], [
            (
                (x, x + 1),
            )
        ]),
    ]
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
tests = [
    [(x, 3245541), (y, -1213102), ],
    [(x, 886029), (y, 5311931), ],
    [(x, -4514745), (y, -5088826), ],
    [(x, -2427569), (y, -4824415), ],
    [(x, 4612336), (y, 4035510), ],
    [(x, 5028975), (y, -7354206), ],
    [(x, 3836158), (y, -5327801), ],
    [(x, -2991193), (y, 710477), ],
    [(x, -477481), (y, 9370900), ],
    [(x, -3105550), (y, -700040), ],
    [(x, -9132719), (y, -4543852), ],
    [(x, -6032232), (y, -9779214), ],
    [(x, 6041192), (y, 2603305), ],
    [(x, 2070331), (y, 5904506), ],
    [(x, -7782505), (y, -277906), ],
    [(x, 882635), (y, 1865028), ],
    [(x, -9179712), (y, 5519612), ],
    [(x, 6880642), (y, -5387038), ],
    [(x, -3421752), (y, -1325366), ],
    [(x, 7208434), (y, -5450296), ],
    [(x, -9752894), (y, -1135524), ],
    [(x, -610316), (y, 3572009), ],
    [(x, 3589621), (y, -4476104), ],
    [(x, -8795546), (y, -4287590), ],
    [(x, -8438128), (y, 2096895), ],
    [(x, -6732799), (y, 2745140), ],
    [(x, -9559125), (y, 6898877), ],
    [(x, 7858567), (y, -5165084), ],
    [(x, 2626950), (y, 3844333), ],
    [(x, -5935714), (y, 8948231), ],
    [(x, -8043349), (y, 9199409), ],
    [(x, -787475), (y, 402827), ],
    [(x, -187433), (y, -3436087), ],
    [(x, 4644409), (y, 8494347), ],
    [(x, 5609808), (y, 4570904), ],
    [(x, 5965375), (y, -8349971), ],
    [(x, 5320149), (y, 7417622), ],
    [(x, -7453670), (y, -4790618), ],
    [(x, 8322967), (y, 455727), ],
    [(x, -1331052), (y, 9362309), ],
    [(x, 2717332), (y, -7860326), ],
    [(x, -1943331), (y, 5956739), ],
    [(x, 4399273), (y, -3847929), ],
    [(x, 3299781), (y, -3057265), ],
    [(x, -7255783), (y, 9202580), ],
    [(x, -7394873), (y, 6596307), ],
    [(x, 6275574), (y, -5320002), ],
    [(x, 7791117), (y, -7597247), ],
    [(x, 9803190), (y, -4202086), ],
    [(x, -8336238), (y, 4878423), ],
    [(x, -9103577), (y, -1711545), ],
    [(x, 7556670), (y, 9002976), ],
    [(x, -3119619), (y, 1295988), ],
    [(x, 9105982), (y, -245622), ],
    [(x, 9100056), (y, 5097601), ],
    [(x, -3766436), (y, -8976906), ],
    [(x, 4938471), (y, -7339342), ],
    [(x, 7286793), (y, 1930837), ],
    [(x, -9724500), (y, 3584790), ],
    [(x, 8127652), (y, -7984067), ],
    [(x, 5680570), (y, -7164177), ],
    [(x, -8167732), (y, 7020033), ],
    [(x, -4431261), (y, -2551551), ],
    [(x, 1428272), (y, -9673863), ],
    [(x, 615511), (y, -3820083), ],
    [(x, -431612), (y, -274824), ],
    [(x, -7522234), (y, -5591212), ],
    [(x, 5217328), (y, 6886174), ],
    [(x, -25900), (y, -8862601), ],
    [(x, 6391510), (y, 9765612), ],
    [(x, -6668830), (y, 711138), ],
    [(x, 8243985), (y, 1780069), ],
    [(x, -9137883), (y, 2384682), ],
    [(x, 8024696), (y, -3457382), ],
    [(x, -7921754), (y, 788560), ],
    [(x, 3320299), (y, 7701849), ],
    [(x, -295917), (y, -4650932), ],
    [(x, 9124731), (y, -8552131), ],
    [(x, -2330302), (y, 1719150), ],
    [(x, -7951897), (y, 2628143), ],
    [(x, -2376282), (y, 2444596), ],
    [(x, -4863096), (y, 2181250), ],
    [(x, 7392725), (y, -1283233), ],
    [(x, 4635213), (y, 3972317), ],
    [(x, -9909121), (y, -1983663), ],
    [(x, -4093446), (y, -42809), ],
    [(x, 7010995), (y, -1461000), ],
    [(x, -1114699), (y, 5882698), ],
    [(x, -5524488), (y, -2373533), ],
    [(x, -4491676), (y, 3726825), ],
    [(x, -9410778), (y, -3259784), ],
    [(x, -6950766), (y, -3305164), ],
    [(x, 254227), (y, 9633670), ],
    [(x, 4910668), (y, -7349139), ],
    [(x, -4473001), (y, 2587805), ],
    [(x, -3428720), (y, 3683494), ],
    [(x, 6103387), (y, 5107242), ],
    [(x, -7475700), (y, 199257), ],
    [(x, 6961839), (y, 9916586), ],
    [(x, -3394194), (y, 1337117), ],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")