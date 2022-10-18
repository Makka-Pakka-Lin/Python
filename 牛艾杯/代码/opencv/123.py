import numpy as np
def fun(t1):
    for i in range(t1.shape[1]):
        t2 = t1[:,i]
        if np.count_nonzero(np.isnan(t2))!= 0:
            t3 = t2[t2 ==t2]
            t2[np.isnan(t2)] = t3.mean()
    return t1
if __name__ == "__main__":
    t1 =  np.arange(12).reshape(3,4).astype("float")
    t1[1,:2] = np.nan
    print(t1)
    print('*'*100)
    fun(t1)
    print(t1)