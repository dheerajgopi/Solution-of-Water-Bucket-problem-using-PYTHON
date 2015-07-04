queue = []
seen = {}

def test(oldState, newState, goal) :
    [newA, newB] = newState
    won = (newA == goal or newB == goal)
    add_state(oldState, newState)
    return won

def get_solution() :
    "return soln from latest state added"
    global queue
    solution = []
    state = queue[-1]
    while state :
        solution.append(str(state))
        state = get_parent(state)
    solution.reverse()
    return solution

def get_parent(childState) :
    "return parent of state, if it exists"
    global seen
    try : return seen[str(childState)]
    except : return None

def play_game(aMax, bMax, goal) :
    add_state("", [0,0]) # Start with empty buckets
    while True :
        oldstate = get_state()
        [aHas, bHas] = oldstate
        if test(oldstate, [aMax, bHas], goal) : #fill A from well
            break
        if test(oldstate, [0, bHas], goal) : #empty A
            break
        if test(oldstate, [aHas, bMax], goal) : #fill B from well
            break
        if test(oldstate, [aHas, 0], goal) : #empty B
            break
        howmuch = min(aHas, bMax - bHas)
        if test(oldstate, [aHas - howmuch, bHas + howmuch], goal) : #pour A to B
            break
        howmuch = min(bHas, aMax - aHas)
        if test(oldstate, [aHas + howmuch, bHas - howmuch], goal) : #pour B to A
            break

    print "Solution is "
    return '\n'.join(get_solution())

def get_state() :
    "Pop next state from queue and return"
    global queue
    if not queue : return None
    state = queue.pop(0)
    return state

def add_state(parentState, newState) :
    "Add state to 'seen' dict if its new. Remember its parent"
    global seen
    global queue
    if seen.has_key(str(newState)) :
        return
    seen[str(newState)] = str(parentState)
    queue.append(newState)

print play_game(7, 11, 6)
