import keyword
from random import randint
from string import digits
from faker import Faker



def randRatio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')

def makeRecipe():
    return {
        'id': fake.random_number(digits=6, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=16),
        'preparationTime': fake.random_number(digits=2, fix_len=True),
        'preparationTimeUnit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servingsUnit': 'Porções',
        'preparationSteps': fake.text(3000),
        'createdAt': fake.date_time(),
        'author': {
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
        },
        'category':{
            'name': fake.word()
        },
        'cover': {
            'url': 'https://source.unsplash.com/random/1280x720',
        },
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(makeRecipe())