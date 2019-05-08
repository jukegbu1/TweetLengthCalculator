# Create a variable called tweet and put "Hear Me Code class was so much fun today!"
tweet = "Hear Me Code class was so much fun today!ar Me Code class was so much fun today!"

# Measure the length of tweet
print len(tweet)

# Was that tweet more than 140 characters?
# If so, tell the user it was too long!
# Was that tweet 140 or fewer characters?
# If so, tell the user how witty they are!
maxtweet = 140

if tweet < maxtweet:
    print "You are so witty"
else:
    print "That was way to long!"

# Adjust program to say how many characters remaining to use or how many you need to trim by to meet 140 character limit

print """That tweet is {0} character. You have {1} characters left""".format(len(tweet), 140 - len(tweet))