def get_gender(gender='unknown'):
    if gender.lower() == 'm':
        print("Gender Male")
    elif gender.lower() == 'f':
        print("Gender Female")
    else:
        print("Gender unknown")


get_gender('M')
get_gender('f')
get_gender()
