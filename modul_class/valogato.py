def valogato(Lista : list[float])-> list[float]:
    ujLista = []
    for i in range(len(Lista)) :
        for j in range(i+1,len(Lista)) :
                if Lista[i] == Lista[j] and Lista[j] not in ujLista :
                    ujLista.append(Lista[i])
    return ujLista