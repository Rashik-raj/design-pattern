class Handler:
    """Abstract Class"""

    def __init__(self,successor):
        self._successor = successor

    def handle(self,request):
        handled = self._handle(request)
        if not handled:
            self._successor.handle(request)

    def _handle(self,request):
        raise NotImplementedError('Must provide implementation in subclass')

class ConcreateHandler1(Handler):
    def _handle(self,request):
        if 0 < request <= 10:
            print('Request {} handled in {}'.format(request,self.__class__.__name__))
            return True

class DefaultHandler(Handler):
    def _handle(self,request):
        print('End of chain, Request {} has no handler'.format(request))
        return True

class Client:
    def __init__(self):
        self.handler = ConcreateHandler1(DefaultHandler(None))

    def delegate(self,requests):
        for request in requests:
            self.handler.handle(request)

c = Client()

requests = [2,5,30]
c.delegate(requests)