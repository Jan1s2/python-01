from structures import charFrequency
INPUT = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech." 
print("Četnost výskytu písmen:")
print("-----------------------")
print(*charFrequency(INPUT), sep='\n')
