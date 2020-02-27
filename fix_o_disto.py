__author__ = "Ratul Chowdhury, Harvard Medical School"

import sys,os
import numpy as np

name_a3m=input('Enter a3m alignment filename (add .a3m extension)': )
name_npz=input('Enter the npz file you obtained from executing networks/predict.py (add .npz extension)': )


a3m_open=open(str(name_a3m))
a3m_read=a3m_open.readlines()

ref_seq=str(a3m_read[1]).strip()


a=()

for i in range(len(ref_seq)):
    if str(ref_seq[i])=='-':
        a+=(int(i),)

npz=np.load(str(name_npz))

dis=np.delete(npz['dist'],a,0)
dis=np.delete(dis,a,1)

thet=np.delete(npz['theta'],a,0)
thet=np.delete(thet,a,1)

omega=np.delete(npz['omega'],a,0)
omega=np.delete(omega,a,1)

phi=np.delete(npz['phi'],a,0)
phi=np.delete(phi,a,1)


#temp={'dist':dis, 'theta':thet, 'omega':omega, 'phi':phi}

np.savez('corrected_'+str(name_npz)[:-4]+'.npz', dist=dis, theta=thet, omega=omega, phi=phi)

#print(type(temp))




