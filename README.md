# python-design-patterns

## Behavioral
### Strategy
Defines a set of encapsulated algorithms that can be swapped to carry out a specific behaviour

Elements:
- Client
- Context
- Abstract class
- Implementations

### Observer
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

- Abstract Subject
- Concrete subject
- AbstractObserver
- ConcreteObserver

### Command
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

Benefits:
- Each command is encapsulated in objects
- The client does not need to pass any arguments. Just execute the command
- Easy to add new commands by adding new concrete commands


### State
Allows an object to alter its behaviour when its internal state changes. The object will appear to change its class.

Elements
- Context: Holds internal state
- State interface
- Concrete state

### Template method
Defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithms structure.

