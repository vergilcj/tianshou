class Batch(object):
    """Suggested keys: [obs, act, rew, done, obs_next, info]"""
    def __init__(self, **kwargs):
        super().__init__()
        self.obs_next = None
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        self.__dict__.update(kwargs)
