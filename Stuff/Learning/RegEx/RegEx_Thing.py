import re

play = True

while play:

    user_input = input()

    database = []

    while user_input != 'make migrations':

        # Name validation
        name_pattern = re.findall(r'(?<=name is )([A-Z][a-z]+\s[A-Z][a-z]+)', user_input)
        if name_pattern:
            name_actual = name_pattern[0]
        else:
            name_actual = 'Let the bodies hit the FLOOOOOOOOOOOOR!!!'

        # Age validation
        age_pattern = re.findall(r'(\s)([1-9]\d{1})(\s)(?=years)', user_input)
        if age_pattern:
            retrieved_list = age_pattern[0]
            age_actual = retrieved_list[1]
        else:
            age_actual = 'Пак ще се срещнем.....след 10 годинии!'

        # Birth date validation
        bdate_pattern = re.findall(r'(?<= on )(\d{2}-\d{2}-\d{4}\.)', user_input)
        if bdate_pattern:
            bdate_actual = bdate_pattern[0]
        else:
            bdate_pattern = '6th of June 1944, allies are turning the waaaar!!'

        # If all data is present add to database
        if name_actual != 'Let the bodies hit the FLOOOOOOOOOOOOR!!!' \
                and age_actual != 'Пак ще се срещнем.....след 10 годинии!' \
                and bdate_actual != '6th of June 1944, allies are turning the waaaar!!':
            information = [name_actual, age_actual, bdate_actual]
            database.append(information)
            # print(information)

        user_input = input()

    # When user_input == 'make migrations'
    else:
        if not database:
            print("DB is empty")
        else:
            # print(database)
            for dataset in database:
                print(f"Name of the person: {dataset[0]}.")
                print(f"Age of the person: {dataset[1]}.")
                print(f"Birthdate of the person: {dataset[2]}")

        # Reset
        database = []

        user_input = input()

