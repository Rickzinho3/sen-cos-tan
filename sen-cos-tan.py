# seno, cosseno e tangente de um ângulo qualquer

import math

ângulo = float(input('Digite um ângulo: '))

#seno 
sen = math.sin(math.radians(ângulo))
print('O seno de {} é > {:.2f}'.format(ângulo, sen))

#cosseno
cos = math.cos(math.radians(ângulo))
print('O cosseno de {} é > {:.2f}'.format(ângulo, cos))

#tangente
tan = math.tan(math.radians(ângulo))
print('A tangente de {} é > {:.2f}'.format(ângulo, tan))
