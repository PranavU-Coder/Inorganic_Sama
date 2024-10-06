from random import choice
def get_response(user_input:str)->str:
    lowered: str = user_input.lower()

    if(lowered==''):
        return 'Well . you\'re silent ...'
    elif 'hello' in lowered:
        return 'hello buddy , what are you doing in discord , go to study !!!'
    elif 'bye' in lowered:
        return 'you better study and not waste time on instagram !'
    elif 'ok' in lowered:
        return 'do you want to know anything specific'
    elif 'covalent bonds' in lowered:
        return 'the bond formed between two atoms by mutual sharing of electrons between them so as to complete their octets or duplets'
    elif 'octet rule' in lowered:
        return 'This rule is based on the observation that atoms of noble gases, which are very stable, have eight electrons in their valence shell. The octet rule helps to explain why atoms form bonds and how they do so'
    elif 'limitations' in lowered:
        return 'several limitations which include : (1) elements beyond the third period , (2) incomplete octet , (3) expanded octet , (4) odd electron molecules and so on'
    elif 'formal charge' in lowered:
        return 'total number of valence electrons in free atom - (total no. of lone pair of electrons) - 0.5*(total no. of bond pair of electrons)'
    elif 'lattice enthalpy' in lowered:
        return 'defined as energy required to completely seperate one mole of an ionic compound into its constituent gaseous counterparts completely'
    else:
        return choice(['I dont understand...',
                       'What are you talking about ?',
                       'Do you mind rephrasing that'])