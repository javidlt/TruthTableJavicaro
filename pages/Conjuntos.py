import streamlit as st
import re
import random 
import pandas as pd
 
st.set_page_config(
    page_title="Conjuntos",
    page_icon="👋",
)

st.write("# Operaciones con conjuntos")

numConjuntos = 0
numElemConjuntos = 2
# ? union
# % interseccion
# $ diferencia
# # diferencia simetrica
operadores = ["?","%","$","#"]

dictConjuntos= {}

def listIntersection(lists):
    intersection = set(lists[0])
    for i in range(1, len(lists)):
        intersection = intersection.intersection(set(lists[i]))
    return list(intersection)

def listUnion(listOfLists):
  elements = set()
  for lista in listOfLists:
    elements.update(lista)
  return [*elements]

def diferenciaSimetrica(conjuntos):
    resultado = set(conjuntos[0])
    for i, conjunto in enumerate(conjuntos):
        if i != 0:
            resultado ^= set(conjunto)
    return list(resultado)

def diferencia(conjuntos):
    resultado = set(conjuntos[0])
    for i, con in enumerate(conjuntos):
        if i != 0:
            resultado = resultado - set(con)
    return list(resultado)
  
def generarConjuntos(nCon, nElCon):
    global dictConjuntos
    dict = {}
    for i in range(nCon):
        newCon = []
        for n in range(nElCon):
            el = random.randint(0,9)
            newCon.append(el)
        dict[posiblesConjuntos[i]] = newCon
    # st.write(dict)
    return dict

# Input "A?B?(C%(D$A)%E%F)?(A$(B#D))?(F#C)"
# Output {"YSV": [], "QDI": [], "CIRIT": [], "AUBU(CIRIT)U(QDI)U(YSV)": []}
posiblesConjuntos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def detectarSiEsConjunto(el):
    if el.lower() in posiblesConjuntos:
        return True
    else:
        return False
        
def group_consecutives(vals, step=1):
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result

def reorderList(indicesnuevos, indicesviejos, lista):
    print(f"lista no ordenada: {lista}")
    nueva_lista = [None] * len(lista)
    for i, (subindicesNuevos, subindicesViejos) in enumerate(zip(indicesnuevos, indicesviejos)):
        for j, (indicenuevo, indiceviejo) in enumerate(zip(subindicesNuevos, subindicesViejos)):
            nueva_lista[indicenuevo] = lista[indiceviejo]

    orderedList = []
    for last, new in zip(lista, nueva_lista):
        valueToAppend = 0
        if new == None:
            valueToAppend = last
        else: 
            valueToAppend = new
        orderedList.append(valueToAppend)
    print(f"lista ordenada: {orderedList}")
    
    return orderedList


# ? union
# % interseccion
# $ diferencia
# # diferencia simetrica
operadores = ["?","%","$","#"]
def opConjuntos(dictionary):
    print(f"es este {dictionary}")
    for elemento in dictionary.keys():
        result = []
        print(f"llega a empty {dictionary[elemento]}")
        if len(dictionary[elemento]) == 0:
            operation = elemento
            opType = ""
            listWithOpsInOperation = []
            for o in operation:
                if o in operadores:
                    listWithOpsInOperation.append(o)
            print(f"llega a esto {listWithOpsInOperation}")
            if listWithOpsInOperation[0] == "?":
                opType = "?"
            elif listWithOpsInOperation[0] == "%":
               opType = "%"
            elif listWithOpsInOperation[0] == "$":
               opType = "$"
            elif listWithOpsInOperation[0] == "#":
               opType = "#"
            
            # encontrar si tiene parentesis y quitarselos
            if "(" in operation and operation[0] == "(":
               print("si llega aquí")
               operation = operation[1:-1]
               print(operation)
            print(operation)
            # remplazar el tipo de operacion por espacio
            operation = operation.replace(opType, " ")
            print(operation)
            # convertir operaciones en array con sus componentes
            operation = operation.split(" ")
            operation = [x for x in operation if x != '']
            print(operation)

            listToOperate = []
            for con in operation:
            #    con = con.replace(" ", "")
               print(f"conjunto {con}")
               conjuntoDeElementos = dictionary[con] 
               listToOperate.append(conjuntoDeElementos)
            print(operation)
            print(listToOperate)
            #quitar listas vacias en caso de haber
            listToOperate = [ele for ele in listToOperate if ele != []]
            print(listToOperate)

            if opType == "?":
                result = listUnion(listToOperate)
            elif opType == "%":
                result = listIntersection(listToOperate)
            elif opType == "$":
                result = diferencia(listToOperate)
            elif opType == "#":
                result = diferenciaSimetrica(listToOperate)
            
            print(f"resultado {elemento} {result}")
            dictionary[elemento] = result
    return dictionary
            

def separateOps(operation, prevDictWithConj):
    dictReturn = {}
    for el in operation:
        if detectarSiEsConjunto(el):
            queryToLookForInDict = el.lower()
            dictReturn[el] = prevDictWithConj[queryToLookForInDict]

    newOp = operation.replace("(", "/")
    newOp = newOp.replace(")", "&")
    objectOfIndexesOfopenPar = re.finditer(pattern="/", string=newOp)
    indexesWhereOpenParAppears = [index.start() for index in objectOfIndexesOfopenPar]
    objectOfIndexesOfClosePar = re.finditer(pattern="&", string=newOp)
    indexesWhereCloseParAppears = [index.start() for index in objectOfIndexesOfClosePar]
    listWithIndexesWhereParOpensAEnds = []
    indexesOfOpsToTakeCareOf = []
    for i, (open, close) in enumerate(zip(indexesWhereOpenParAppears, indexesWhereCloseParAppears)):
        if i < len(indexesWhereCloseParAppears)-1:
            if (indexesWhereOpenParAppears[i+1] in range(indexesWhereOpenParAppears[i], indexesWhereCloseParAppears[i])):
                indexesOfOpsToTakeCareOf.append(i)
                indexesOfOpsToTakeCareOf.append(i+1)
    
    indexesOfOpsToTakeCareOf = list(set(indexesOfOpsToTakeCareOf))
    originalIndexesOfOpsToTakeCareOf = group_consecutives(indexesOfOpsToTakeCareOf)
    newIndexesOfOpsToTakeCareOf = []
    for i, subList in enumerate(originalIndexesOfOpsToTakeCareOf):
        newList = []
        for i,z in enumerate(subList):
            if i < len(subList)-1:
                el = subList[(len(subList)-1)-i]
            else:
                el = subList[0]
            newList.append(el)  
        newIndexesOfOpsToTakeCareOf.insert(i, newList)

    indexesWhereCloseParAppears = reorderList(newIndexesOfOpsToTakeCareOf, originalIndexesOfOpsToTakeCareOf, indexesWhereCloseParAppears) 
    print(indexesWhereOpenParAppears)
    print(indexesWhereCloseParAppears)

    # lista con sublistas con los indeces en dónde se abre un parentesis y se cierra otro 
    listWithIndexesWhereParOpensAEnds
    for open, close in zip(indexesWhereOpenParAppears, indexesWhereCloseParAppears):
        listWithIndexesWhereParOpensAEnds.append([open, close])

    # generar lista con las operaciones
    listWithOpsInOrder = []
    for el in listWithIndexesWhereParOpensAEnds:
        op = operation[el[0]:el[1]+1]
        listWithOpsInOrder.append(op)
    listWithOpsInOrder.sort(key=len)
    listWithOpsInOrder.append(operation)

    for oper in listWithOpsInOrder:
        dictReturn[oper] = []
    
    return dictReturn


def generador():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            numConjuntos = st.number_input('Ingresa número de conjuntos', min_value=2)
            st.write('Número de conjuntos ', numConjuntos)
        with col2:
            numElemConjuntos = st.number_input('Ingresa número de elementos por conjunto', min_value=2)
            st.write('Elementos por conjunto ', numElemConjuntos)
        
    dictConjuntos = generarConjuntos(numConjuntos, numElemConjuntos)
    operation = st.text_input('Operación', '')
    st.write("? unión / % intersección / $ diferencia / # diferencia simétrica" )
    st.write("Si deseas usar más de un operador en la misma operación utiliza paréntesis para la jerarquía" )
    
    responses = {}
    try:
        responses = separateOps(operation, dictConjuntos)
        print(responses)
        
        responses = opConjuntos(responses)
        print(f"llega aquí {responses}")
    except:
        dictConjuntos = separateOps(operation, dictConjuntos)
        entryDict = generarConjuntos(numConjuntos, numElemConjuntos)
        print("entryDict")
        responses = opConjuntos(entryDict)
        
    dt = pd.DataFrame.from_dict(dictConjuntos, orient='index')
    st.table(dt)
    st.write(responses)
    if operation != "":
        st.write(f"Cardinalidad {operation}: {len(responses[operation])}")

def ingresar(): 
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            conjunto1 = st.text_input('Ingresa un conjunto A', '')
        with col2:
            conjunto2 = st.text_input('Ingresa un conjunto B', '')
        with col3:
            conjunto3 = st.text_input('Ingresa un conjunto C', '')
    
    try:
        conjunto1 = conjunto1.split(",")
        newConjunto1 = []
        if conjunto1 != []:
            for i in conjunto1:
                changed1 = i
                print(i)
                newConjunto1.append(int(changed1))
        conjunto2 = conjunto2.split(",")
        newConjunto2 = []
        if conjunto2 != []:
            for i in conjunto2:
                changed2 = i
                print(i)
                newConjunto2.append(int(changed2))
        conjunto3 = conjunto3.split(",")
        newConjunto3 = []
        if conjunto3 != []:
            for i in conjunto3:
                changed3 = i
                print(i)
                newConjunto3.append(int(changed3))
    except:
        newConjunto1 = []
        newConjunto2 = []
        newConjunto3 = []

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Cardinalidad A {len(set(conjunto1))}")
        with col2:
            st.write(f"Cardinalidad B {len(set(conjunto2))}")
        with col3:
            st.write(f"Cardinalidad C {len(set(conjunto3))}")

    dictToIterate = {"a": newConjunto1, "b": newConjunto2, "c": newConjunto3}
    operacion = st.text_input('Ingresa la operación con máximo 3 conjuntos (A, B, C)', '')
    st.write("? unión / % intersección / $ diferencia / # diferencia simétrica" )
    st.write("Si deseas usar más de un operador en la misma operación utiliza paréntesis para la jerarquía" )

    dt = pd.DataFrame.from_dict(dictToIterate, orient='index')
    st.table(dt)

    try:
        responses = separateOps(operacion, dictToIterate)
        responses = opConjuntos(responses)
        st.write(responses)
        if operacion != "":
            st.write(f"Cardinalidad {operacion}: {len(responses[operacion])}")
    except:
        st.write("completa la info")

    

sb = st.sidebar
page_names = ["Generador automatico de conjuntos", "Ingresar tus conjuntos conjuntos"]
page = sb.radio("", page_names, index=0)

if page == "Generador automatico de conjuntos":
    generador() 
    # if listadeConjuntos != []:
elif page == "Ingresar tus conjuntos conjuntos":
    ingresar()