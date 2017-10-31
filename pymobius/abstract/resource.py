class Resource:

    def __init__(self, requestor):
        self.requestor = requestor

    def get(self, action, **kwargs):
        return self.requestor.get(self.resource, action, **kwargs)

    def post(self, action, **kwargs):
        return self.requestor.post(self.resource, action, **kwargs)
