import pygame

class Modules:
    a = """
    SSSSSSSSSSS
    aaaaaaSSSSS
    aaaaSaaaaSa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaSS
    aaaaaaaaSSS
    SSSSSSSSSSS
    """

    b = """
    SSSSSSSSSSS
    aSSaaaaaaSa
    aaaaaaaaaSa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    SSSSSaaaaSS
    """

    c = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaSSaaaaa
    aaSSSSaaaaa
    SSSSSSaaaSa
    SSSSSSSSSSS
    """

    d = """
    SSSSSSSSSSS
    aSaaaSSaaaa
    aaaaaSSaaaa
    aaaaaSSaaaa
    aaaaaSSaaaa
    aaaaaaaaaaa
    aSaaaaaaaaa
    SSSSsSSSSSS
    """
    
    e = """
    SSSSSSSSSSS
    aaaaaaSaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaSaSSaaa
    aaSSaaaaSaa
    aSaaaaaaSaa
    SSaaaaaaSSS
    """
    f = """
    SSSSSSSSSSS
    aSaaaaSaSaa
    aSaaaaSaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    SaSSaaSSaSS
    """
    g = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaSaa
    aaaaaaaaSaa
    aaaaSaSaSaa
    SSSSSaSaSSS
    """
    h = """
    SSSSSSSSSSS
    aSSSSSSSSaa
    aSSaaSSSSaa
    aSaaaaSSSaa
    aSaaaaSSaaa
    aaaSSaaaaaa
    aaaSSaaaaaa
    SSSSSSSSSSS
    """
    i = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaSSaaSaaaa
    aaSSaaSSSaa
    SSSSaaSSSSS
    """
    j = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    SSSaaSSSaSS
    """
    k = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaSSSaaa
    aaaSaSSSaaa
    aaSSaSSSSaa
    SSSSSSSSSSS
    """
    l = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaSaaSSaaaa
    SSSaaaSSSSS
    """
    m = """
    SSSSSSSSSSSSS
    aaaaaaaaaaaaa
    aaaaaaaaaaaaa
    aaaaSaaaaaaaa
    aaaSSaaaaaaaa
    aaaSSaaaaaSaa
    aSSSSaaaaaSSa
    SSSSSaaaaSSSS
    """
    n = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaSaaaaa
    aaaaSSaaaaa
    aaaSSSSaaSa
    SSSSSSSaaSS
    """
    o = """
    SSSSSSSSSSS
    aaaaaaaaSa
    aaaaaaaaSaa
    aaaaaaaaaaa
    aaaaaSaaaaa
    aaaaSSaaaaa
    aaSaSSaaaaa
    SSSSSSaaSSS
    """
    p = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaSSSaaaa
    aaaaSaaaaaa
    aaaSSaaaaSa
    SSSSSaaSSSS
    """
    q = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaSaaaaaa
    aaSSSaaaSaa
    SSSSSaaaSSS
    """
    r = """
    SSSSSSSSSSS
    aSaaaaaSaaa
    aSaaaaaaaaa
    aSaaaaaaaaa
    aaaaSaaaaaa
    aaaSaaaaaaa
    aaaSaaaSaaa
    aSSSaaaSSSS
    """

    s = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaSaaaaaaa
    aaaSaaaSaaa
    aSSSaaaSSaa
    SSSSaaaSSSS
    """
    t = """
    SSSSSSSSSSS
    aaaaaaaaSaa
    aaaaaaaaSaa
    aaaaaaaaaaa
    aaaaSaaaaaa
    aaaaaaaaaaa
    aaaaaaSaaaa
    SSaaSSSSSSS
    """

    u = """
    SSSSSSSSSSS
    aSaaaaSaaaa
    aSaaaaSaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaSaaaSaa
    SSSSSSSSSSS
    """
    
    v = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    SSSaSSSaaSS
    """
    
    w = """
    SSSSSSSSSSS
    aaaaSSaaaaa
    aaaaSSaaaaa
    aaaaSaaaaaS
    aaaaaaaSaaS
    aaaaaaaSSSa
    aaaaaSSSSSa
    SSSSSSSSSSS
    """
    
    x = """
    SSSSSSSSSSS
    aaSaaaaSaaa
    aaSaaaaSaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaSaaaa
    aaaaaSSaaaa
    SSSSSSSSSSS
    """
    
    y = """
    SSSSSSSSSSS
    aSaaaaaaaaa
    aSaaaaaaaaa
    aaaaaaaaaaa
    aaaaaSaaaaa
    aaaaaSaaaaa
    aaaSSSaaaaa
    SSSSSSSSSSS
    """
    
    z = """
    SSSSSSSSSSS
    aSaaSaaSaaa
    aSaaSaaSaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    SSSSSSSSSSS
    """

    Tutorial = """
    SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSSSSSaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSSSSSaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSaaaSaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSaaaSaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaSaaaaaaaaaaaaaaaaaaaaaaaaaaSaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaSaaaSaaaaaaaaaaaaaaaaaaaaaaaaaaSaaaaaaaSSSSSSSSSSSSSSSSSS
    SSSSSSSSSSSSSSSSSSSaSSSSSSSSSaaaaSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    """
    
    troll = """
    SSSSSSSSSSS
    aAaaaaaaaaa
    aAaaaaaaaaa
    aAaaaAaaAaa
    aAAsaaaAaaa
    ssaasaaAaaa
    ßsasAasAaaa
    SSSSSSSSSSS
    """
    
    cheat = """
    SSSSSaaaSSS
    aaaaaaaaaaa
    aaaaasaaaaa
    aaaaaaSSaaa
    aaaaaaaaaaa
    aaaaSaaaaaa
    aaaaSaaaaaa
    SSSSSSSSSSS
    """
    
    Test = """
    SSSSSSSSSSS
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaSaaaaaaa
    aaaaSaaaaaa
    aaaaaSaaaaa
    aaaaaaaaSaa
    GGGGGGGGGGG
    """

    Levels = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, t, u, v, w, x, y, z, troll]#, cheat]

#class Level2:
    '''a = """
    SSSSSSSSSSS
    SSSaaaaaaSa
    aaaaaaaaaSa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    aaaaaaaaaaa
    GGGGGGGGGGG
    """
    #a = ""
    '''
