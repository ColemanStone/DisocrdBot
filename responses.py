import random

def handle_responses(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Test Success'
    
    if p_message == 'roll':
        return str(random.randint(1 , 6))
    
    if p_message == '!help':
        return 'This can work as a help message'

    return 'Try again'