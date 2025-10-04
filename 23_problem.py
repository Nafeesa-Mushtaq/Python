post = input("Enter your post: ")

if("Nafeesa" in post):
    print("This post is talking about Nafeesa")
else:
    print("This post is not talking about Nafeesa")


# NOTE that when i enter nafeesa in lower case it will not recognize it so in-order to solve this we will use this 
# this will convert all the text to lower case so that it can give the correct result

if("Nafeesa".lower() in post.lower()):
    print("This post is talking about Nafeesa")
else:
    print("This post is not talking about Nafeesa")
