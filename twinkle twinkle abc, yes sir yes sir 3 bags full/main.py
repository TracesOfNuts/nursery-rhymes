with open("abc-lyrics.txt", "r") as f:
    abc = f.readlines()

with open("baa-baa-black-sheep-lyrics.txt", "r") as f:
    baa = f.readlines()

with open("twinkle-twinkle-little-star-lyrics.txt", "r") as f:
    twinkle = f.readlines()

possible_combinations = [
    (abc, baa, twinkle),
    (abc, twinkle, baa),
    (baa, abc, twinkle),
    (baa, twinkle, abc),
    (twinkle, abc, baa),
    (twinkle, baa, abc),
]

for c_i, combination in enumerate(possible_combinations):
    print(f"Song {c_i+1}:")
    for s_i, song in enumerate(combination):
        print(song[s_i], sep="", end="")
    for s_i, song in enumerate(combination):
        print(song[s_i+3], sep="", end="")
    print("\n")