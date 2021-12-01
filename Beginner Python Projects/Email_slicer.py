#User Input
name = input("Enter you email id ")
#Splitting
splitting = name.split("@")
#Indexing
user = splitting[0]
domain = splitting[1]
#Output
print(f"Your user name is {user} and your domain is {domain}")