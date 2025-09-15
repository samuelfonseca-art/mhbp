import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_message(split_message)
    if response == "":
        response = unknown()
    return {"response": response}

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):

    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    
    percentage = float(message_certainty) / float(len(recognized_words)) if recognized_words else 0
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_message(message):

    highest_prob = {}

    def response(bot_response, list_of_words,  single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Definición de respuestas posibles con URL de gifs
    response(
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        ['hola', 'saludos', 'buenas'],
        single_response=True
    )
    response(
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        ['hola', 'saludos', 'buenas'],
        single_response=True
    )
    response(
    "La rosa necesita 500 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (1800-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
    ['rosa'],
    single_response=True
    )

    response(
        "La albahaca necesita 300 ml de agua diarios, 6 horas de luz al día, 20 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['albahaca'],
        single_response=True
    )

    response(
        "El cactus necesita 100 ml de agua diarios, 5 horas de luz al día, 10 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima árido y seco, y debe plantarse a una distancia de 0.4 m.",
        ['cactus'],
        single_response=True
    )

    response(
        "La papa necesita 800 ml de agua diarios, 6 horas de luz al día, 70 g de composta al mes, se adapta a pisos térmicos templados (2000-3000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.4 m.",
        ['papa'],
        single_response=True
    )

    response(
        "El maíz necesita 600 ml de agua diarios, 8 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.5 m.",
        ['maiz', 'maíz'],
        single_response=True
    )

    response(
        "La caña de azúcar necesita 900 ml de agua diarios, 8 horas de luz al día, 80 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['caña de azucar', 'caña de azúcar','cana de azucar','cana','azucar','caña','azúcar'],
        single_response=True
    )

    response(
        "La yuca necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['yuca'],
        single_response=True
    )

    response(
        "El plátano necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 3.0 m.",
        ['platano', 'plátano'],
        single_response=True
    )

    response(
        "El café necesita 500 ml de agua diarios, 5 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (1200-1800 msnm), clima templado y húmedo, y debe plantarse a una distancia de 2.0 m.",
        ['cafe', 'café'],
        single_response=True
    )

    response(
        "El cacao necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 3.0 m.",
        ['cacao'],
        single_response=True
    )

    response(
        "El aguacate necesita 700 ml de agua diarios, 6 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos templados (1500-2500 msnm), clima templado y húmedo, y debe plantarse a una distancia de 5.0 m.",
        ['aguacate'],
        single_response=True
    )

    response(
        "El clavel necesita 400 ml de agua diarios, 7 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos templados (1800-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['clavel'],
        single_response=True
    )

    response(
        "El crisantemo necesita 450 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (1800-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.4 m.",
        ['crisantemo'],
        single_response=True
    )

    response(
        "La orquídea necesita 350 ml de agua diarios, 5 horas de luz al día, 30 g de composta al mes, se adapta a pisos térmicos templados (1200-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['orquidea', 'orquídea'],
        single_response=True
    )

    response(
        "La palma de aceite necesita 1000 ml de agua diarios, 8 horas de luz al día, 90 g de composta al mes, se adapta a pisos térmicos bajos (0-500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 9.0 m.",
        ['palma de aceite','palma','aceite'],
        single_response=True
    )

    response(
        "La cebada necesita 550 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (2000-3000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.25 m.",
        ['cebada'],
        single_response=True
    )

    response(
        "Gracias por tu visita. ¡Que tengas un gran día!",
        ['adios', 'gracias', 'nos vemos'],
        single_response=True
    )
    
    best_match = max(highest_prob, key=highest_prob.get)
    return best_match if highest_prob[best_match] > 0 else ""


def unknown():
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', 
                 'Por favor, intenta ser más específico.']
    return responses[random.randrange(len(responses))]
