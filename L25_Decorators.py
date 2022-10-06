def cough_dec(func):
    def func_wrapper():
        # code before function
        print('*cough*')
        func()
        # ocde after function
        print('*cough*')
    return func_wrapper


@cough_dec
def question():
    print('Can you give me a discount on that?')


question()
# *cough*
# Can you give me a discount on that?
# *cough*


@cough_dec
def answer():
    print('it is only 50p you cheapskate')
# *cough*
# Can you give me a discount on that?
# *cough*
