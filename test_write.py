# test_write.py - try this separately
stats = {'words': 45, 'characters': 267, 'sentences': 4}

with open("test.txt", "w") as f:
    f.write("Words: ")
    f.write(str(stats['words']))
    f.write("\n")  # What happens without this?
    f.write("Done")

# Then open test.txt and see what it looks like