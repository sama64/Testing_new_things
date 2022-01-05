import random

class create_password:
    def __init__(self, length=12):
        self.__password = self.__new_password(length)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if new_password > 0:
            self.__password = new_password
        else:
            raise ValueError("Value must be an integer major than 0")

    def __new_password(self, length):
        upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z']
        characters = ['@', '_', '#', '$', '¡', '!', '¿', '?']
        holder_password = ''
        for i in range(0, length):
            pick1 = upper_letters[random.randint(0, 25)]
            pick2 = lower_letters[random.randint(0, 25)]
            pick3 = characters[random.randint(0, 7)]
            pick4 = random.randint(0, 9)
            foo = [pick1, pick2, pick3, pick4]
            holder_password = holder_password + str(random.choice(foo))

        return holder_password


def run():
    user_length = int(input('How long do you want your password to be?:  '))
    password = create_password(user_length)

    print(f'Your new password is :   {password.password}')

if __name__ == '__main__':
    run()