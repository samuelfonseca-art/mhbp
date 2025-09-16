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
        "El sorgo dulce necesita 850 ml de agua diarios, 8 horas de luz al día, 60 g de composta al mes, se adapta a pisos cálidos (0-1000 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.4 m.",
        ['sorgo','dulce'],
        single_response=True
    )

    response(
        "La quinua necesita 600 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos fríos (2500-3800 msnm), clima frío y seco, y debe plantarse a una distancia de 0.3 m.",
        ['quinua'],
        single_response=True
    )

    response(
        "La alfalfa necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos templados (1000-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['alfalfa'],
        single_response=True
    )

    response(
        "El tarwi necesita 650 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos fríos (2000-3500 msnm), clima frío y húmedo, y debe plantarse a una distancia de 0.35 m.",
        ['tarwi', 'chocho'],
        single_response=True
    )

    response(
        "El frijol mungo necesita 800 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos templados (500-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['frijol mungo', 'mungo'],
        single_response=True
    )

    response(
        "El teff necesita 600 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos templados (1000-2000 msnm), clima templado y seco, y debe plantarse a una distancia de 0.2 m.",
        ['teff'],
        single_response=True
    )

    response(
        "El frijol azuki necesita 750 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos templados (500-1500 msnm), clima húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['frijol','azuki'],
        single_response=True
    )

    response(
        "El amaranto blanco necesita 700 ml de agua diarios, 8 horas de luz al día, 50 g de composta al mes, se adapta a pisos templados (1000-2500 msnm), clima seco y templado, y debe plantarse a una distancia de 0.3 m.",
        ['amaranto','blanco'],
        single_response=True
    )

    response(
        "El haba verde necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (1500-3000 msnm), clima fresco y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['haba','verde'],
        single_response=True
    )

    response(
        "El caupí necesita 800 ml de agua diarios, 7 horas de luz al día, 60 g de composta al mes, se adapta a pisos cálidos (0-1000 msnm), clima tropical seco, y debe plantarse a una distancia de 0.35 m.",
        ['caupí', 'caupi'],
        single_response=True
    )

    response(
        "El balú necesita 650 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos templados (500-2000 msnm), clima templado húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['balú','balu'],
        single_response=True
    )

    response(
        "El kenaf necesita 900 ml de agua diarios, 9 horas de luz al día, 70 g de composta al mes, se adapta a pisos cálidos (0-800 msnm), clima tropical húmedo, y debe plantarse a una distancia de 0.5 m.",
        ['kenaf'],
        single_response=True
    )

    response(
        "La moringa necesita 600 ml de agua diarios, 8 horas de luz al día, 40 g de composta al mes, se adapta a pisos cálidos (0-1200 msnm), clima seco y cálido, y debe plantarse a una distancia de 0.6 m.",
        ['moringa'],
        single_response=True
    )

    response(
        "El yacón necesita 900 ml de agua diarios, 7 horas de luz al día, 70 g de composta al mes, se adapta a pisos templados (1000-2500 msnm), clima templado húmedo, y debe plantarse a una distancia de 0.5 m.",
        ['yacón','yacon'],
        single_response=True
    )

    response(
        "El fonio necesita 550 ml de agua diarios, 7 horas de luz al día, 35 g de composta al mes, se adapta a pisos cálidos (0-1000 msnm), clima seco, y debe plantarse a una distancia de 0.2 m.",
        ['fonio'],
        single_response=True
    )

    response(
        "El sésamo negro necesita 650 ml de agua diarios, 8 horas de luz al día, 50 g de composta al mes, se adapta a pisos cálidos (0-1500 msnm), clima tropical seco, y debe plantarse a una distancia de 0.25 m.",
        ['sésamo','sesamo','negro'],
        single_response=True
    )

    response(
        "El guandú necesita 800 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos cálidos (0-1200 msnm), clima seco y cálido, y debe plantarse a una distancia de 0.4 m.",
        ['guandú', 'gandul'],
        single_response=True
    )

    response(
        "El amaranto tricolor necesita 700 ml de agua diarios, 8 horas de luz al día, 50 g de composta al mes, se adapta a pisos templados (1000-2500 msnm), clima templado y seco, y debe plantarse a una distancia de 0.3 m.",
        ['amaranto','tricolor'],
        single_response=True
    )

    response(
        "El lupino andino necesita 750 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos fríos (2000-3500 msnm), clima frío y húmedo, y debe plantarse a una distancia de 0.35 m.",
        ['lupino','andino'],
        single_response=True
    )

    response(
        "El frijol carita necesita 700 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos cálidos (0-1000 msnm), clima tropical seco, y debe plantarse a una distancia de 0.3 m.",
        ['frijol','carita'],
        single_response=True
    )

    response(
        "El centeno necesita 750 ml de agua diarios, 7 horas de luz al día, 60 g de composta al mes, se adapta a pisos fríos (1500-3000 msnm), clima templado frío, y debe plantarse a una distancia de 0.35 m.",
        ['centeno'],
        single_response=True
    )

    response(
        "El balú amazónico necesita 850 ml de agua diarios, 8 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['balú','balu','amazónico','amazonico'],
        single_response=True
    )

    response(
        "El sorgo forrajero necesita 900 ml de agua diarios, 9 horas de luz al día, 70 g de composta al mes, se adapta a pisos cálidos (0-800 msnm), clima tropical seco, y debe plantarse a una distancia de 0.5 m.",
        ['sorgo','forrajero'],
        single_response=True
    )

    response(
        "El mijo africano necesita 600 ml de agua diarios, 8 horas de luz al día, 40 g de composta al mes, se adapta a pisos cálidos (0-1200 msnm), clima árido, y debe plantarse a una distancia de 0.25 m.",
        ['mijo','africano'],
        single_response=True
    )

    response(
        "El arvejón necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos templados (1000-2000 msnm), clima templado y seco, y debe plantarse a una distancia de 0.3 m.",
        ['arvejón','arvejon'],
        single_response=True
    )

    response(
        "El balú serrano necesita 650 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos fríos (2000-3000 msnm), clima frío y seco, y debe plantarse a una distancia de 0.25 m.",
        ['balú','balu','serrano'],
        single_response=True
    )

    response(
        "El sorgo negro necesita 850 ml de agua diarios, 8 horas de luz al día, 60 g de composta al mes, se adapta a pisos cálidos (0-1000 msnm), clima árido, y debe plantarse a una distancia de 0.4 m.",
        ['sorgo','negro'],
        single_response=True
    )

    response(
        "El guisante de olor necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos templados (500-1500 msnm), clima templado húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['guisantede','olor'],
        single_response=True
    )

    response(
        "El balú rojo necesita 750 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y seco, y debe plantarse a una distancia de 0.35 m.",
        ['balú','balu','rojo'],
        single_response=True
    )

    response(
        "El alpiste necesita 650 ml de agua diarios, 7 horas de luz al día, 40 g de composta al mes, se adapta a pisos templados (500-2000 msnm), clima templado seco, y debe plantarse a una distancia de 0.2 m.",
        ['alpiste'],
        single_response=True
    )

    response(
        "El frijol blanco necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['frijol','blanco'],
        single_response=True
    )

    response(
        "El frijol negro necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['frijol','negro'],
        single_response=True
    )

    response(
        "El frijol rojo necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['frijol','rojo'],
        single_response=True
    )

    response(
        "El frijol pinto necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['frijol','pinto'],
        single_response=True
    )

    response(
        "El frijol canario necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['frijol','canario'],
        single_response=True
    )

    response(
        "El frijol garbanzo necesita 800 ml de agua diarios, 7 horas de luz al día, 60 g de composta al mes, se adapta a pisos templados (500-1500 msnm), clima seco y templado, y debe plantarse a una distancia de 0.35 m.",
        ['garbanzo'],
        single_response=True
    )

    response(
        "El trébol rojo necesita 600 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos templados (1000-2500 msnm), clima templado húmedo, y debe plantarse a una distancia de 0.2 m.",
        ['trébol rojo','trebol','trébol','rojo'],
        single_response=True
    )

    response(
        "El trébol persa necesita 600 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos templados (1000-2500 msnm), clima templado húmedo, y debe plantarse a una distancia de 0.2 m.",
        ['trébol persa','trébol','trebol','persa'],
        single_response=True
    )

    response(
        "El trébol subterráneo necesita 600 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos templados (1000-2500 msnm), clima templado húmedo, y debe plantarse a una distancia de 0.2 m.",
        ['trébol subterráneo','trebol','subterraneo','é','subterráneo'],
        single_response=True
    )

    response(
        "La veza común necesita 700 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos templados (1000-2000 msnm), clima templado fresco, y debe plantarse a una distancia de 0.3 m.",
        ['veza común','veza','comun','común'],
        single_response=True
    )

    response(
        "La veza vellosa necesita 700 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos templados (1000-2000 msnm), clima templado fresco, y debe plantarse a una distancia de 0.3 m.",
        ['veza vellosa','veza','vellosa'],
        single_response=True
    )

    response(
        "El haba morada necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (1500-3000 msnm), clima fresco y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['haba morada','haba','morada'],
        single_response=True
    )

    response(
        "El haba negra necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (1500-3000 msnm), clima fresco y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['haba negra','haba','negra'],
        single_response=True
    )

    response(
        "El haba peluda necesita 850 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos templados (1500-3000 msnm), clima fresco y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['haba peluda','haba','peluda'],
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
        "La zanahoria necesita 600 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (1200-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.2 m.",
        ['zanahoria'],
        single_response=True
    )

    response(
        "La lechuga necesita 500 ml de agua diarios, 5 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos bajos (500-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['lechuga'],
        single_response=True
    )

    response(
        "El tomate necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1800 msnm), clima cálido y templado, y debe plantarse a una distancia de 0.4 m.",
        ['tomate'],
        single_response=True
    )

    response(
        "La cebolla necesita 550 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (1000-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.25 m.",
        ['cebolla'],
        single_response=True
    )

    response(
        "El ajo necesita 400 ml de agua diarios, 6 horas de luz al día, 30 g de composta al mes, se adapta a pisos térmicos templados (1000-2500 msnm), clima templado y seco, y debe plantarse a una distancia de 0.2 m.",
        ['ajo'],
        single_response=True
    )

    response(
        "El pepino necesita 650 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.5 m.",
        ['pepino'],
        single_response=True
    )

    response(
        "La calabaza necesita 800 ml de agua diarios, 8 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['calabaza'],
        single_response=True
    )

    response(
        "La fresa necesita 600 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (1000-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['fresa'],
        single_response=True
    )

    response(
        "La sandía necesita 900 ml de agua diarios, 8 horas de luz al día, 70 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.5 m.",
        ['sandia', 'sandía'],
        single_response=True
    )

    response(
        "El melón necesita 850 ml de agua diarios, 8 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y seco, y debe plantarse a una distancia de 1.2 m.",
        ['melon', 'melón'],
        single_response=True
    )

    response(
        "La piña necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.6 m.",
        ['piña', 'pina'],
        single_response=True
    )

    response(
        "La espinaca necesita 500 ml de agua diarios, 5 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.2 m.",
        ['espinaca'],
        single_response=True
    )

    response(
        "El brócoli necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (1000-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.4 m.",
        ['brocoli', 'brócoli'],
        single_response=True
    )

    response(
        "La coliflor necesita 650 ml de agua diarios, 6 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (1000-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.4 m.",
        ['coliflor'],
        single_response=True
    )

    response(
        "El repollo necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (1000-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['repollo'],
        single_response=True
    )

    response(
        "El apio necesita 550 ml de agua diarios, 5 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['apio'],
        single_response=True
    )

    response(
        "El perejil necesita 400 ml de agua diarios, 5 horas de luz al día, 25 g de composta al mes, se adapta a pisos térmicos bajos (500-1500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.2 m.",
        ['perejil'],
        single_response=True
    )

    response(
        "El cilantro necesita 450 ml de agua diarios, 5 horas de luz al día, 30 g de composta al mes, se adapta a pisos térmicos bajos (500-1500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.2 m.",
        ['cilantro'],
        single_response=True
    )

    response(
        "El romero necesita 300 ml de agua diarios, 6 horas de luz al día, 20 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['romero'],
        single_response=True
    )

    response(
        "El tomillo necesita 300 ml de agua diarios, 6 horas de luz al día, 20 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.25 m.",
        ['tomillo'],
        single_response=True
    )

    response(
        "La menta necesita 500 ml de agua diarios, 5 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos bajos (0-1800 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['menta'],
        single_response=True
    )

    response(
        "La manzana necesita 750 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos templados (1500-2800 msnm), clima templado y fresco, y debe plantarse a una distancia de 3.0 m.",
        ['manzana', 'manzano'],
        single_response=True
    )

    response(
        "La pera necesita 700 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (1500-2800 msnm), clima templado y fresco, y debe plantarse a una distancia de 3.0 m.",
        ['pera', 'peral'],
        single_response=True
    )

    response(
        "El durazno necesita 750 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos templados (1200-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 4.0 m.",
        ['durazno', 'melocoton', 'melocotón'],
        single_response=True
    )

    response(
        "La ciruela necesita 700 ml de agua diarios, 6 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (1000-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 3.5 m.",
        ['ciruela'],
        single_response=True
    )

    response(
        "La uva necesita 600 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y seco, y debe plantarse a una distancia de 2.0 m.",
        ['uva', 'vid'],
        single_response=True
    )

    response(
        "La granada necesita 650 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 3.0 m.",
        ['granada'],
        single_response=True
    )

    response(
        "La guayaba necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 4.0 m.",
        ['guayaba'],
        single_response=True
    )

    response(
        "La mora necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (1200-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 2.0 m.",
        ['mora'],
        single_response=True
    )

    response(
        "El mango necesita 900 ml de agua diarios, 8 horas de luz al día, 80 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 5.0 m.",
        ['mango'],
        single_response=True
    )

    response(
        "El limón necesita 750 ml de agua diarios, 7 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1800 msnm), clima cálido y templado, y debe plantarse a una distancia de 4.0 m.",
        ['limon', 'limón'],
        single_response=True
    )

    response(
        "La naranja necesita 800 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-1800 msnm), clima cálido y templado, y debe plantarse a una distancia de 4.0 m.",
        ['naranja'],
        single_response=True
    )

    response(
        "La mandarina necesita 750 ml de agua diarios, 7 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1800 msnm), clima cálido y templado, y debe plantarse a una distancia de 3.5 m.",
        ['mandarina'],
        single_response=True
    )

    response(
        "La toronja necesita 800 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y templado, y debe plantarse a una distancia de 4.0 m.",
        ['toronja', 'pomelo'],
        single_response=True
    )

    response(
        "El kiwi necesita 650 ml de agua diarios, 6 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (1000-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 3.0 m.",
        ['kiwi'],
        single_response=True
    )

    response(
        "El higo necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y seco, y debe plantarse a una distancia de 3.0 m.",
        ['higo'],
        single_response=True
    )

    response(
        "El olivo necesita 400 ml de agua diarios, 8 horas de luz al día, 30 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima árido y seco, y debe plantarse a una distancia de 6.0 m.",
        ['olivo', 'aceituna'],
        single_response=True
    )

    response(
        "El nogal necesita 900 ml de agua diarios, 7 horas de luz al día, 70 g de composta al mes, se adapta a pisos térmicos templados (1200-2500 msnm), clima templado y fresco, y debe plantarse a una distancia de 8.0 m.",
        ['nogal'],
        single_response=True
    )

    response(
        "El almendro necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 6.0 m.",
        ['almendro', 'almendra'],
        single_response=True
    )

    response(
        "El pistacho necesita 600 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima árido y seco, y debe plantarse a una distancia de 6.0 m.",
        ['pistacho'],
        single_response=True
    )

    response(
        "El girasol necesita 700 ml de agua diarios, 8 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.4 m.",
        ['girasol'],
        single_response=True
    )

    response(
        "La lavanda necesita 300 ml de agua diarios, 7 horas de luz al día, 20 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.4 m.",
        ['lavanda'],
        single_response=True
    )

    response(
        "La vainilla necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.5 m.",
        ['vainilla'],
        single_response=True
    )

    response(
        "El té necesita 500 ml de agua diarios, 5 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos templados (1000-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 1.5 m.",
        ['te', 'té'],
        single_response=True
    )

    response(
        "El trigo necesita 600 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (2000-3000 msnm), clima templado y seco, y debe plantarse a una distancia de 0.2 m.",
        ['trigo'],
        single_response=True
    )

    response(
        "El arroz necesita 1000 ml de agua diarios, 7 horas de luz al día, 80 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['arroz'],
        single_response=True
    )

    response(
        "La soya necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos templados (1000-2000 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['soya', 'soja'],
        single_response=True
    )

    response(
        "El girasol ornamental necesita 650 ml de agua diarios, 8 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.5 m.",
        ['girasol ornamental','girasol','ornamental'],
        single_response=True
    )

    response(
        "El bambú necesita 800 ml de agua diarios, 6 horas de luz al día, 70 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.5 m.",
        ['bambu', 'bambú'],
        single_response=True
    )
    response(
        "La avena necesita 550 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (1500-2800 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.25 m.",
        ['avena'],
        single_response=True
    )

    response(
        "El sorgo necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['sorgo'],
        single_response=True
    )

    response(
        "El lino necesita 600 ml de agua diarios, 6 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.25 m.",
        ['lino'],
        single_response=True
    )

    response(
        "El maní necesita 650 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.4 m.",
        ['mani', 'maní'],
        single_response=True
    )

    response(
        "El sésamo necesita 500 ml de agua diarios, 7 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['sesamo', 'sésamo'],
        single_response=True
    )

    response(
        "El girasol de aceite necesita 700 ml de agua diarios, 8 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.5 m.",
        ['girasol de aceite','girasol','aceite'],
        single_response=True
    )

    response(
        "El cardamomo necesita 800 ml de agua diarios, 6 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['cardamomo'],
        single_response=True
    )

    response(
        "La cúrcuma necesita 700 ml de agua diarios, 6 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['curcuma', 'cúrcuma'],
        single_response=True
    )

    response(
        "El jengibre necesita 650 ml de agua diarios, 6 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.4 m.",
        ['jengibre'],
        single_response=True
    )

    response(
        "La canela necesita 700 ml de agua diarios, 6 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 3.0 m.",
        ['canela'],
        single_response=True
    )

    response(
        "La nuez moscada necesita 750 ml de agua diarios, 6 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 4.0 m.",
        ['nuez moscada','nuez','moscada'],
        single_response=True
    )

    response(
        "El anís necesita 400 ml de agua diarios, 6 horas de luz al día, 30 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y seco, y debe plantarse a una distancia de 0.3 m.",
        ['anis', 'anís'],
        single_response=True
    )

    response(
        "El eneldo necesita 450 ml de agua diarios, 6 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos bajos (500-1500 msnm), clima templado y seco, y debe plantarse a una distancia de 0.3 m.",
        ['eneldo'],
        single_response=True
    )

    response(
        "La salvia necesita 400 ml de agua diarios, 6 horas de luz al día, 25 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['salvia'],
        single_response=True
    )

    response(
        "El laurel necesita 500 ml de agua diarios, 7 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima templado y seco, y debe plantarse a una distancia de 2.0 m.",
        ['laurel'],
        single_response=True
    )

    response(
        "El clavo necesita 700 ml de agua diarios, 6 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 3.0 m.",
        ['clavo'],
        single_response=True
    )

    response(
        "La stevia necesita 500 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['stevia'],
        single_response=True
    )

    response(
        "La hierbabuena necesita 500 ml de agua diarios, 6 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.3 m.",
        ['hierbabuena'],
        single_response=True
    )

    response(
        "La alcachofa necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.8 m.",
        ['alcachofa'],
        single_response=True
    )

    response(
        "El espárrago necesita 600 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.4 m.",
        ['esparrago', 'espárrago'],
        single_response=True
    )

    response(
        "El nabo necesita 550 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (1000-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['nabo'],
        single_response=True
    )

    response(
        "La remolacha necesita 600 ml de agua diarios, 6 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['remolacha', 'betabel'],
        single_response=True
    )

    response(
        "El rábano necesita 500 ml de agua diarios, 6 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos bajos (500-1800 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.2 m.",
        ['rabano', 'rábano'],
        single_response=True
    )

    response(
        "La acelga necesita 550 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['acelga'],
        single_response=True
    )

    response(
        "La berenjena necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.5 m.",
        ['berenjena'],
        single_response=True
    )

    response(
        "El chile necesita 650 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.4 m.",
        ['chile', 'ají', 'guindilla','aji'],
        single_response=True
    )

    response(
        "El pimiento necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y templado, y debe plantarse a una distancia de 0.4 m.",
        ['pimiento', 'morrón','morron'],
        single_response=True
    )

    response(
        "La okra necesita 650 ml de agua diarios, 7 horas de luz al día, 50 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 0.5 m.",
        ['okra'],
        single_response=True
    )

    response(
        "La malanga necesita 800 ml de agua diarios, 6 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['malanga'],
        single_response=True
    )

    response(
        "El ñame necesita 850 ml de agua diarios, 6 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['ñame', 'name'],
        single_response=True
    )

    response(
        "El taro necesita 800 ml de agua diarios, 6 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 1.0 m.",
        ['taro'],
        single_response=True
    )

    response(
        "El lino de flor azul necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (1000-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['lino azul','lino','azul'],
        single_response=True
    )

    response(
        "El amaranto necesita 550 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['amaranto'],
        single_response=True
    )

    response(
        "El mijo necesita 500 ml de agua diarios, 7 horas de luz al día, 40 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima árido y seco, y debe plantarse a una distancia de 0.25 m.",
        ['mijo'],
        single_response=True
    )

    response(
        "El cáñamo necesita 700 ml de agua diarios, 7 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.5 m.",
        ['cañamo', 'cáñamo'],
        single_response=True
    )

    response(
        "El lino dorado necesita 600 ml de agua diarios, 6 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos templados (800-2000 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.3 m.",
        ['lino dorado','lino','dorado'],
        single_response=True
    )

    response(
        "El trébol necesita 400 ml de agua diarios, 5 horas de luz al día, 30 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima templado y húmedo, y debe plantarse a una distancia de 0.25 m.",
        ['trébol', 'trebol'],
        single_response=True
    )

    response(
        "El pasto de trigo necesita 500 ml de agua diarios, 6 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima templado y fresco, y debe plantarse a una distancia de 0.25 m.",
        ['pasto de trigo','pasto','trigo'],
        single_response=True
    )

    response(
        "La chía necesita 450 ml de agua diarios, 7 horas de luz al día, 35 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['chia', 'chía'],
        single_response=True
    )

    response(
        "El amaranto rojo necesita 550 ml de agua diarios, 7 horas de luz al día, 45 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y seco, y debe plantarse a una distancia de 0.3 m.",
        ['amaranto rojo','amaranto','rojo'],
        single_response=True
    )

    response(
        "La guanábana necesita 800 ml de agua diarios, 7 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 5.0 m.",
        ['guanabana', 'guanábana'],
        single_response=True
    )

    response(
        "El zapote necesita 850 ml de agua diarios, 7 horas de luz al día, 70 g de composta al mes, se adapta a pisos térmicos bajos (0-1200 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 5.0 m.",
        ['zapote','sapote'],
        single_response=True
    )

    response(
        "El níspero necesita 700 ml de agua diarios, 6 horas de luz al día, 55 g de composta al mes, se adapta a pisos térmicos bajos (0-1500 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 3.0 m.",
        ['nispero', 'níspero'],
        single_response=True
    )

    response(
        "El tamarindo necesita 900 ml de agua diarios, 7 horas de luz al día, 75 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y seco, y debe plantarse a una distancia de 6.0 m.",
        ['tamarindo'],
        single_response=True
    )

    response(
        "El maracuyá necesita 700 ml de agua diarios, 7 horas de luz al día, 60 g de composta al mes, se adapta a pisos térmicos bajos (0-1000 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 2.0 m.",
        ['maracuya', 'maracuyá', 'fruta de la pasión','fruta','pasion','fruta de la pasion','pasión'],
        single_response=True
    )

    response(
        "El lichi necesita 750 ml de agua diarios, 6 horas de luz al día, 65 g de composta al mes, se adapta a pisos térmicos bajos (0-800 msnm), clima cálido y húmedo, y debe plantarse a una distancia de 4.0 m.",
        ['lichi', 'lychee'],
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
