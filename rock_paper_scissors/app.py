
import random

lst = [
    {
        'rock': {
            'rock': 2,
            'paper': 3,
            'scissors': 1
        }
    },
    {
        'paper': {
            'paper': 2,
            'scissors': 3,
            'rock': 1
        }
    },
    {
        'scissors': {
            'scissors': 2,
            'rock': 3,
            'paper': 1
        }
    }
]

ai_score = 0
user_score = 0
draw_score = 0

i = 0
while i < 101:
    ai_rndm = random.choice(lst)
    simulated_ai_input = list(ai_rndm.keys())[0]
    simulated_user_input = random.choice(['rock', 'paper', 'scissors'])

    ai_choice = list(ai_rndm.values())[0].get(simulated_ai_input)
    user_choice = list(ai_rndm.values())[0].get(simulated_user_input)

    if user_choice > ai_choice:
        user_score += 1
        # print(f"You win! [You: {user_score}, Robot: {ai_score}, draw: {draw_score}]")
    elif user_choice < ai_choice:
        ai_score += 1
        # print(f"You lose! [You: {user_score}, Robot: {ai_score}, draw: {draw_score}]")
    else:
        draw_score += 1
        # print(f"It's a draw. [You: {user_score}, Robot: {ai_score}, draw: {draw_score}]")
    i += 1

print(f"Final score:\n[You: {user_score}, Robot: {ai_score}, draw: {draw_score}]")
