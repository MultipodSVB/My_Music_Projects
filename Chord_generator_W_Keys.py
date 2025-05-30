# My chord generator, need to add more types And some scales 

# Version 2 - CURRENTLY WORKS, has a loop to ask for another chord
# VERSION 3 added keys and input choices 

#         0    1    2   3    4     5   6     7    8    9     10   11   --- Index
notes = ["A", "A#","B","C", "C#", "D","D#", "E", "F", "F#", "G", "G#"]

# each index mapped to the musical notes above to create the chord
chords = {
	"major" : [0, 4, 7], # root, major third, perfect fifth
	"minor" : [0, 3, 7], # root, minor third, perfect fifth
	"major7" : [0, 4, 7, 10], #root, major third, perfect fifth, major seventh
	"minor7" : [0, 3, 7, 10] #root, minor third, perfect fifth, minor seventh
	}

# index mapped to each note to create a scale
modes = {
	"ionian": [0, 2, 4, 5, 7, 9, 11],    # Major
	"dorian": [0, 2, 3, 5, 7, 9, 10],
	"phrygian": [0, 1, 3, 5, 7, 8, 10],
	"lydian": [0, 2, 4, 6, 7, 9, 11],
	"mixolydian": [0, 2, 4, 5, 7, 9, 10],
	"aeolian": [0, 2, 3, 5, 7, 8, 10],                  # Minor
	"locrian": [0, 1, 3, 5, 6, 8, 10],
 
}

def add_notes(root, intervals):
    #check if root selected is in the "notes" list
    if root in notes:
        #finds the index of the note selected
        index = notes.index(root)
        # moves through the indexes listed in chosen 'chord_type' and loops back around using %len
        return [notes[(index + step) % len(notes)] for step in intervals] 
    


while True:
    #select a note in the notes list
	root = input("Select a root note: > ").lower()
	note_choice = input("Do you want a chord or a scale? Type chord or scale: ").lower()

	# will check if input matches choices given
	if note_choice == "chord":
		chord_choice = input("Choose chord type: major, minor, major7, minor7: > ").lower()
		if chord_choice in chords:
			print(add_notes(root, chords[chord_choice]))
			print("choose another note!")
		else:
			print("Invalid choice!")

	elif note_choice == "scale":
		scale_choice = input("Choose a scale/mode: ionian (Major), dorian. phrygian, lydian, mixolydian, aeolian (Minor), locrian: > ")
		print(add_notes(root, modes[scale_choice]))
		print("choose another note!")
	else:
		print("INVALID CHOICE")
    
