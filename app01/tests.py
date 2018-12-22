from django.test import TestCase

# Create your tests here.

i = 1
flag = True
while flag:
    print(i*('*'))
    if i > 0 and i < 5:
        i += 1
    elif i >= 5:
        i -= 1
    else:
        break

