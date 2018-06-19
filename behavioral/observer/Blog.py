from ABCSubject import ABCSubject

class Blog(ABCSubject):

    def publish_new_post(self, value):
        print('Publishing a post on the blog')
        self.notify(value)