sample_info = """My name is Anna
My age is 101  
My country of birth is The United States
My favorite language is Python"""

my_info =  {'name': 'nate',
            'age': 101,
            'age_unit': 'standard 15 week semesters',
            'height': "6'2\"",
            }

print('hi! here\'s my quick stats:')
for k, val in my_info.iteritems():
    print('My {} is {}.'.format(k, val)) 