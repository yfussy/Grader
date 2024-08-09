def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:] + ':' + ('0'+str(s))[-2:]

def to_sec(h,m,s):
    return h*3600 + m*60 + s
def to_hms(s):
   h = s//3600
   s -= h*3600
   m = s//60
   s -= m*60
   return h,m,s
def diff(h1,m1,s1,h2,m2,s2):
    tdiff = to_sec(h2,m2,s2) - to_sec(h1,m1,s1)
    h, m, s = to_hms(tdiff)
    return h,m,s
def main():
    hmsStart = str2hms(input())
    hmsEnd = str2hms(input())
    diffSec = diff(hmsStart[0], hmsStart[1], hmsStart[2], hmsEnd[0], hmsEnd[1], hmsEnd[2])
    diffHMS = to_hms(to_sec(diffSec[0], diffSec[1], diffSec[2]))
    diffStr = hms2str(diffHMS[0], diffHMS[1], diffHMS[2])
    print(diffStr)

exec(input()) # DON'T remove this line