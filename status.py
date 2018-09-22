import collections

class Status(object):
    isQuit = False
    entitiesBuffer = collections.deque()
    objects = []
    cache = {}
