def spacing():
    return "\n\n"

def update_pos(current_pos, rel_dist):
    new_pos = [current_pos[0]+rel_dist, current_pos[1], current_pos[2]]
    return new_pos
