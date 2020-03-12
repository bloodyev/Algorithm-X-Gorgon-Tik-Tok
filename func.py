    def m135436d(s):
        indexOf  = s.find("?")
        indexOf2 = s.find("#")
        if indexOf == -1: return None
        if indexOf2 == -1: return s[indexOf+1:]
        if indexOf2 < indexOf: return None
        return s[indexOf+1:indexOf2]

    def m64150a(bArr):
        n = len(bArr)
        cArr = ["\00"] * (n * 2)
        for i in range(n):
            b = bArr[i] & 255
            i2 = i * 2
            cArr[i2] = f54574a[b >> 4]
            cArr[i2 + 1] = f54574a[b & 15]
        return "".join(cArr)

    def m64151a(s):
        n = len(s)
        bArr = [0] * (n//2)
        for i in range(0,n,2):
            bArr[i//2] = (int(s[i], 16) << 4) + int(s[i+1], 16)
        return bArr

    b = m135436d(s)
    str3 = None
    a = None if b is None or len(b) == 0 else m64163a(b)
    str4 = None
    str5 = None
    for k,v in m.items():
        if k.upper() == "X-SS-STUB":
            str3 = v
        if k.upper() == "COOKIE":
            str6 = v
            if str6 is not None:
                str4 = m64163a(str6)
                c = m135437e(str6)
                if c != None and len(c) > 0:
                    str5 = m64163a(c)



    if a is None or len(a) == 0: a = "00000000000000000000000000000000"
    if str3 is None or len(str3) == 0: str3 = "00000000000000000000000000000000"
    if str4 is None or len(str4) == 0: str4 = "00000000000000000000000000000000"
    if str5 is None or len(str5) == 0: str5 = "00000000000000000000000000000000"
    sb = a + str3 + str4 + str5
    a2 = m64150a(leviathan(sec, bytearray(m64151a(sb))))
    return {"X-Khronos" : str(sec), "X-Gorgon" : a2}
