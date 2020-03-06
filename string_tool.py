
def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

