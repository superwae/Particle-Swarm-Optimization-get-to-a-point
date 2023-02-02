import random
import math 


max_iter=10000
target_location=[69,69]
N=100
minx=-50
maxx=50
w=0.8
c1=0.4
c2=0.8
bestfit=1000
best_sworm_postionx=0
best_sworm_postiony=0
sworm=[]
bool=False
def fintness(x,y):
    x2=[x,y]
    fit=((math.dist(x2, target_location)))
    return fit

class particle:
  def __init__(self, postionx,postiony,volictyx,volictyy):
    self.postionx = postionx
    self.postiony = postiony
    self.bestpostionx = postionx
    self.bestpostiony = postiony
    self.volictyx=volictyx
    self.volictyy=volictyy

  def testfit(self,postionx,postiony):
    if(fintness(postionx,postiony)<fintness(self.bestpostionx,self.bestpostiony)):
        self.bestpostionx=postionx
        self.bestpostiony=postiony



for i in range (N):
    x=random.randint(minx,maxx)
    y=random.randint(minx,maxx)
    volictyx=random.randint(minx,maxx)
    volictyy=random.randint(minx,maxx)
    postion={x,y}
    if bool==False:
        best_sworm_postionx=x
        best_sworm_postiony=y
        bestfit=fintness(x,y)
        bool=True
    fit=fintness(x,y)
    if(fit<bestfit):
        bestfit=fit
        best_sworm_postionx=x
        best_sworm_postiony=y
    sworm.append(particle(x,y,volictyx,volictyy))

for i in range (max_iter):
    for particles in sworm:
        r1=random.randint(0,2)
        r2=random.randint(0,2)
        particles.volictyx=(w*particles.volictyx)+c1*r1*(particles.bestpostionx-particles.postionx)+c2*r2*(best_sworm_postionx-particles.postionx)
        particles.volictyy=(w*particles.volictyy)+c1*r1*(particles.bestpostiony-particles.postiony)+c2*r2*(best_sworm_postionx-particles.postiony)
        if( particles.volictyx>maxx):
             particles.volictyx=maxx
        elif(particles.volictyx<minx):
             particles.volictyx=minx
        elif(particles.volictyy<minx):
             particles.volictyy=minx
        elif(particles.volictyy<minx):
             particles.volictyy=minx
        particles.postionx=particles.postionx+particles.volictyx
        particles.postiony=particles.postiony+particles.volictyy

        if(fintness(particles.postionx,particles.postiony)<bestfit):
            bestfit=fintness(particles.postionx,particles.postiony)
            best_sworm_postionx=particles.postionx
            best_sworm_postiony=particles.postiony

        if(fintness(particles.postionx,particles.postiony)<fintness(particles.bestpostionx,particles.bestpostiony)):
           particles.bestpostionx =particles.postionx
           particles.bestpostiony =particles.postiony
           
for particles in sworm:
    print(particles.postionx,particles.postiony)
print(best_sworm_postionx,best_sworm_postiony)
