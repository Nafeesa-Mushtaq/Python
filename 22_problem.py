p1 = "Subscribe this"
p2 = "Make money"
p3 = "Click this"
p4 = "Buy now"

message = input("Enter your comment: ")

# NOTE THAT PYTHON IS A CASE SENSITIVE LANGUAGE -- CAPITAL A != small a

if((message in p1) and (message in p2) and (message in p3) and (message in p4)):
    print("This is scam")
else:
    print("This comment is ok : ",message)