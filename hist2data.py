import numpy as np
from ROOT import TFile, TH1F, TH2F, TTree, gDirectory

def th12arr(th1f):
    nbins=th1f.GetXaxis().GetNbins() 
    binc=np.array([th1f.GetXaxis().GetBinCenter(i+1) for i in range(nbins)])
    y=np.array([th1f.GetBinContent(i+1) for i in range(nbins)])
    return [binc, y]
def h2sum(h2name,norm=1):
    h2=gDirectory.Get(h2name)
    nbins_x=h2.GetXaxis().GetNbins() 
    nbins_y=h2.GetYaxis().GetNbins() 
    x_binc=np.array([h2.GetXaxis().GetBinCenter(i+1) for i in range(nbins_x)])
    y_binc=np.array([h2.GetYaxis().GetBinCenter(i+1) for i in range(nbins_y)])

    sum_y=[]

    for i in range(nbins_x):
        s=0
        for j in range(nbins_y):
            val=h2.GetBinContent(i+1,j+1)
            s+=val
        sum_y.append(s)
    sum_y=np.array(sum_y)/norm
    return [x_binc, sum_y]
