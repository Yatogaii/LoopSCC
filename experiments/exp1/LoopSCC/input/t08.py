from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

y, z = INT.define_int("y"), INT.define_int("z")

var_map = {"y": y, "z": z}

loop1 = CFG.define_loop([[z > y]], [
    [
        ([[z == z]], [
            (
                (y, y + 1),
            )
        ]),
    ]
])

loop2 = CFG.define_loop([[y > 2]], [
    [
        ([[y == y]], [
            (
                (y, y - 3),
            )
        ]),
    ]
])

spg = SPath_Graph(loop1)
summarizer = Summarizer(spg)
summarizer.summarize()

spg2 = SPath_Graph(loop2)
summarizer2 = Summarizer(spg2)
summarizer2.summarize()
tests = [
    [(y, 1940083), (z, 7424199), ],
    [(y, 9717701), (z, 8576676), ],
    [(y, 2460871), (z, -4123190), ],
    [(y, 8997060), (z, 3754085), ],
    [(y, 3044873), (z, 6980736), ],
    [(y, 1132502), (z, -5812749), ],
    [(y, -6694534), (z, 2140166), ],
    [(y, 3150441), (z, 6066725), ],
    [(y, 3580807), (z, -2840490), ],
    [(y, 3315174), (z, -5828650), ],
    [(y, -7947407), (z, -7031160), ],
    [(y, -8458036), (z, -5773356), ],
    [(y, -9487942), (z, -5523224), ],
    [(y, 4989839), (z, -5838575), ],
    [(y, -2409171), (z, -9984403), ],
    [(y, 5120404), (z, 4036070), ],
    [(y, 3771487), (z, 9465080), ],
    [(y, 4517226), (z, 1730325), ],
    [(y, -7005206), (z, 6181409), ],
    [(y, 7127993), (z, 9640031), ],
    [(y, -4113837), (z, -2619068), ],
    [(y, 6982100), (z, 1036911), ],
    [(y, 3847529), (z, -6813086), ],
    [(y, -1837840), (z, -4586905), ],
    [(y, -2810062), (z, 9167068), ],
    [(y, 1511485), (z, -1943214), ],
    [(y, 200529), (z, -7815337), ],
    [(y, 4902918), (z, -3413510), ],
    [(y, 2911778), (z, 3911230), ],
    [(y, 2001842), (z, -8876962), ],
    [(y, 8801583), (z, -2088460), ],
    [(y, 1739052), (z, -3203290), ],
    [(y, 9785805), (z, -8449491), ],
    [(y, 9994020), (z, 1927638), ],
    [(y, 4584497), (z, 6924125), ],
    [(y, -5555746), (z, 2652151), ],
    [(y, 4023596), (z, 9010605), ],
    [(y, 1754029), (z, 5053613), ],
    [(y, -5879599), (z, -4628895), ],
    [(y, -1171207), (z, -7241689), ],
    [(y, 3754573), (z, 7200563), ],
    [(y, -3242049), (z, -5721110), ],
    [(y, 1635305), (z, -5305956), ],
    [(y, -9238946), (z, 7715017), ],
    [(y, -3582073), (z, -567378), ],
    [(y, 2221418), (z, -7044371), ],
    [(y, 7898201), (z, -840009), ],
    [(y, -3954526), (z, 9127291), ],
    [(y, 6456116), (z, -2182139), ],
    [(y, 8494648), (z, -8210967), ],
    [(y, 6955787), (z, 6889891), ],
    [(y, -5029078), (z, 3629248), ],
    [(y, 108467), (z, 6250840), ],
    [(y, 3197013), (z, -7180015), ],
    [(y, -9619823), (z, 4387556), ],
    [(y, 1981358), (z, 8885387), ],
    [(y, -6544094), (z, -5215902), ],
    [(y, 5715117), (z, 8594355), ],
    [(y, -7625555), (z, 6663280), ],
    [(y, 5215256), (z, 648583), ],
    [(y, -940862), (z, -4824259), ],
    [(y, 7213598), (z, -3159691), ],
    [(y, 7520266), (z, -5210102), ],
    [(y, 396904), (z, -4076690), ],
    [(y, 4316978), (z, 2156801), ],
    [(y, 9822231), (z, -732804), ],
    [(y, 7480931), (z, -4154774), ],
    [(y, 8964764), (z, -4417815), ],
    [(y, 4643197), (z, 7454584), ],
    [(y, 7074914), (z, 2452406), ],
    [(y, 9528325), (z, 6371356), ],
    [(y, 4930068), (z, 6731391), ],
    [(y, -2936235), (z, -6960175), ],
    [(y, -2912755), (z, 8101413), ],
    [(y, 8033466), (z, 2807053), ],
    [(y, -2505696), (z, 9571451), ],
    [(y, 7247995), (z, 1945984), ],
    [(y, 1933413), (z, -3188751), ],
    [(y, 7163518), (z, -5816983), ],
    [(y, -8699419), (z, -4892740), ],
    [(y, 1917651), (z, 9576781), ],
    [(y, -4554381), (z, -4560734), ],
    [(y, -866465), (z, -480605), ],
    [(y, 4484401), (z, -2653054), ],
    [(y, -4176277), (z, 9499862), ],
    [(y, -1410246), (z, -8127814), ],
    [(y, -6564810), (z, -3854050), ],
    [(y, 7790605), (z, -7372981), ],
    [(y, -3940911), (z, -2328867), ],
    [(y, 4585198), (z, -2095839), ],
    [(y, -5987887), (z, -7979586), ],
    [(y, 5124268), (z, -2682129), ],
    [(y, 8495533), (z, -8090493), ],
    [(y, 3759860), (z, 8518594), ],
    [(y, 4739032), (z, -9529418), ],
    [(y, 698921), (z, 2464630), ],
    [(y, 5325818), (z, 1388682), ],
    [(y, 9322714), (z, 7689890), ],
    [(y, -3307482), (z, -8028320), ],
    [(y, 1652755), (z, 8223281), ],
]
for test in tests:
    # res1 = List[tuple('symbol_name', 'symbol_var')]
    res1 = summarizer.solve(test)
    y_val = res1[0][1]
    z_val = res1[1][1]

    input2 = [(y, y_val),(z, z_val)]

    result = summarizer2.solve(input2)
    y_val = result[0][1]
    print(f"y = {y_val}")
