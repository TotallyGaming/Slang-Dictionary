# The dictionary itself
slang_dict = {
    "SIGMA": "Either a lone ranger or something cool",
    "LOL": "Laughing Out Loud (something that is funny)",
    "GYATT": "Somebody's butt, usually used to point out that it's big",
    "CRINGE": "Something that is embarrassing or awkward",
    "CAP": "Used to state that something is a lie",
    "CAPPING": "Used to state that someone is lying (see: CAP)",
    "YAPPING": "Talking too much or saying what seems like nonsense to the listener",
    "YAPANESE": "Used with speaking to mean yapping (see: YAPPING)",
    "YAPPUCINO": "Used with  I didn't order a  to mean  You are yapping  (see: YAPPING)",
    "NGL": "Not Going to Lie (I am being honest)"
}

# Get input
word = input("Type slang word to find its meaning:  (in capital letters)")
found = False

# Search the dictionary
for slang in slang_dict:
    # If it matches a key with the input,
    if word in slang and not found:
        # Print the value
        print(slang_dict[slang])
        found = True

# Pretty self-explainatory
if not found:
    print("That word isn't in the dictionary.")
else:
    print("Is that what you were looking for?")
    
