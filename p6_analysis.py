from p6_game import Simulator

ANALYSIS = {}

def analyze(design):
    sim = Simulator(design)
    init = sim.get_initial_state()
    for i in range(0, design['width']):
        for j in range(0, design['height']):
            queue = [init]
            parent = {init: None}
            paths = []
            path = None
            while queue:
                current = queue.pop(0)
                position, abilities = current
                moves = sim.get_moves()
                for move in moves:
                    next_state = sim.get_next_state(current, move)
                    if next_state is not None and next_state not in parent:
                        parent[next_state] = current
                        queue.append(next_state)
                if position == (i,j):
                    path = []
                    
                    while current:
                        position, abilities = current
                        path = [position] + path
                        current = parent[current]
                    paths.append(path)
            if paths is not []:
                ANALYSIS[(i,j)] = paths

def inspect((i,j), draw_line):
    color = 0
    if (i,j) in ANALYSIS:
        for path in ANALYSIS[(i,j)]:
            color+=1
            for square in range(0, len(path)-1):
                draw_line(path[square], path[square+1], color, color)
    else:
        print "no path"
