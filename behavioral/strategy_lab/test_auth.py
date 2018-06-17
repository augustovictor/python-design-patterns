from Auth import Auth
from FacebookStrategy import FacebookStrategy
from TwitterStrategy import TwitterStrategy
from User import User

# Auth with facebook
user = User('user1')
strategy = FacebookStrategy()
token = Auth(strategy).auth(user)
assert token == f'tokenFb{user.name}'

# Auth with twitter
user = User('user2')
strategy = TwitterStrategy()
token = Auth(strategy).auth(user)
assert token == f'tokenTwitter{user.name}'

print('All good')