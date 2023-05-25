from models.MyInterface import MyInterface

class MyProbabilistic(MyInterface):
    def __init__(self, name):
        """
        Constructor of the Model Probabilistic class
        Args:
        name: name of the model
        """
        super().__init__(name)
        self.is_probabilistic = True
        """
        Boolean: Determines if the model is probabilistic
        """
    def predict(self, X):
        """
        X: Input samples to predict
        """
        if self.model is None:
            print("ERROR: the model needs to be trained before predict")
            return
        predictions = self.model.predict(X)
        return predictions
    
    def evaluate(self):
        """
        Evaluate the model on the training set ds.X_train_array
        """
        if self.verbose:
            print("Evaluate")
        predicted_mean, predicted_std = self.predict(self.ds.X_train_array)
        return predicted_mean, predicted_std