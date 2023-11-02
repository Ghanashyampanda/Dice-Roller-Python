import random
def parse_input(input_string):
    if input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)
    else:
        print("please enter a number from 1 to 6")
        raise SystemExit(1)

num_dice_input=input("How many dice you want to roll,[1-6]")
num_dice=parse_input(num_dice_input)


def roll_dice(num_dice):
    roll_results=[]
    for _ in range(num_dice):
        roll=random.randint(1,6)
        roll_results.append(roll)
    return roll_results


Dice_art={1:(
    " _________ ",
    "|         |",
    "|    0    |",
    "|         |",
    " _________ ",
    ),
    2:(
    " _________ ",
    "| 0       |",
    "|         |",
    "|       0 |",
    " _________ ",
       ),
    3:(
       " _________ ",
       "| 0       |",
       "|    0    |",
       "|       0 |",
       " _________ ",
       ),
    4:(
       " _________ ",
       "| 0     0 |",
       "|         |",
       "| 0     0 |",
       " _________ ",
       ),
    5:(
       " _________ ",
       "| 0     0 |",
       "|    0    |",
       "| 0     0 |",
       " _________ ",
       ),
    6:(
       " _________ ",
       "| 0     0 |",
       "| 0     0 |",
       "| 0     0 |",
       " _________ ",
       ),
    }
die_height=len(Dice_art[1])
die_width=len(Dice_art[1][0])
die_face_separator=" "

def generate_dice_face_diagram(dice_values):
    dice_faces=[]
    for value in dice_values:
        dice_faces.append(Dice_art[value])
    dice_face_rows=[]
    for row_idx in range(die_height):
        row_components=[]
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string=die_face_separator.join(row_components)
        dice_face_rows.append(row_string)
    width=len(dice_face_rows[0])
    diagram_header="RESULTS".center(width,"~")
    
    dice_faces_diagram="\n".join([diagram_header]+dice_face_rows)
    return dice_faces_diagram


def _get_dice_faces(dice_valus):
    dice_faces=[]
    for value in dice_valus:
        dice_faces.append(Dice_art[value])
    return dice_faces


roll_results=roll_dice(num_dice)

dice_faces_diagram=generate_dice_face_diagram(roll_results)
print(f"\n{dice_faces_diagram}")
#print(roll_results)