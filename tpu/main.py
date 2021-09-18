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
    """Takes a chord as a string along with a semitone offset as an integer
    (positive or negative) and returns the well-formatted, transposed chord.

    It is possible that the given chord is invalid (aka not well-formatted). In
    such case, NAC symbol is being returned.
    """

    try:
        i = VALID_TABS.index(chord)
        return VALID_TABS[ (i+offset) % len(VALID_TABS) ]

    except ValueError:
        print(f"\"{ chord }\" is not a recognized chord!")
        return NAC_SYMBOL

def pretty_print_chord(chord):
    return chord[0].upper() + chord[1:]

def extract_minor(chord):
    """Checks whether the given cord is specified as "minor". If so, it pops out
    the specifier and returns a boolean indicator along with the clean chord.

    E.g.
    ----
        Am  --> True,  A
        B#  --> False, B#
        F#m --> True, F#
    """
    if chord[-1] == 'm':
        return True, chord[:-1]
    else: return False, chord

def transpose(tabs, offset):
    """Takes a list of chords (aka tabs) and returns the transposed version of it
    by N semitones, as defined by given offset.
    """

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
        
    return [pretty_print_chord(x) for x in scale_corrected]
