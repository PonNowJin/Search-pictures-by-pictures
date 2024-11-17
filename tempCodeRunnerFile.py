if __name__ == '__main__':
    # data files
    unformal_file = "unformal.csv"
    fnormal_file = "fnormal.csv"

    unformal_data = pd.read_csv(unformal_file, sep=',', header=None, skiprows=1)
    fnormal_file = pd.read_csv(fnormal_file, sep=',', header=None, skiprows=1)

    precision_unf = []
    precision_fno = []
    for i in range(1):
        unf_data = EuclideanDistance(unformal_data, i)
        fno_data = EuclideanDistance(fnormal_file, i)
    
        precision_unf.append(precision(unf_data, 10))
        precision_fno.append(precision(fno_data, 10))

    prec_unf_mean = np.mean(precision_unf)
    prec_fno_mean = np.mean(precision_fno)
    
    print('prec_unf: ', prec_unf_mean)
    print('prec_fno:', prec_fno_mean)