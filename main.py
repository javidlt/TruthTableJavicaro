import re
import pandas as pd
import streamlit as st

if 'stringtoOperate' not in st.session_state:
	st.session_state.stringtoOperate = ""

inputvalue = st.session_state.stringtoOperate

def addOperator(butt):
    if butt == "d":
        st.session_state.stringtoOperate = ""
    elif butt == "-":
        st.session_state.stringtoOperate = inputvalue[:-1]
    elif butt == "(":
        st.session_state.stringtoOperate = st.session_state.stringtoOperate + "("
    elif butt == ")":
        st.session_state.stringtoOperate = st.session_state.stringtoOperate + ")"
    else:
        st.session_state.stringtoOperate = st.session_state.stringtoOperate + butt

def divideList(lista, tamano):
    resultados = []
    i = 0
    while i < len(lista):
        resultados.append(lista[i:i+tamano])
        i += tamano
    return resultados

st.title("Calculadora de tablas de verdad")

def opToShow(op):
    displayOp = op
    displayOp = displayOp.replace("&", "^")
    displayOp = displayOp.replace("~", "¬")
    displayOp = displayOp.replace("/", "⊕")
    displayOp = displayOp.replace("#", "→")
    displayOp = displayOp.replace("*", "⇔")

    return displayOp

valueToDisplay = opToShow(inputvalue)

st.text_input("Operación", value=valueToDisplay, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Ej. p^q", disabled=False, label_visibility="visible")

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
       st.button("p", on_click=addOperator, args=("p"))
    with col2:
        st.button("q", on_click=addOperator, args=("q"))
    with col3:
        st.button("r", on_click=addOperator, args=("r"))
    with col4:
        st.button("s", on_click=addOperator, args=("s"))
    with col5:
        st.button("¬", on_click=addOperator, args=("~"), type="primary")
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("b", on_click=addOperator, args=("b"))
    with col2:
        st.button("f", on_click=addOperator, args=("f"))
    with col3:
        st.button("g", on_click=addOperator, args=("g"))
    with col4:
        st.button("h", on_click=addOperator, args=("h"))
    with col5:
        st.button("^", on_click=addOperator, args=("&"), type="primary")
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("i", on_click=addOperator, args=("i"))
    with col2:
        st.button("j", on_click=addOperator, args=("j"))
    with col3:
        st.button("k", on_click=addOperator, args=("k"))
    with col4:
        st.button("l", on_click=addOperator, args=("l"))
    with col5:
        st.button("v", on_click=addOperator, args=("v"), type="primary")
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("m", on_click=addOperator, args=("m"))
    with col2:
        st.button("u", on_click=addOperator, args=("u"))
    with col3:
        st.button("w", on_click=addOperator, args=("w"))
    with col4:
        st.button("x", on_click=addOperator, args=("x"))
    with col5:
        st.button("⊕", on_click=addOperator, args=("/"), type="primary")
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("y", on_click=addOperator, args=("y"))
    with col2:
        st.button("z", on_click=addOperator, args=("z"))
    with col3:
        st.button("(", on_click=addOperator, args=("("))
    with col4:
        st.button(")", on_click=addOperator, args=(")"))
    with col5:
        st.button("→", on_click=addOperator, args=("#"), type="primary")
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("t", on_click=addOperator, args=("t"))
    with col2:
        st.button("c", on_click=addOperator, args=("c"))
    with col3:
        st.button("Del", on_click=addOperator, args=("d"))
    with col4:
        st.button("X", on_click=addOperator, args=("-"), type="secondary")
    with col5:
        st.button("⇔", on_click=addOperator, args=("*"), type="primary")

operationPrueba = inputvalue

arrayvar = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'u', 'w', 'x', 'y', 'z']
arrayvarAndTandC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

# / o xclusiva
# # -> 
# * <->

arrayops = ["&", "v", "~", "/", "#", "*"]

def generaValores( iteracion, numCols):
    values = []
    for i in range(numCols):
        value = (i // iteracion) % 2 == 1
        values.append(value)
    return values

def identifyVariables(element):
    if element in arrayvarAndTandC: 
        return True

        
def findIndexesStartAndEnd(char, stringg):
    objectOfIndexes = re.finditer(pattern=char, string=stringg)
    indexesWhereOpAppears = [[index.start(), index.end()] for index in objectOfIndexes]
    return indexesWhereOpAppears

qtyOfVariables = 0

def find(char, string):
    return [i for i, ltr in enumerate(string) if ltr == char]

def checkParenthesis(operation):
    countOfOpenParentheses = operation.count("(")
    countOfClosedParentheses = operation.count(")")
    if countOfOpenParentheses != countOfClosedParentheses:
        return False
    else:
        return True

def evaluateLogicExpression(expresion, valores):
    #Reemplazamos las variables de la expresión por sus valores booleanos correspondientes
    for variable, valor in valores.items(): 
        trueOrfalse = ""
        if valor == True:
            trueOrfalse = "1"
        else:
            trueOrfalse = "0"

        expresion = expresion.replace(variable, trueOrfalse)

    #Reemplazamos los operadores lógicos por los símbolos correspondientes en Python
    expresion = expresion.replace("&", " and ")
    expresion = expresion.replace("v", " or ")
    expresion = expresion.replace("~", " not ")
    expresion = expresion.replace("/", " ^ ")
    expresion = expresion.replace("#", " <= ")
    expresion = expresion.replace("*", " == ")
    expresion = expresion.replace("  ", " ")
    
    if " not 0 " in expresion: 
        expresion = expresion.replace(" not 0 ", " (not 0) ")
    
    if "not 0 " in expresion: 
        expresion = expresion.replace("not 0 ", "(not 0) ")

    if " not 0" in expresion: 
        expresion = expresion.replace(" not 0", " (not 0)")

    if " not 1 " in expresion:
        expresion = expresion.replace(" not 1 ", " (not 1) ")
    
    if "not 1 " in expresion:
        expresion = expresion.replace("not 1 ", "(not 1) ")
    
    if " not 1" in expresion:
        expresion = expresion.replace(" not 1", " (not 1)")

    result = eval(expresion) 

    if result == 1:
        return True
    elif result == 0: 
        return False

printTable = True
def separateOps(operation):
    resultTruthTable = {}
    global qtyOfVariables, printTable 
    arrayOfParenthesis = []
    error = ""
    arrayWithIndexOfOpenAndClosedParenthesis = []
    for i,char in enumerate(operation):
        # identificar variables y agregarlas al diccionario
        if identifyVariables(char):
            objectOfIndexesOfvariables = re.finditer(pattern=char, string=operation)
            indexesWhereOVarAppears = [index.start() for index in objectOfIndexesOfvariables]
            if resultTruthTable.get(char) is None:
                resultTruthTable[char] = []

            objectOfIndexesOfvariables = re.finditer(pattern=char, string=operation)
            indexesWhereOVarAppears = [index.start() for index in objectOfIndexesOfvariables]
            for index in indexesWhereOVarAppears:
                if (operation[index-1] == "~") and (resultTruthTable.get(f"~{char}") is None):
                    resultTruthTable["~"+char] = []
        # encontrar parentesis y guardar el caracter con su index
        if (char == "(") or (char == ")"):
            arrayOfParenthesis.append([i, char])
                
    for i, pC in enumerate(arrayOfParenthesis):
        # agrupar los indices según la jerarquía de operaciones
        if len(arrayOfParenthesis) > 2:
            try: 
                if (pC[1] == "(") and (arrayOfParenthesis[i+1][1] == "("):
                    closeIndex = 0
                    for idx, e in enumerate(arrayOfParenthesis[(i+1):]):
                        arrayOfParenthesisCutted = arrayOfParenthesis[(i+1):]
                        closed = False
                        if (e[1] == ")") and (arrayOfParenthesisCutted[idx-1][1] == ")") and (not closed):
                            closeIndex = arrayOfParenthesis.index(e)
                            closed = True
                            arrayWithIndexOfOpenAndClosedParenthesis.append([("abre", arrayOfParenthesis[i][0]), ("cierre", arrayOfParenthesis[closeIndex][0])])
                elif (pC[1] == "(") and (arrayOfParenthesis[i+1][1] == ")"): 
                    arrayWithIndexOfOpenAndClosedParenthesis.append([("abre", arrayOfParenthesis[i][0]), ("cierre", arrayOfParenthesis[i+1][0])])
            except:
                printTable = False
        else:
            try:
                arrayWithIndexOfOpenAndClosedParenthesis.append([("abre", arrayOfParenthesis[0][0]), ("cierre", arrayOfParenthesis[1][0])])
                break
            except:
                printTable = False
    
    #Generar array con las operaciones dentro de un parentesis y ordenarlo según la longitud
    arrayOfoperationsInsideParenthesis = []
    for p in arrayWithIndexOfOpenAndClosedParenthesis:
        generatedOp = operation[(p[0][1]):(p[1][1]+1)]
        arrayOfoperationsInsideParenthesis.append(generatedOp)
    arrayOfoperationsInsideParenthesis.sort(key=len)

    # Mantener las operaciones correctas de los parentesis y eliminar las incorrectas
    listOfelementsToMaintain = []
    for i, element in enumerate(arrayOfoperationsInsideParenthesis):
        countOfOpenPar = element.count('(')
        countOfClosePar = element.count(')')
        if countOfOpenPar == countOfClosePar:
            listOfelementsToMaintain.append(element)
    
    # Encontrar si existe negación de algún parentesis 
    for i, element in enumerate(listOfelementsToMaintain):
        indexWhereSubstrStarts = operation.find(element)
        if indexWhereSubstrStarts != 0:
            if operation[indexWhereSubstrStarts-1] == "~":
                newNegOpToAppend = "~" + element
                listOfelementsToMaintain.insert((i+1),newNegOpToAppend)

    listOfelementsToMaintain.sort(key=len)
    listOfelementsToMaintain.append(operation)

    # agregar elementos dentro de parentesis al diccionario
    for e in listOfelementsToMaintain:
        resultTruthTable[e] = []
    
    return resultTruthTable
    
columnsOftruthTableWithoutresults = separateOps(operationPrueba)

usedVariables = []
contOrTaut = []
for paso in columnsOftruthTableWithoutresults:
    if paso in arrayvar:
        qtyOfVariables += 1
        usedVariables.append(paso)
    elif( paso == "c") or (paso == "t"):
        contOrTaut.append(paso)

# print(usedVariables)
usedVariables.reverse()
qtyOfRows = 2**qtyOfVariables
for i, var in enumerate(usedVariables):
    iter = 2**i
    col = generaValores(iter, qtyOfRows)
    columnsOftruthTableWithoutresults[var] = col

for op in contOrTaut:
    if op == "t":
        col = []
        for i in range(qtyOfRows):
            col.append(True)
        columnsOftruthTableWithoutresults[op] = col
    elif op == "c":
        col = []
        for i in range(qtyOfRows):
            col.append(False)
        columnsOftruthTableWithoutresults[op] = col

def solveTable(columnsOftruthTableWithoutresults):
    # Resolver Tabla de verdad 
    for key, values in zip(columnsOftruthTableWithoutresults.keys(), columnsOftruthTableWithoutresults.values()):
         if values == []:
            arrayOfVariablesInThisOp = []
            for cOp in key:
                if cOp in arrayvarAndTandC:
                    arrayOfVariablesInThisOp.append(cOp)
            arrayOfVariablesInThisOp = list(set(arrayOfVariablesInThisOp))

            dictofValuesToOperate = {}
            contador = 0
            numOfVari = len(arrayOfVariablesInThisOp)
            listOfBoolValues = []
            for vari in arrayOfVariablesInThisOp:
                listOfValuesForEachVar = []
                for numIdx in range(qtyOfRows):
                    contador += 1
                    listOfValuesForEachVar.append((columnsOftruthTableWithoutresults.get(vari))[numIdx])
                listOfBoolValues.append((vari, listOfValuesForEachVar))

            qtyOfBoolsPerVar = len(listOfBoolValues[0][1])

            everyEvaluation = []
            for i in range(qtyOfBoolsPerVar):
                dictExpression = {}
                for val in arrayOfVariablesInThisOp:
                    boolToAdd = columnsOftruthTableWithoutresults.get(val)[i]
                    dictExpression[val] = boolToAdd
                everyEvaluation.append(dictExpression)

            for evalu in everyEvaluation:
                result = evaluateLogicExpression(key, evalu)
                columnsOftruthTableWithoutresults[key].append(result)
            
            resultTable = columnsOftruthTableWithoutresults

            return resultTable

try: 
    # Resolver Tabla de verdad 
    for key, values in zip(columnsOftruthTableWithoutresults.keys(), columnsOftruthTableWithoutresults.values()):
        if values == []:
            arrayOfVariablesInThisOp = []
            for cOp in key:
                if cOp in arrayvarAndTandC:
                    arrayOfVariablesInThisOp.append(cOp)
            arrayOfVariablesInThisOp = list(set(arrayOfVariablesInThisOp))

            dictofValuesToOperate = {}
            contador = 0
            numOfVari = len(arrayOfVariablesInThisOp)
            listOfBoolValues = []
            for vari in arrayOfVariablesInThisOp:
                listOfValuesForEachVar = []
                for numIdx in range(qtyOfRows):
                    contador += 1
                    listOfValuesForEachVar.append((columnsOftruthTableWithoutresults.get(vari))[numIdx])
                listOfBoolValues.append((vari, listOfValuesForEachVar))

            qtyOfBoolsPerVar = 0
            if len(listOfBoolValues) > 0:
                qtyOfBoolsPerVar = len(listOfBoolValues[0][1])

            everyEvaluation = []
            for i in range(qtyOfBoolsPerVar):
                dictExpression = {}
                for val in arrayOfVariablesInThisOp:
                    boolToAdd = columnsOftruthTableWithoutresults.get(val)[i]
                    dictExpression[val] = boolToAdd
                everyEvaluation.append(dictExpression)

            for evalu in everyEvaluation:
                result = evaluateLogicExpression(key, evalu)
                columnsOftruthTableWithoutresults[key].append(result)
except: 
    printTable = False

finalResultTable = columnsOftruthTableWithoutresults

if printTable and (len(finalResultTable.keys()) > 0):
    dt = pd.DataFrame.from_dict(finalResultTable)
    for (columnName, columnData) in dt.iteritems():
        dt.rename(columns={columnName: opToShow(columnName)}, inplace=True)

    st.table(dt)
    
elif printTable:
    st.write("Escribe tu expresión lógica")
else: 
    st.write("Completa tu expresión lógica")