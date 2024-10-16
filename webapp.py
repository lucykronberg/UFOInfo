numbers = [ orb, triangle,other, fireball, disc, egg, cigar, changing, rectangle, diamond]
counts = {}
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
    counts[num] = 1
    