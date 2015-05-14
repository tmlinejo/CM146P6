from p6_game import Simulator

ANALYSIS = {}

def analyze(design):
    sim = Simulator(design)
    init = sim.get_initial_state()
    
    for i in range(0, design['width']): # prepare list of lists
        for j in range(0, design['height']):
            ANALYSIS[(i,j)] = []
            
    queue = [init] # search setup
    parent = {init: None}
    
    while queue: # BFS
        current = queue.pop(0)
        position, abilities = current
        
        if parent[current] is not None: # add new path to current location
            previous, junk = parent[current]
            path = ANALYSIS[previous][len(ANALYSIS[previous])-1] + [position]
        else: # initial state case
            path = [position]
        ANALYSIS[position].append(path)
        
        moves = sim.get_moves() # add all new possibilities to queue
        for move in moves:
            next_state = sim.get_next_state(current, move)
            if next_state is not None and next_state not in parent: # if next_state is valid and new
                parent[next_state] = current
                queue.append(next_state)

def inspect((i,j), draw_line):
    color = 0
    if (i,j) in ANALYSIS:
        for path in ANALYSIS[(i,j)]:
            color+=1
            for square in range(0, len(path)-1):
                draw_line(path[square], path[square+1], color, color)
    else:
        print "no path"
