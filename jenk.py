import os

print(os.environ['name'])


print('ALL_test_1336', os.environ)



# def auth_with():
#     jenkins_param = os.environ['profile']
#     profiles = {'user':('login', 'password'),
#                 'root':('login', 'password'),
#                 'administrator':('login', 'password'),
#                 'supervisor':('login', 'password')}
#     if jenkins_param in profiles.keys():
#         return jenkins_param, profiles[jenkins_param]
#     else:
#         return jenkins_param, profiles['root']
#
#
#
# if jenkins_param == 'root':
#     assert foo == True