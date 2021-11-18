state = {}

def update_state(new_state):
    global state
    state = new_state

def get_state():
    global state
    return state

def set_value_for_path(path, value):
    curr = state
    try:
        for index, p in enumerate(path):
            if index == len(path) - 1:
                curr[p] = value
                return
            curr = curr[p]
    except:
        print("invalid path: path should already exist in state", path)

def get_value_for_path(path):
    curr = state
    try:
        for index, p in enumerate(path):
            if index == len(path) - 1:
                return curr[p]
            curr = curr[p]
    except:
        print("invalid path: path should already exist in state", path)