from Blog import Blog
from Subscriber import Subscriber
from ABCSubject import ABCSubject

blog = Blog()

s1 = Subscriber()
s2 = Subscriber()
s3 = Subscriber()

blog.add_subscriber(s1)
blog.add_subscriber(s2)

blog.publish_new_post('This is a brand new post')

blog.add_subscriber(s3)

blog.publish_new_post('A second post')

blog.remove_subscriber(s1)

blog.publish_new_post('A third and last post')