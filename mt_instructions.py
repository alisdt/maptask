
# each of these is just (e.g.) A01 to A10
mt_instructions = {
    k: ["{}{}".format(k,x) for x in range(1,11)]
    for k in ["A", "B"]
}
