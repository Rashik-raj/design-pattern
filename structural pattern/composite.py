class Component:
    """ Abstract class """
    def __init__(self,*args,**kwarg):
        pass

    def component_function(self):
        pass

class Child(Component):
    """ Concrete class """
    def __init__(self,*args,**kwargs):
        Component.__init__(self,*args,**kwargs)
        self.name = args[0]

    def component_function(self):
        print('{}'.format(self.name))

class Composite(Component):
    """ Concrete class and maintains tree recusrive structure """

    def __init__(self,*args,**kwargs):
        Component.__init__(self,*args,**kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self,child):
        self.children.append(child)

    def remove_child(self,child):
        self.children.remove(child)

    def component_function(self):
        print('{}'.format(self.name))
        for i in self.children:
            i.component_function()

sub1 = Composite("Submenu 1")
sub11 = Child("Submenu 11")
sub12 = Child("Submenu 12")
sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("Top Menu")

sub2 = Child("Submenu 2")

top.append_child(sub1)
top.append_child(sub2)

top.component_function()