import pygame as P;z=Q=64;r,m,W=range(z),range(-1,2),P.display.set_mode([z*8]*2);S=[[(Q:=hash(Q**.5))%2 for C in r]for R in r]
def U(x,y,G):N=-G[x][y];[[N:=N+G[(x+R)%z][(y+C)%z]for C in m]for R in m];return (N==3)|(N==2)&G[x][y]==1
while Q:[Q:=0 if E.type==P.QUIT else Q for E in P.event.get()];[[P.draw.rect(W,[z]*3 if S[R][C]==1 else [0]*3,P.Rect(R*8,C*8,8,8))for C in r]for R in r];S=[[U(x,y,S)for y in r]for x in r];P.display.update()
P.quit()