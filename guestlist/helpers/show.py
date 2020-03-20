def show(database, group_id):
    ref = database.child(group_id)

    output = ['*' + ref.child('title').get() + '*']

    will_show = ref.child('will-show').get()
    if will_show is not None:
        output.append('\n_Participantes_')
        for i, member in enumerate(will_show, start=1):
            output.append(str(i) + '. @' + member)

    wont_show = ref.child('wont-show').get()
    if wont_show is not None:
        output.append('\n_Não poderão comparecer_')
        for i, member in enumerate(wont_show, start=1):
            output.append(str(i) + '. @' + member)

    return '\n'.join(output)
