import requests
import random

 
m = random.randint(0000, 99999)
def requ(nepc_id):
    
    data = {}
    url = 'https://nepc.gov.ng/ereg/api/public/search'
    headers = {
        'X-Requested-With': 'ECVPHttpRequest',
        }
    hey = {'Search': '{}'.format(nepc_id)}
    try:
        r = requests.post(url, data=hey, headers=headers)
    except: 
        r = None


    if r is not None:
        b = str(r.content)
        d = 'is registered'
        e = 'expired'
        # print(f)
        if r.ok is True : 

            if d in b:
                data['success'] = 'The NEPC ID is Valid'
                data['status'] = 200
                data['nepc_id'] = nepc_id
            elif e in b:
                data['success'] = 'The NEPC ID has expired'
                data['status'] = 200
                data['nepc_id'] = nepc_id
            else:
                data['success'] = 'The NEPC ID does not exist'
                data['status'] = 200
                data['nepc_id'] = nepc_id
            return data 

        else:
            data['error'] = 'There was an Error '
            data['status'] = 400 
            data['nepc_id'] = nepc_id
            return data
    else:
        data['error'] = 'There was an error'
        data['status'] = 500
        data['nepc_id'] = nepc_id
        return data
  


  
print(requ(m))