#try: Somthink that might cause an exception (might or might not)
#except: Do this if there was an exception(if code fails do this)
#else: Do this if there was no exceptions(if nothig fails do this)
#finally: Do this no matter what happens(alweys is True)
#rais: Raises an error even if it doesn't exsist(makes up an error)

# fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
# try:
#     make_pie(4) 
# except IndexError:
#     print("Fruit pie")

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):

#     total_likes = 0
#     try:
#         for post in posts:
#             total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#     else:
#         return total_likes


# count_likes(facebook_posts)