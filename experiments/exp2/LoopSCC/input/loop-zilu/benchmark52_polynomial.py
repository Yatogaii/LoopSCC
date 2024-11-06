from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i = INT.define_int("i")

loop = CFG.define_loop([[i*i < 100]], [
    (
        (i,i+1),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Result verification
import z3
i_pre = z3.Int('i_0')
i_post = z3.Int('i')
summarizer.check_after_loop([i_pre<10,i>-10], {"i": i_post}, [i == 0])
