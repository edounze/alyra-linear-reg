# Demo

question = input("Comment tu vas ? ")

print("Réponse : " + question)

def askAge():
    try:
        response_age=int(input("Quel est votre age ? "))
    except:
        print("Merci de saisir une valeur numérique")
        askAge()
    else:
        if response_age > 40:            
            print("Vous avez", response_age, "ans")
        else:
            print(response_age,"ans:" ,"Ca va, tu es jeune")

askAge()