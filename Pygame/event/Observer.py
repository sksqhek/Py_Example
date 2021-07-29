class Subject(object):

    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.notify(event)


class IObserver(object):
    def notify(self, event):
        raise NotImplementedError("Must subclass and overwrite me")


# overwrite the observer's notify so
# custom code is executed
class PrintObserver(IObserver):
    def notify(self, event):
        print("observer", self, "got event:", event)


# create a subject
subject = Subject()

# create two observers and register them to the subject
observer1 = PrintObserver()
subject.register(observer1)
observer2 = PrintObserver()
subject.register(observer2)

# send an event
subject.notify("hello1")
subject.notify("hello2")