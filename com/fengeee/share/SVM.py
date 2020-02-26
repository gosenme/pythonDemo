from sklearn import svm
import DC

if __name__ == '__main__':
    stock = '002841.SZ'
    dc = DC.data_collect(stock, '2017-01-19', '2019-09-23')
    train = dc.data_train
    target = dc.data_target
    test_case = [dc.test_case]
    model = svm.SVC(gamma='auto')
    model.fit(train, target)
    ans2 = model.predict(test_case)
    print(ans2[0])
