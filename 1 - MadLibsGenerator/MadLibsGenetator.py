from random import randint 
import copy

story = (
    'My family and I are going camping near a {} {} this summer. ' +
    'Camping is {} because you get to {} and {} outside. ' +
    'When we {} to the campground, we set up our {}, where we will {} at night.  ' +
    'We like to go {} in the {}, hoping to {} some {} fish for dinner. ' +
    'we also go {} in the {} {},hoping to spot wildlife like {} or {}. ' +
    'My favorite part about camping is {} {} over the campfire. '
)

word_dict = {
    'adjective':['amazing','awesome','bad','curved','nice'], 
    'noun':['charger','calculator','water','bottle','sandal','pen','bed','tree'], 
    'verb':['discover','buy','cheat','play','kill'], 
    'verb_ing':['cooking','fishing','sleeping','going','fucking'], 
    'plrl_noun':['clothes','screws','twigs','stones','magazines'],
    'place':['London','Paris','Zarzis','forest','skyland'],
    'plrl_noun_animals':['Donkey','Rabbit','Cat','Elephant','Duck'],
    'plrl_noun_food':['pizza','spagitaa','couscous','apple','salad']
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)
    index = randint(0, cnt-1)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('verb', local_dict),
        get_word('verb', local_dict),
        get_word('verb', local_dict),
        get_word('plrl_noun', local_dict),
        get_word('verb', local_dict),
        get_word('verb_ing', local_dict),
        get_word('noun', local_dict),
        get_word('verb', local_dict),
        get_word('adjective', local_dict),
        get_word('verb_ing', local_dict),
        get_word('adjective', local_dict),
        get_word('place', local_dict),
        get_word('plrl_noun_animals', local_dict),
        get_word('plrl_noun_animals', local_dict),
        get_word('verb_ing', local_dict),
        get_word('plrl_noun_food', local_dict)
    )

print("Story1: ")
print(create_story())
print("Story2: ")
print(create_story())
print("Story3: ")
print(create_story())