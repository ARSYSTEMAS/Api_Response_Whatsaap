import re
import random
import WebScraping as  w
import conexionBD as Bd
import funcionsbot as fn


def get_response(user_input):

    funcions = fn.funcion_Bot(user_input.lower())
    if funcions:
        return funcions
    else:
        split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        response = check_all_messages(split_message)
        if response.startswith("http"):
            return w.extract_information(response,user_input.lower())
        else:

            return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):

    words = " ".join(user_message)
    message_certainty = 0
    has_required_word = True


    for word in user_message:
        if word in recognized_words:
            message_certainty +=1
        elif words in recognized_words:
            message_certainty += 1


    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_word = False
            break

    if has_required_word or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    global playgame
    highest_prob = {}
    wordsplay = " ".join(message)
    playgame = False
    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #########Respuestas del Bot automatica#############
    ciclo_for =  Bd.lst_question()

    for i in ciclo_for:
        question =  Bd.user_question(i)
        response_question =  Bd.response_bot(i)
        response(response_question[random.randrange(len(response_question))], question, single_response=True)
    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    global playgame
    response_question = Bd.response_bot(9)
    response = response_question[random.randrange(len(response_question))]
    return response

#while True:
#    print("Bot: " + get_response(input('You: ')))