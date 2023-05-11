import streamlit as st

st.title("Relaciones")
inputvalue = st.text_input("Relación", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Ej. (1,2), (3,4), (5,6)", disabled=False, label_visibility="visible")

# relation = [(1,1),(2,2),(1,2),(2,1)]

# Obtener elementos del conjunto
def obtainElemsOfRelation(setRe):
    elementosConjunto = str(setRe)
    elemToRemove = ["[", "]", "(", ")"]
    for e in elemToRemove:
        elementosConjunto = elementosConjunto.replace(e, '')
    elementosConjunto = [int(x) for x in list(set(elementosConjunto.split(", ")))]
    elementosConjunto.sort()
    return elementosConjunto

def reflexSet(setRe):
    response = False
    elementosConjunto = obtainElemsOfRelation(setRe)
    relacion = str(setRe)
    sumrReflex = 0
    for e in elementosConjunto:
        obgTuple = f"({e}, {e})"
        if obgTuple in relacion:
            sumrReflex += 1
    
    if sumrReflex == len(elementosConjunto):
        response = True
    
    return response
    

def transitiveSet(setRel):
    response = True
    for tupla in setRel: # recorre la relación por tuplas y separar los elementos de inicio con los elementos de fin
        ini = tupla[0]
        fin = tupla[1]
        relacion = str(setRel)
        # #encontrar tuplas que comiencen con el segundo elemento de la tupla
        tuplasQueComienUlt = [x for x in setRel if x[0] == fin]
        # print(f"ini: {ini} fin: {fin}")
        # print(tuplasQueComienUlt)
        if len(tuplasQueComienUlt) > 0:
            for t in tuplasQueComienUlt:
                tuplNecesaria = f"({ini}, {t[1]})"
                if tuplNecesaria not in relacion:                    
                    response = False 
        else:
            response = False

    return response
            
def simetricSet(setRe):
    response = True
    relacion = str(setRe)
    sumrReflex = 0
    for e in setRe:
        obgTuple = f"({e[1]}, {e[0]})"
        if not obgTuple in relacion:
            response = False
            break
    
    return response

def es_funcion(R): 
    is_Function = True 
    Dominio_usado = [] 
    Codominio = [] 

    for (x,y) in R: 
        if x not in Dominio_usado: 
            Dominio_usado.append(x) 
            Codominio.append(y) 

    if len(Dominio_usado) < len(Codominio): 
        is_Function = False 
    
    return is_Function

try: 
    relation = []
    arrayWithTuplas = inputvalue.split("),")
    for t in arrayWithTuplas:
        tupl = t.replace("(", "")
        tupl = t.replace(")", "")
        tupl = t.replace(" ", "")
        tupl = tupl.split(",")
        valX = int("".join([x for x in tupl[0] if x.isdigit()]))
        valY = int("".join([x for x in tupl[1] if x.isdigit()]))
        relation.append((valX, valY))
    
    st.write(str(relation))
    isfunction = es_funcion(relation)
    simetrica = simetricSet(relation)
    transitiva = transitiveSet(relation)
    reflexiva = reflexSet(relation)
    st.write(f"Es una función: {isfunction}")
    st.write(f"Es simétrica: {simetrica}")
    st.write(f"Es transitiva: {transitiva}")
    st.write(f"Es reflexiva: {reflexiva}")
except:
    st.write("Ingresa una peración válida")