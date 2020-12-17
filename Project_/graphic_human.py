import math
from graphic import*


def body(x, y, k):
    ag = Aggregator()
    canvas = ag.canv

    ag.add(canvas.create_rectangle(
        x - k, y + 2*k, x + k, y + 6*k,
        fill='green', outline='green'
    ))
    ag.add(canvas.create_oval(
        x - 4 * k, y - 4 * k, x + 4 * k, y + 4 * k,
        fill='green', outline='green'
    ))
    ag.add(canvas.create_polygon(
        x -3*k, y + 18*k, x - 6*k, y + 8*k,
        x - k, y + 6*k, x + k, y + 6*k,
        x + 6*k, y + 8*k, x + 3*k, y + 18*k,
        fill='green', outline='green'
    ))


def right_hand(x, y, k, alpha_right):
    ag = Aggregator()
    canvas = ag.canv

    ag.add(canvas.create_polygon(
        x - 6*k, y + 8*k,
        x - 6*k + 2*k*math.cos(alpha_right), y + 8*k + 2*k*math.sin(alpha_right),
        x - 6*k - 18*k*math.sin(alpha_right) + 2*k*math.cos(alpha_right),
        y + 8*k + 18*k*math.cos(alpha_right)+ 2*k*math.sin(alpha_right),
        x - 6*k - 18*k*math.sin(alpha_right),  y + 8*k + 18*k*math.cos(alpha_right),
        fill='green', outline='green'
    ))


def left_hand(x, y, k, alpha_left):
    ag = Aggregator()
    canvas = ag.canv

    ag.add(canvas.create_polygon(
        x + 6 * k, y + 8 * k,
        x + 6 * k - 2 * k * math.cos(alpha_left), y + 8 * k + 2 * k * math.sin(alpha_left),
        x + 6 * k + 18 * k * math.sin(alpha_left) - 2 * k * math.cos(alpha_left),
        y + 8 * k + 18 * k * math.cos(alpha_left) + 2 * k * math.sin(alpha_left),
        x + 6 * k + 18 * k * math.sin(alpha_left), y + 8 * k + 18 * k * math.cos(alpha_left),
        fill='green', outline='green'
    ))


def right_leg(x, y, k, beta_right):
    ag = Aggregator()
    canvas = ag.canv

    ag.add(canvas.create_polygon(
        x - 4 * k, y + 16 * k,
        x - 4 * k + 4 * k * math.cos(beta_right), y + 16 * k + 4 * k * math.sin(beta_right),
        x - 4 * k - 24 * k * math.sin(beta_right) + 4 * k * math.cos(beta_right),
        y + 16 * k + 24 * k * math.cos(beta_right) + 4 * k * math.sin(beta_right),
        x - 4 * k - 24 * k * math.sin(beta_right), y + 16 * k + 24 * k * math.cos(beta_right),
        fill='green', outline='green'
    ))


def left_leg(x, y, k, beta_left):
    ag = Aggregator()
    canvas = ag.canv

    ag.add(canvas.create_polygon(
        x + 4 * k, y + 16 * k,
        x + 4 * k - 4 * k * math.cos(beta_left), y + 16 * k + 4 * k * math.sin(beta_left),
        x + 4 * k + 24 * k * math.sin(beta_left) - 4 * k * math.cos(beta_left),
        y + 16 * k + 24 * k * math.cos(beta_left) + 4 * k * math.sin(beta_left),
        x + 4 * k + 24 * k * math.sin(beta_left), y + 16 * k + 24 * k * math.cos(beta_left),
        fill='green', outline='green'
    ))


def draw_human(x, y, size, params):
    right_hand(x, y, size, params[0])
    left_hand(x, y, size, params[1])
    right_leg(x, y, size, params[2])
    left_leg(x, y, size, params[3])
    body(x, y, size)
