import more-itertools as mit
import pandas as pd
import streamlit as st

def sumatoria(coordenates):
    sum = 0
    if len(coordenates)==0:
        return 0
    else:
        val = coordenates[0][1] if coordenates[0][1] != 'indefinido' else 0 
        sum = val + sumatoria(coordenates[1:]) 
    
    return sum

def multiplicatoria(coordenates):
    mult = 1
    if len(coordenates)==0:
        return 1
    else:
        val = coordenates[0][1] if coordenates[0][1] != 'indefinido' else 1
        mult = val * multiplicatoria(coordenates[1:]) 
    
    return mult

def gruoupConsequtiveIndexes(arrayOfIndexes, xArray):
    for element in xArray:
        if not element[1].isdigit():
            newArrayOfOperations.append(element[1])

    for group in mit.consecutive_groups(arrayOfIndexes):
        l = []
        for indexElement in group:
            for x in xArray:
                if indexElement == x[0]:
                    l.append(x[1])

        if not l:
            x = "no hacer nada"
        else:
            #Hacer string el subgrupo de numeros y agregarlo a la lista
            newNumber = ''.join(l)
            newArrayOfDigits.append(newNumber)

def concatConsequitiveNumbers(array):
    newtArray = []

    for value in array:
        if value[1] == True:
            newtArray.append(value[0])
        else:
            break

    return newtArray

def getIndexOfDigitsAndDigits(arrayToWorkWith):
    list = []
    for i, x in enumerate(arrayToWorkWith):
        if x[1] == "number":
            list.append((i,x[0]))
        else:
            list.append((i, x[1]))

    return list

def orderOperationElements (operation, array):
    for character in operation:
        if character.isdigit() == True:
            whatCharacterIs = "number"
        elif character == "+":
            whatCharacterIs = "sum"
        elif character == "-":
            whatCharacterIs = "subtract"
        elif character == "/":
            whatCharacterIs = "division"
        elif character == "*":
            whatCharacterIs = "multiplication"
        elif character == "**" or character == "^":
            whatCharacterIs = "power"
        elif character == "//":
            whatCharacterIs = "division"
        elif character == "%":
            whatCharacterIs = "remainderOfaDivision"
        elif character == "(" or character == "[":
            whatCharacterIs = "hierarchyOpener"
        elif character == ")" or character == "]":
            whatCharacterIs = "hierarchyCloser"
        else:
            # darle un distintivo a cada variable
            whatCharacterIs = f"variable '{character}' (se repite {operation.count(character)} veces)"

        array.append((character, whatCharacterIs))

def returnIndexOfValuesToConcat (array):
    return [i for i, x in enumerate(array) if x[1] == "number"]

def orderElementsOfTheOperation (array, arrayWithOrderedElements, currentValue):
    for value in array:
        if value[1] != currentValue[1] or value[1] == "hierarchyCloser":
            if value[1].isdigit() == True:
                arrayWithOrderedElements.append(currentValue[0])
            else:
                arrayWithOrderedElements.append(currentValue[1])
            currentValue = value
    if value[1].isdigit():
        arrayWithOrderedElements.append(currentValue[0])
    else:
        arrayWithOrderedElements.append(currentValue[1])

def orderOperationWithRealNumbers (array, orderedOperationWithRealNumbers, arrayOfOperations, arrayOfDigits):
    for elementInOrderofOperation in array:
        if elementInOrderofOperation != "number":
            orderedOperationWithRealNumbers.append(arrayOfOperations[0])
            # Eliminar primer elemento actual de la lista de operaciones para que se siga actualizando
            arrayOfOperations.pop(0)
        else:
            orderedOperationWithRealNumbers.append(arrayOfDigits[0])
            # Eliminar primer elemento actual de la lista de digitos para que se siga actualizando
            arrayOfDigits.pop(0)

def findAndGiveValueToVariables (list_of_variables, list_of_values_of_variables, ordered_operation_withNumbers):
    for e in ordered_operation_withNumbers:
        if e[:8] == "variable":
            if ordered_operation_withNumbers.count(e) >= 1:
                if list_of_variables.count(e) == 0:
                        list_of_variables.append(e)

    # Darle un valor a cada variable
    for e in list_of_variables:
        value = input(f"Ingresa el valor de la {e}: ")
        list_of_values_of_variables.append(value)

def findAndGiveValueToVariableInFunction (list_of_variables, pointInX, ordered_operation_withNumbers):
    list_of_values_of_variables = []
    for e in ordered_operation_withNumbers:
        if e[:8] == "variable":
            if ordered_operation_withNumbers.count(e) >= 1:
                if list_of_variables.count(e) == 0:
                        list_of_variables.append(e)

    # Darle un valor a cada variable
    for e in list_of_variables:
        list_of_values_of_variables.append(str(pointInX))
    
    return list_of_values_of_variables


def processProblem (problema, orderedOperation, listOfValuesOfVariables):
    for i, elementInOrderofOperation in enumerate(orderedOperation):
        if elementInOrderofOperation == "sum":
            add = "+"
            problema = problema + add
        elif elementInOrderofOperation == "subtract":
            add = "-"
            problema = problema + add
        elif elementInOrderofOperation == "division":
            add = "/"
            problema = problema + add
        elif elementInOrderofOperation == "multiplication":
            add = "*"
            problema = problema + add
        elif elementInOrderofOperation == "power":
            add = "**"
            indexToGoBack = len(orderedOperation[i - 1])
            problemLength = len(problema)
            whereToInsertHierarchyOpener = problemLength - indexToGoBack - 1
            if "variable" in orderedOperation[i - 1]:
                problema = problema[:whereToInsertHierarchyOpener] + "(" + problema[whereToInsertHierarchyOpener:] + ")" + add
            else:
                problema = problema + add
        elif elementInOrderofOperation == "divisionWhitoutDecimals":
            add = "//"
            problema = problema + add
        elif elementInOrderofOperation == "remainderOfaDivision":
            add = "%"
            problema = problema + add
        elif elementInOrderofOperation == "hierarchyOpener":
            add = "("
            if i != 0:
                if orderedOperation[i - 1].isdigit():
                    problema = problema + "*" + add
                elif "variable" in orderedOperation[i - 1]:
                    problema = problema + "*" + add
                elif orderedOperation[i - 1] == "hierarchyCloser":
                    problema = problema + "*" + add
                else:
                    problema = problema + add
            else:
                problema = problema + add
        elif elementInOrderofOperation == "hierarchyCloser":
            add = ")"
            problema = problema + add
        elif elementInOrderofOperation[:8] == "variable":
            indexOfVariable = listOfVariables.index(elementInOrderofOperation)

            if i != 0:
                if orderedOperation[i - 1].isdigit():
                    problema = problema + "*" + listOfValuesOfVariables[indexOfVariable]
                elif "variable" in orderedOperation[i - 1]:
                    problema = problema + "*" + listOfValuesOfVariables[indexOfVariable]
                elif orderedOperation[i - 1] == "hierarchyCloser":
                    problema = problema + "*" + listOfValuesOfVariables[indexOfVariable]
                else:
                    problema = problema + listOfValuesOfVariables[indexOfVariable]
            else:
                problema = problema + listOfValuesOfVariables[indexOfVariable]

        else:
            if i != 0:
                if orderedOperation[i - 1] == "hierarchyCloser":
                    add = elementInOrderofOperation
                    problema = problema + "*" + add
                else:
                    add = elementInOrderofOperation
                    problema = problema + add
            else:
                add = elementInOrderofOperation
                problema = problema + add

    return problema

# operationstring = "2k^(k-1)"
st.title("Calculadora de Sucesiones")
inputvalue = st.text_input("Operación", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Ej. 2k^(8-3k)", disabled=False, label_visibility="visible")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        initVal = st.number_input('Ingresa valor inicial de la variable', value=0)
    with col2:
        lastVal = st.number_input('Ingresa valor final de la variable', value=0)
    with col3:
        interval = st.number_input('Ingresa intervalo de la sucesión', value=0)
    
newArrayOfOperations = []
newArrayOfDigits = []
listOfVariables = []
listaDeProblemas = []

def enter(op, ini, las, inter):
    operation = [*op]

    countVariables = 0
    for character in operation:
        if character.isalpha() == True:
            countVariables = countVariables + 1
        else:
            countVariables = 0

    if operation:
        print(inputvalue)

    # print("-"*25 + " SELECCIONA EL RANGO PARA LA TABLA Y GRÁFICA " + "-"*25)
    # xInicial = int(input("Valor inicial de x: "))
    # xFinal = int(input("Valor final de x: "))
    # intervalBetweenEachPoint = int(input("Intervalo entre cada punto: "))
    valuesInXForFunction = []
    for i in range(ini, (las+inter), inter):
        valuesInXForFunction.append(i)

    temporaryArray = []
    orderOperationElements(operation, temporaryArray)
    # indexOfvaluesToConcat = [i for i, x in enumerate(temporaryArray) if x[1] == "number"]
    indexOfvaluesToConcat = returnIndexOfValuesToConcat(temporaryArray)
    arrayWithIndexAndCharacter = getIndexOfDigitsAndDigits(temporaryArray)
    gruoupConsequtiveIndexes(indexOfvaluesToConcat, arrayWithIndexAndCharacter)
    allElementsOfOperation = (newArrayOfOperations + newArrayOfDigits)
    # Elementos de la operación ordenados
    result_list = []
    current = temporaryArray[0]
    orderElementsOfTheOperation(temporaryArray, result_list, current)
    # Ordered operation con los valores de los números
    orderedOperation = []
    orderOperationWithRealNumbers(result_list, orderedOperation, newArrayOfOperations, newArrayOfDigits)
    # Encontrar Los puntos en X y en Y
    listOfX = valuesInXForFunction
    listOfY = []
    coordinatesForTable = []

    print(" " * 50)
    print(" " * 50)
    print("-" * 25 + " VALORES EN X SUSTITUIDOS " + "-" * 25)
    for i, value in enumerate(valuesInXForFunction):
        # listOfValuesOfVariables = []
        listOfValuesOfVariables = findAndGiveValueToVariableInFunction(listOfVariables, value, orderedOperation)
        # Procesar problema
        problema = ""
        problem = processProblem(problema, orderedOperation, listOfValuesOfVariables)
        listaDeProblemas.append(problem)
        print(f"{problem}")
        try: 
            pointInY = eval(problem)  
        except: 
            pointInY = "indefinido" 

        print(f"Respuesta: {pointInY}")
        listOfY.append(pointInY)

    for i, value in enumerate(listOfX):
        coordinatesForTable.append((value, listOfY[i]))

    sumaElementos = sumatoria(coordinatesForTable)
    productoElementos = multiplicatoria(coordinatesForTable)
    dictToIterate = {"variable": listOfX, "Sustición": listaDeProblemas,"Valores sucesión": listOfY}
    dt = pd.DataFrame.from_dict(dictToIterate, orient="index")
    st.table(dt)
    st.write(f"Sumatoria: {sumaElementos}")
    st.write(f"Multiplicatoria: {productoElementos}")

try:
    enter(inputvalue, initVal, lastVal, interval)
except:
    st.write("Complete datos necesarios")


