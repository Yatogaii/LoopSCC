import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, j = INT.define_int("i"), INT.define_int("j")

loop = CFG.define_loop([[i < 100]], [
    (
        (i, i + 1),
        (j, j + 2),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

i_pre = z3.Int('i_0')
j_pre = z3.Int('j_0')
j_post = z3.Int('j')

summarizer.check_after_loop([i_pre == 0, j_pre == 0],
                            {"j": j_post},
                            [200 == j_post])