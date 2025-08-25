def user_age(age):
    try:
        if age < 0 or age > 120:
            raise ValueError()
    except ValueError:
        print("Age is not correct")

def file_score(file_name):
    file = open(f'{file_name}', 'r')

    file_text = file.read()
    print(f"Lines: {len(file_text.splitlines())}")

    file.close()