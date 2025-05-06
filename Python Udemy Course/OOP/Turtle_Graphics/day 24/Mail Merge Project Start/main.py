#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"C:\Users\PC\Python Udemy Course\OOP\Turtle_Graphics\day 24\Mail Merge Project Start\Input\Names\invited_names.txt" ,"r") as name_list:
    for names in name_list:
        names = names.strip()
        with open(r"C:\Users\PC\Python Udemy Course\OOP\Turtle_Graphics\day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt" ,"r") as text:
            switch = text.read()
            switch = switch.replace("[name]", f"{names}")
            with open(rf"C:\Users\PC\Python Udemy Course\OOP\Turtle_Graphics\day 24\Mail Merge Project Start\Output\letter_to_{names}.txt", "w") as letter_to:
                letter_to.write(switch)