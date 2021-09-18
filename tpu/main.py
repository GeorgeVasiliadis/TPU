VALID_TABS = "a a# b c c# d d# e f f# g g#".split()

FLATMAP = {
    "db":"c#",
    "eb":"d#",
    "gb":"f#",
    "ab":"g#",
    "bb":"a#"
}

# Not-a-Chord conventions
NAC = -1
NAC_SYMBOL = "X"

def transpose_chord(chord, offset=0):
    
    try:
        i = VALID_TABS.index(chord)
        return VALID_TABS[ (i+offset) % len(VALID_TABS) ]
        
    except ValueError:
        print(f"\"{ chord }\" is not a recognized chord!")
        return NAC_SYMBOL
    
def pretty_print_chord(chord):
    return chord[0].upper() + chord[1:]

def extract_minor(chord):
    if chord[-1] == 'm':
        return True, chord[:-1]
    else: return False, chord

def transpose(tabs, offset): 
    tabs = [x.lower() for x in tabs]
    minors = []
    clear = []
    for t in tabs:
        m, x = extract_minor(t)
        minors.append(m)
        clear.append(x)
    tabs = [FLATMAP[x] if x in FLATMAP.keys() else x for x in clear]
    transposed = [transpose_chord(x, offset) for x in tabs]
    scale_corrected = []
    for i in range(len(tabs)):
        x = transposed[i]
        scale_corrected.append(x + "m" if minors[i] else x)
    print([pretty_print_chord(x) for x in scale_corrected])
