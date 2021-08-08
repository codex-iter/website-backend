from model.Member import Member

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