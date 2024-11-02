from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, z, y = INT.define_int("x"), INT.define_int("z"), INT.define_int("y")

# y=z-x
# z=x+y
loop = CFG.define_loop([[x < 100]], [
    [
        ([[y > 0]], [
            (
                (x, x + 1),
                (y, y - 1),
            )
        ]),
        ([[y <= 0]], [
            (
                (y, y + 1),
            )
        ]),
    ]
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
tests = [
    [(x, -2009334), (z, 903231), ],
    [(x, -4167490), (z, 3486694), ],
    [(x, 2649801), (z, 4162708), ],
    [(x, 4275904), (z, -9480356), ],
    [(x, 4989888), (z, 9962201), ],
    [(x, 2215565), (z, -4867607), ],
    [(x, 6997471), (z, 4710925), ],
    [(x, -1967868), (z, -7830902), ],
    [(x, 2434802), (z, 5715634), ],
    [(x, 9591041), (z, -8237245), ],
    [(x, 7544653), (z, -8669085), ],
    [(x, 3701262), (z, -8362007), ],
    [(x, 7818494), (z, 2688438), ],
    [(x, -1381763), (z, -3936058), ],
    [(x, -5846398), (z, 5738983), ],
    [(x, 2912078), (z, -4809594), ],
    [(x, -3032442), (z, -9917406), ],
    [(x, 304576), (z, -9819913), ],
    [(x, 4861297), (z, 1473400), ],
    [(x, -1419920), (z, 754242), ],
    [(x, 2103731), (z, -9411974), ],
    [(x, -5376728), (z, 7013554), ],
    [(x, 6516974), (z, 9008717), ],
    [(x, 5029869), (z, 8889666), ],
    [(x, -1419340), (z, -442449), ],
    [(x, 183224), (z, 211934), ],
    [(x, 6286191), (z, -9613501), ],
    [(x, 6034956), (z, -475722), ],
    [(x, 7618517), (z, 9159318), ],
    [(x, -7336871), (z, 7588451), ],
    [(x, -659111), (z, 2832333), ],
    [(x, 7718075), (z, -7186035), ],
    [(x, -6177089), (z, 8215583), ],
    [(x, -1934902), (z, 6337569), ],
    [(x, -7095487), (z, 5304395), ],
    [(x, 170097), (z, -2964610), ],
    [(x, 2516200), (z, -4647730), ],
    [(x, -9343221), (z, -5275243), ],
    [(x, 1823397), (z, -4389739), ],
    [(x, -8112818), (z, 9567893), ],
    [(x, -7082400), (z, 8244675), ],
    [(x, 6609832), (z, 2317021), ],
    [(x, 5317195), (z, -5195915), ],
    [(x, 9946243), (z, 503897), ],
    [(x, 190661), (z, 2182470), ],
    [(x, -5774358), (z, 548839), ],
    [(x, 9569160), (z, -5255948), ],
    [(x, -7930945), (z, 1379546), ],
    [(x, -4166092), (z, 5148847), ],
    [(x, 5152437), (z, -8109753), ],
    [(x, 1548089), (z, -2667049), ],
    [(x, 2236620), (z, -4838604), ],
    [(x, -6800287), (z, 5735323), ],
    [(x, -2618667), (z, -1247146), ],
    [(x, 7251161), (z, -9511389), ],
    [(x, 4451260), (z, -6262063), ],
    [(x, 9158038), (z, 871630), ],
    [(x, 8821225), (z, -308269), ],
    [(x, -2830813), (z, 1223520), ],
    [(x, 4462488), (z, 4533466), ],
    [(x, -6859084), (z, 8543733), ],
    [(x, 301564), (z, 7781165), ],
    [(x, -4164908), (z, -7842846), ],
    [(x, 4914761), (z, -9966810), ],
    [(x, -7176882), (z, 2232692), ],
    [(x, 4529021), (z, 809245), ],
    [(x, -9692190), (z, -697870), ],
    [(x, 5556524), (z, -3557173), ],
    [(x, -9780191), (z, -8175034), ],
    [(x, 6010554), (z, -1558926), ],
    [(x, -4232294), (z, 8455434), ],
    [(x, -6998951), (z, 6047724), ],
    [(x, 1202455), (z, -1462591), ],
    [(x, -9299356), (z, 1740782), ],
    [(x, -8322095), (z, -4902842), ],
    [(x, 9374277), (z, -294764), ],
    [(x, -3470012), (z, -981030), ],
    [(x, 6026721), (z, 6723013), ],
    [(x, 7516729), (z, -3060597), ],
    [(x, -8340590), (z, -2167267), ],
    [(x, -1754421), (z, 7213115), ],
    [(x, -8532836), (z, -2843036), ],
    [(x, -5131257), (z, -1542172), ],
    [(x, -8290451), (z, -7919947), ],
    [(x, -5380744), (z, 9915616), ],
    [(x, -1204722), (z, -4421632), ],
    [(x, 4841578), (z, 4249684), ],
    [(x, 4183552), (z, 9434793), ],
    [(x, -8538368), (z, -4524514), ],
    [(x, 9635113), (z, -8619732), ],
    [(x, 3392923), (z, 6664897), ],
    [(x, -381125), (z, -4701381), ],
    [(x, 1133163), (z, 3807213), ],
    [(x, 278679), (z, 9510732), ],
    [(x, -4805391), (z, 6607163), ],
    [(x, 1361922), (z, 1086514), ],
    [(x, 7229065), (z, 8490296), ],
    [(x, -370282), (z, 3635573), ],
    [(x, -9785502), (z, 1327060), ],
    [(x, 9892357), (z, -4834234), ],
]
for test in tests:
    x_val = test[0][1]
    z_val = test[1][1]
    y_val = z_val - x_val
    result = summarizer.solve([(x, x_val), (y, y_val)])
    x_val = int(result[0][1])
    y_val = int(result[1][1])
    z_val = x_val + y_val
    print(f"x = {x_val}")
    print(f"z = {z_val}")
