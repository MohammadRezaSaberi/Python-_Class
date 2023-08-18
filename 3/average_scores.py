name = input('please enter your name: ')

math_score = float(input('Math Score: '))
physic_score = float(input('Physic Score: '))
algebra_score = float(input('Algebra Score: '))
chemistry_score = float(input('Chemistry Score: '))

sum_scores = math_score + physic_score + algebra_score + chemistry_score
average = sum_scores / 4

print(average)
