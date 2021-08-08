from controller.mongodbOperations import addRecord, searchRecord, deleteRecord

class Member:
    def __init__(self, name, role, skill, github, githubDP, twitter=None, linkedin=None):
        self.name=name
        self.role=role
        self.skill=skill
        self.twitter=twitter
        self.linkedin=linkedin
        self.github=github
        self.githubDP=githubDP
        
    def insert(self):
        data ={
            'name': self.name,
            'role': self.role,
            'skill': self.skill,
            'twitter': self.twitter,
            'linkedin': self.linkedin,
            'github': self.github,
            'githubDP': self.githubDP
        }

        return addRecord('members', data)

    def query(q={}):
        return searchRecord('members', q)

    def delete(q):
        deleteRecord('members', q)