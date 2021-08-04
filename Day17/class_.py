# class user :
# # to pass anything youdonot want in your code
#     pass
 #pascal way
class User :
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following +=1
           
user1 = User("001","miku")
user2 = User("002","pott")
print(user1.user_id)
print(user1.username)  #note that user_name and username are different
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

