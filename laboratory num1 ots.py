import turtle

def perform_switch_case(state, t, turn):
    horiz_len = 10   
    vert_len = 2    
    max_horiz = 5   

    if state == "INIT":
        t.setheading(180)   
        state = "LEFT"
        return state, turn

    if state == "LEFT":
        for _ in range(horiz_len):
            t.forward(10)
        turn += 1
        if turn >= max_horiz:
            state = "STOP"
        else:
            state = "DOWN_LEFT"
            t.setheading(270)  
        return state, turn

    if state == "DOWN_LEFT":
        for _ in range(vert_len):
            t.forward(10)
        state = "RIGHT"
        t.setheading(0)       
        return state, turn

    if state == "RIGHT":
        for _ in range(horiz_len):
            t.forward(10)
        turn += 1
        state = "DOWN_RIGHT"
        t.setheading(270)     
        return state, turn

    if state == "DOWN_RIGHT":
        for _ in range(vert_len):
            t.forward(10)
        state = "LEFT"
        t.setheading(180)     
        return state, turn

    if state == "STOP":
        return state, turn

    return state, turn


def draw():
    curr_state = "INIT"
    end_state = "STOP"
    t = turtle.Turtle()
    t.speed(0)
    turn = 0
    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if __name__ == "__main__":
    draw()