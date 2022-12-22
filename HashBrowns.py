import hashlib, time

# Get the input to hash
txt_to_hash = input("Input: ")

# Hash the input using the SHA-256 algorithm
hashed_input = hashlib.sha256(txt_to_hash.encode()).hexdigest()

# Save the hash to a .hs file
with open('C:/Users/coope/OneDrive/Desktop/Coding/1/Scripts/Order 66/HashBrowns/hash files/Hash-base.hs', 'w') as f:
    f.truncate(0)
    f.write(hashed_input + '\n')
    f.close()

# display hash
print(hashed_input)
time.sleep(4)
