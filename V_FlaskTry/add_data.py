from models.jobs import Jobs
from models.user import User
from models import db_session
db_session.global_init("db/users_and_jobs.db")

session = db_session.create_session()

user = User()
user.name = "Scott"
user.surname = "Ridley"
user.age = 21
user.position = 'capitan'
user.speciality = 'research engineer'
user.address = 'module_1'
user.email = "scott_chief@mars.org"
session.add(user)
session.commit()

user = User()
user.name = "fvsdfd"
user.surname = "dsafsdfgds"
user.age = 123
user.position = 'engineer'
user.speciality = 'research engineer'
user.address = 'module_2'
user.email = "fvsdfd@mars.org"
session.add(user)
session.commit()

user = User()
user.name = "Weir"
user.surname = "Andy"
user.age = 28
user.position = 'cook'
user.speciality = 'cook'
user.address = 'module_kitchen'
user.email = "weir_andy@mars.org"
session.add(user)
session.commit()

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2 3'
job.is_finished = False
session.add(job)
session.commit()

job = Jobs()
job.team_leader = 3
job.job = 'приготовить еду'
job.work_size = 10
job.collaborators = ''
job.is_finished = False
session.add(job)
session.commit()
