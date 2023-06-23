# Find the max of max distance between the same words

string = "Harsh is currently in India. Harsh is working in IT company. Harsh temp is"

map = dict()

for i, word in enumerate(string.split(" ")):
    if map.__contains__(word):
        map[word][1] = i - map.get(word)[0] - 1
        continue
    map[word] = [i, 0]

op = ""
maxx = 0

for k, v in map.items():
    if v[1] > maxx:
        maxx = v[1]
        op = k

print(op)
