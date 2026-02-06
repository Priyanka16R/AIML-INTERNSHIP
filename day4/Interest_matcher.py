friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(" interests they both share",friend_a & friend_b)
print("list of all unique interests between friend_a and friend_b",friend_a|friend_b)
print("interests that friend_a has but friend_b does not",friend_a-friend_b)