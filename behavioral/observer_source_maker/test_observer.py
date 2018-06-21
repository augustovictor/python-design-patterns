from AbsObserver import AbsObserver
from Subject import Subject
from Observer import Observer

# obs = AbsObserver()
subject = Subject()

o1 = Observer('obs1')
o2 = Observer('obs2')
o3 = Observer('obs3')

subject.add_subscriber(o1)

subject.post('First passed value')

subject.add_subscriber(o3)
subject.post('Second value posted...')

subject.remove_subscriber(o1)
subject.post('Third value posted')

subject.add_subscriber(o2)
o2.subject.post('Value from o2')