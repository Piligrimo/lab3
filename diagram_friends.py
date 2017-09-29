from vk_clients import *

get_user = GettingID('janmakin')
user = get_user.execute()
user_id = user.get('id')

get_friends = GettingFriends(user_id)
friends = get_friends.execute()

age_list = [0 for i in range(120)]
today = datetime.now()

print(user.get('last_name')+" "+user.get('first_name'))

for f in friends:
    age_list[f] += 1

for i in range(120):
    if age_list[i]>0:
        print(i,': ','#'*age_list[i])
