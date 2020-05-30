class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    def __init__(self):
        self.name = "British"

    def speak_british(self):
        return "Hello?"

class Adapter:
    def __init__(self,object,**adapter_method):
        self._object = object
        self.__dict__.update(adapter_method)

    def __getattr__(self,attr):
        return getattr(self._object, attr)

objects = []
korean = Korean()
british = British()

objects.append(Adapter(korean, speak = korean.speak_korean))
objects.append(Adapter(british, speak = british.speak_british))

for obj in objects:
    print('{} says {}'.format(obj.name,obj.speak()))