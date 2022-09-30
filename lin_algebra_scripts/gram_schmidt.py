import numpy as np
def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():  
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)

test = np.array([[0.0, 0.0, 1.0, 1.0], [1.0, 0.0, -1.0, 0.0], [1.0, 2.0, 0.0, 2.0], [2.0, 1.0, 1.0, 1.0]])
print(test)
print(gram_schmidt(test))
