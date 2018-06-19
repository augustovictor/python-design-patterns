from PushNotification import PushNotification
from Subscriber import Subscriber

publisher = PushNotification()
s1 = Subscriber()
s2 = Subscriber()
s3 = Subscriber()

publisher.add_subscriber(s1)
publisher.add_subscriber(s2)

publisher.publish_something('victor')

publisher.remove_subscriber(s1)

publisher.publish_something('second content')

publisher.add_subscriber(s3)

publisher.publish_something('Third content')