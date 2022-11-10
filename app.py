from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays a message to the user that changes based on their favorite dessert."""
    return f'Wow, {users_dessert} is my favorite dessert too!'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    """Funny make up story"""
    return f"Sally saw a {adjective} apple but it was actually a {noun}."

@app.route('/multiply/<number_1>/<number_2>')
def multiply_2numbers(number_1, number_2):
    """Displays a message to the user that multiplies two numbers and shows the result."""
    number_answer = int(number_1) * int(number_2)
    return f"{number_1} multipled by {number_2} equals {number_answer}."

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Repeats string n number of times"""
    new_string = ""
    if not word.isnumeric() and n.isdigit(): #Here it checks if the parameter word input is actually is letters and parameter n are in numbers
        n = int(n)
        for n in range(n):
            new_string += word + " "
        return f'{new_string}'
    else:
        return "Invalid input. Please try again by entering a word and a number!"

@app.route('/dicegame')
def dicegame():
    """Game that rolls a dice. If user rolls a 6 they win if not they lose"""
    roll = random.randint(1,6)
    if roll == 6:
        return "You rolled a 6. You win!"
    else:
        return f"You rolled a {roll}. You lost try again!"





# Helps Flask run server
if __name__ == '__main__':
    app.run(debug=True)