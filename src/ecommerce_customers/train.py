from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(ecom):
    X=ecom[["Length of Membership","Time on App","Time on Website","Avg. Session Length"]]
    y=ecom ["Yearly Amount Spent"]
    X_train, X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=101)

    lm=LinearRegression()
    lm.fit(X_train,y_train)

    return X,y,X_train,X_test,y_train,y_test,lm

    

