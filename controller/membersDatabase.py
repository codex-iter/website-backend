from model.Member import Member
from bson import ObjectId

'''
This function is responsible for handling all the exceptions for json data request object
@param data: json data received from client
'''
def addMembers(data):
    if 'linkedin' not in data:
        data['linkedin']=None

    if 'twitter' not in data:
        data['twitter']=None
    
    try:
        m = Member(
        name=data['name'],
        role=data['role'],
        skill=data['skill'],
        github=data['github'],
        githubDP=data['githubDP'],
        linkedin=data['linkedin'],
        twitter=data['twitter'],
        )
        m.insert()

        return True
    except:
        return False

def getMembers():
    return Member.query({
        '$or': [
            {
                'role': 'member'
            },
            {
                'role': 'teacher'
            },
            {
                'role': 'coordinator'
            }
        ]
    })

def getAlumni():
    return Member.query({
        'role': 'alumni'
    })

def delMember(data):
    if 'id' not in data:
        return False

    Member.delete({
        '_id': ObjectId(data['id'])
    })
    return True