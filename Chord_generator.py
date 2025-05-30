# My chord generator, need to add more types And some scales 

# Version 2 - CURRENTLY WORKS, has a loop to ask for another chord

notes = ["A", "A#","B","C", "C#", "D","D#", "E", "F", "F#", "G", "G#"]


def major_chord(root):
	if root in notes:
		index = notes.index(root)
		
		major_third = notes[(index + 4) % len(notes)] # add 4 whole steps after root (major third)
		
		fifth = notes[(index + 7) % len(notes)] # perfect fifth
		
		return[root, major_third, fifth]
		
	else:
		return "invalid root note"
  
def minor_chord(root):
	if root in notes:
		index = notes.index(root)
		
		minor_third = notes[(index + 3) % len(notes)] # add 3 steps after root (minor third)
		
		fifth = notes[(index + 7) % len(notes)] # perfect fifth 
		
		return[root, minor_third, fifth]
		
	else:
		return "invalid root note"

def major_seventh_chord(root):
	if root in notes:
		index = notes.index(root)
		
		major_third = notes[(index + 4) % len(notes)] # add 4 whole steps after root (major third)
		
		fifth = notes[(index + 7) % len(notes)]
		
		seventh = notes[(index + 10) % len(notes)]
		
		return[root, major_third, fifth, seventh]
		
	else:
		return "invalid root note"
  
def minor_seventh_chord(root):
	if root in notes:
		index = notes.index(root)
		
		minor_third = notes[(index + 3) % len(notes)] # add 3 steps after root (minor third)
		
		fifth = notes[(index + 7) % len(notes)] # perfect fifth 
		
		seventh = notes[(index + 10) % len(notes)] # Seventh
		
		return[root, minor_third, fifth, seventh]
		
	else:
		return "invalid root note"



chord_type = {
	"major" : major_chord,
	"minor" : minor_chord,
	"major7" : major_seventh_chord,
	"minor7" : minor_seventh_chord
	}


 
while True:
	root = input("Select a root note: > ").upper() # Doesn't matter if capslock is on or off
	chord_choice = input("Choose chord type: Major, minor, Major7, minor7: > ").lower() # same as above
	print("choose another note: > ")
 
	if chord_choice in chord_type:
		print(chord_type[chord_choice](root))
	else:
		print("INVALID CHOICE")
  

    
