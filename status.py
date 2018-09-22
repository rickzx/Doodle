import collections

class Status(object):
    isQuit = False
    mode = "Listen"

    offset = 0
    scale = 1
    move = 0
    entitiesBuffer = collections.deque()
    objects = {}
    cache = {}
