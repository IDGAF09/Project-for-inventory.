import json
file_names = 'untitled-1.json'
with open(file_names,'r') as file:
    data = json.load(file)

book_allies = { #every book and their acronym to make it easy
    'M_E': "Mastery 'English'",
    '48_E': "The 48 Laws of Power 'English'",
    '50L_E': "The 50th Law 'English'",
    'S_E': "The Art of Sedaction 'English'",
    'HN_E': "The Laws of Human Nature 'English'",
    'M_F': "Mastery 'Francaise'",
    '48_F': "The 48 Laws of Power 'Francaise'",
    'S_F': "The Art of Seduction 'Francaise'",
    '365_F': "The Daily Laws 365 'Francaise'",
    'HN_F': "The Laws of Human Nature 'Francaise'",
    'TIM_E': "This is Marketing 'English'",
    'OT_F': "The One Thing 'Francaise'",
    'DW_F': "Deep Work 'Francaise'",
    'EC_F': "L'effet cumulé 'Francaise'",
    'ZERO_F': "De zéro à un 'Francaise'",
    'rien_F': "Un rien peut tout changer 'Francaise'",
    'MND_E': "The Millionaire Next Door 'English'",
    'SO_E': "Stop Overthinking 'English'",
    'LS_E': "Lean startup 'Francaise'",
    'LDD_F': "Le livre des décisions 'Francaise'",
    'EGO_F': "L'Ego est l'Ennemi 'Francaise'",
    'CLPP_F': "Cultivez la pensée positive 'Francaise'",
    'REDR_F': "Réfléchissez et devenez riche 'Francaise'",
    'RPUV_F': "12 Règles Pour Une Vie 'Francaise'"
}
the_types_of_commends = {#evrey commend und the books Which contains them
      'B_C_E': [
        'Mastery "English"',
        'The 48 Laws of Power "English"',
        'The 50th Law "English"',
        'The Art of Sedaction "English"',
        'The Laws of Human Nature "Englisch"'
    ],
    'B_C_F': [
        'Mastery "Francaise"',
        'The 48 Laws of Power "Francaise"',
        'The Art of Seduction "Francaise"',
        'The Daily Laws 365 "Francaise"',
        'The Laws of Human Nature "Francaise"'
    ],
    'B_C_F1':[
         "Un rien peut tout changer 'Francaise'"
         "De zéro à un 'Francaise'"
         "L'effet cumulé 'Francaise'"
         "Deep Work 'Francaise'"
         "The One Thing 'Francaise'"
         
    ],
    'B_C_F2':[
        "The One Thing 'Francaise'"
        "Deep Work 'Francaise'"
        "L'effet cumulé 'Francaise'"
        "Un rien peut tout changer 'Francaise'"
        "Lean startup 'Francaise'"
    ],
    'S_C_F': [
        'Mastery "Francaise"',
        'The 48 Laws of Power "Francaise"',
        'The Laws of Human Nature "Francaise"'
    ],
    'S_C_F1':[
         "The One Thing 'Francaise'"
         "Deep Work 'Francaise'"
         "L'effet cumulé 'Francaise'"
    ]
} #which type of commend, Because I sell always more than one book for each person
print('hallo user')
def sum_or_min_or_just_check_out():
    the_ansewr = input('what do you want:\nto check the contity:=\nif you buy books:+\nif you sell:-')# = to know the quantity -to mines from the quantity +to add
    if the_ansewr == '=': #show the data
        print(data)
    if the_ansewr == '-':
        which_commend = input('which commend you sale\n"B_C_E"\n"B_C_F"\nor"B_C_F1"\nor"B_C_F2"\n"S_C_F"\nor"S_C_F1"\nor else:').upper()#which commend we had sale
        if which_commend in the_types_of_commends:
            quantity = int(input('how many commend of those:'))
            if quantity == 0:
                print("Please enter a valid quantity greater than zero.")
                return
            for book in the_types_of_commends[which_commend]:

                if  data[book] >= quantity:
                        data[book] -= quantity #to minus from evrey book the quantity
                        print(data[book])

                else:
                        print(f"you don't have enough copies of {book}") #to know wich book we don't have it a lot

        if which_commend not in the_types_of_commends:
            quantity_of_new_commend = int(input('how many books in thise commende:')) #if we had sale a irregular commend,we will gave the opertunites to creat a flexible one
            i = 0
            while i < quantity_of_new_commend:
                books = input('which books sales:').upper() #to ask about every book in thise commend
                i += 1
                if books in book_allies:  
                    if data[books] >= 1: 
                        data[books] -= 1
                        print(f'It sells {book_allies[books]} and??:')
                    else:
                        print(f'{book_allies[books]} is out of stock now.')
                else:
                     print("We don't have that book now, but we will provide it soon.")
    if the_ansewr == '+':
        which_type = input('retur or bying:').lower()
        if which_type == 'bying':
            for book in data:
                quantity = int(input(f'how many copies of this one dii you by{book}'))
                data[book] += quantity
        if which_type == 'reteur':
            which_commend = input('which commend you sale\n"B_C_E"\n"B_C_F"\nor"B_C_F1"\nor"B_C_F2"\n"S_C_F"\nor"S_C_F1"\nor else:').upper() #to know which commend back
            if which_commend in the_types_of_commends:
                quantity = int(input('how many commend of those:'))
                if quantity == 0:
                    print("Please enter a valid quantity greater than zero.")
                    return
            for book in the_types_of_commends[which_commend]:
                data[book] += quantity
            if which_commend not in the_types_of_commends:
                quantity_of_new_commend = int(input('how many books in thise commende:'))
                i = 0
                while i < quantity_of_new_commend:
                    books = input('which books sales:').upper()
                    i += 1
                if books in book_allies: 
                    data[books] += 1
                    
                    print(f"It's back {book_allies[books]} and??:")

        with open(file_names,'w') as file:
                         json.dump(data,file,indent= 4)
sum_or_min_or_just_check_out()

        






            
        
