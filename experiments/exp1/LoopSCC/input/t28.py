from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop1 = CFG.define_loop([[x > y]], [
    [
        ([[x == x]], [
            (
                (x, x - 1),
                (x, x + 1000),
                (y, y + 1000),
            )
        ]),
    ]
])

loop2 = CFG.define_loop([[y > 0]], [
    [
        ([[y == y]], [
            (
                (y, y - 1),
            )
        ]),
    ]
])

loop3 = CFG.define_loop([[x < 0]], [
    [
        ([[x == x]], [
            (
                (x, x + 1),
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

spg3 = SPath_Graph(loop3)
summarizer3 = Summarizer(spg3)
summarizer3.summarize()
tests = [
    [(x, -7644787), (y, 8100673), ],
    [(x, -6294542), (y, -6932221), ],
    [(x, -4928057), (y, 9894544), ],
    [(x, -2123149), (y, 4644194), ],
    [(x, -1750376), (y, 7461830), ],
    [(x, 6935014), (y, 8320038), ],
    [(x, -7191820), (y, 9662825), ],
    [(x, 4414948), (y, 6776350), ],
    [(x, -9792274), (y, -7669523), ],
    [(x, -2074769), (y, -1690502), ],
    [(x, -8431253), (y, 2737828), ],
    [(x, -265438), (y, 4060629), ],
    [(x, -4283413), (y, 3805126), ],
    [(x, 5321710), (y, 8226472), ],
    [(x, -6383492), (y, 8106193), ],
    [(x, -4393244), (y, 6750485), ],
    [(x, 8361779), (y, 8655884), ],
    [(x, -9199929), (y, -8359413), ],
    [(x, -4802538), (y, 4700728), ],
    [(x, -6146413), (y, -7015549), ],
    [(x, -1214612), (y, 6690368), ],
    [(x, -4643438), (y, 8991289), ],
    [(x, -3849133), (y, 1286513), ],
    [(x, -2577551), (y, -1944078), ],
    [(x, 3832105), (y, 4063941), ],
    [(x, -3622181), (y, 7539836), ],
    [(x, -2981390), (y, 7715359), ],
    [(x, -3313659), (y, -177543), ],
    [(x, 9324397), (y, 9714400), ],
    [(x, -3726211), (y, 2997782), ],
    [(x, -7871468), (y, 1089885), ],
    [(x, -3868700), (y, -4298624), ],
    [(x, -6550135), (y, 5525679), ],
    [(x, -5627296), (y, 4107329), ],
    [(x, 2242598), (y, 2870014), ],
    [(x, -3069665), (y, -2662781), ],
    [(x, 4543715), (y, 7004294), ],
    [(x, -4222967), (y, 5323745), ],
    [(x, -9763069), (y, 1381961), ],
    [(x, -5045180), (y, -2034125), ],
    [(x, -2971044), (y, 8920646), ],
    [(x, 677118), (y, 21318), ],
    [(x, -3932006), (y, 7094699), ],
    [(x, -9208548), (y, -733081), ],
    [(x, 4882604), (y, 5027363), ],
    [(x, 3954875), (y, 3135101), ],
    [(x, -6569821), (y, -1947809), ],
    [(x, 252128), (y, 564151), ],
    [(x, -8954940), (y, -2349650), ],
    [(x, -2444026), (y, 2155468), ],
    [(x, -6663463), (y, -2564673), ],
    [(x, -166764), (y, 345414), ],
    [(x, -278316), (y, 9019602), ],
    [(x, -807884), (y, 2979255), ],
    [(x, 6839659), (y, 9489639), ],
    [(x, -7650508), (y, 8471670), ],
    [(x, -9845955), (y, -9045841), ],
    [(x, -7218244), (y, -4713405), ],
    [(x, 2309218), (y, 7218348), ],
    [(x, -9447796), (y, 7901170), ],
    [(x, 2896952), (y, 6995928), ],
    [(x, -5057592), (y, 6177651), ],
    [(x, -7083334), (y, 8629478), ],
    [(x, -6576769), (y, -3178710), ],
    [(x, -4001528), (y, 9498842), ],
    [(x, -6152057), (y, 122375), ],
    [(x, -4269652), (y, 2161786), ],
    [(x, -8500600), (y, -3798876), ],
    [(x, -9760404), (y, -5062950), ],
    [(x, -8433376), (y, 7639369), ],
    [(x, -3737159), (y, 1344488), ],
    [(x, -3799514), (y, 143432), ],
    [(x, -7782051), (y, 8795847), ],
    [(x, 3217384), (y, 5112260), ],
    [(x, 3658172), (y, 7160091), ],
    [(x, 6465198), (y, 5969629), ],
    [(x, -4725899), (y, 9543014), ],
    [(x, -9878210), (y, -9605453), ],
    [(x, -9104148), (y, 3968349), ],
    [(x, 1201172), (y, 259354), ],
    [(x, -5097206), (y, 5287663), ],
    [(x, -5192172), (y, -116366), ],
    [(x, 1274900), (y, 3403959), ],
    [(x, -9845050), (y, -9289943), ],
    [(x, -222348), (y, 3415560), ],
    [(x, -4891329), (y, -5564369), ],
    [(x, -8172476), (y, -4911669), ],
    [(x, 1706075), (y, 1867535), ],
    [(x, 919169), (y, 1316977), ],
    [(x, 2890984), (y, 8104730), ],
    [(x, -1895267), (y, 1007760), ],
    [(x, -8514566), (y, -2096797), ],
    [(x, -540413), (y, 418697), ],
    [(x, 7610077), (y, 7066894), ],
    [(x, -5697403), (y, 9525649), ],
    [(x, -8696633), (y, 9055965), ],
    [(x, -8403704), (y, -5613180), ],
    [(x, 2042435), (y, 5288412), ],
    [(x, -7700224), (y, -4525208), ],
    [(x, -8597777), (y, 4536797), ],
]
for test in tests:
    res1 = summarizer.solve(test)

    x_val = res1[0][1]
    y_val = res1[1][1]
    res2 = summarizer2.solve([(y, y_val)])

    y_val = res2[0][1]
    res3 = summarizer3.solve([(x, x_val)])

    x_val = res3[0][1]
    print(f"x = {x_val}")
    print(f"y = {y_val}")
