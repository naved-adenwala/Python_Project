#we are creating story using random module

# Module
import random
#Creating Story
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Naved', 'Rashid','Umair', 'Raha', 'Nida']
residence = ['Delhi','India', 'Mumbai', 'Dubai', 'USA']
went = ['cinema', 'university','seminar', 'school', 'Park']
happened = ['made a lot of friends','Learning Python', 'found a secret key', 'solved a Problem', 'Help Poor people']
#Displaying Randomly
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
