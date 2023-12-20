import random
feet_in_miles=5280
meters_in_kilometer=1000
beatles=["Jhone","Sachin","Mudannayaka","Viran","Rangajeewa"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)
