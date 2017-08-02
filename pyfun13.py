def pStudents(students):
    for student in students:
        print(student['first_name']+' '+student['last_name'])


def schoolFunc(d):
    for group_name, group in d.items():
        print(group_name)
        n = 1
        for g in group:
            print(str(n) + '  ' + g['first_name'] + ' ' + g['last_name'])
            n += 1




students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print("students: \n\n")
pStudents(students)
print("AllUsers:\n")
print schoolFunc(users)