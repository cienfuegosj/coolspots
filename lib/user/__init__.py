from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def __repr__(self):
        return "{0}:{1}".format(self.id, self.email)

    def __str__(self):
        return self.email


class DevelopmentUser(object):
    def __init__(self, e, p, f, l, d):
        self.email = e
        self.password = p
        self.firstname = f
        self.lastname = l
        self.datecreated = d

    def __str__(self):
        print("{0}, {1}, {2}".format(self.e, self.f, self.l))