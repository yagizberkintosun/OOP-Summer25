animals = [
    {
        'name': 'Lion',
        'group': 'Mammal',
        'number_of_legs': '4',
        'skills': ['being strong','great at hunting']
    },
    {
        'name': 'Spider',
        'group': 'Aranchid',
        'number_of_legs': '8',
        'skills': ['Skilled at spinning webs','quick reflexes']
    },
    {
        'name': 'Cheetah',
        'group': 'Mammal',
        'number_of_legs': '4',
        'skills': ['Fastest land animal','great at acceleration']
    },
    {
        'name': 'Eagle',
        'group': 'Bird',
        'number_of_legs': '2',
        'skills': ['Flying','exceptional vision']
    },
    {
        'name': 'Octopus',
        'group': 'Mollusk',
        'number_of_legs': '8',
        'skills': ['High intelligence','camouflage abilities']
    }
]

for animal in animals:
    print(f"{animal['name']} belongs to group of {animal['group']} and has {animal['number_of_legs']} legs.")
    print(f"Skills: {', '.join(animal['skills'])}")
