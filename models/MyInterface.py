import pickle

class MyInterface:
    def __init__(self, name):
        """
        Args:
            name (string): name of the Machine Learning model
        """
        self.name = name
        self.model = None
        """
        Model: The best trained model
        """
        self.temp_model = None
        """
        Temp_Model: Variable that stores the model temporarily during training
        """
        self.ds = None
        """
        Dataset: dataset used in project
        """
        self.model_path = './save_model/'
        """
        Path: Path to the folder where the model is saved
        """
        self.parameter_list = {}
        """
        Dict: A dictionary containing the model's hyperparameter search parameters
        """
        self.train_time = None
        """
        Model training time
        """
        self.interface_time = None
        """
        Model's inference (prediction) time
        """
        
        
        #Model configuration
        self.verbose = False
        """
        A boolean flag that prints the results during training
        """
    
    def create_model(self):
        """
        definition and the library of the model
        """
        pass
    
    def fit(self):
        """
        Tranining model
        """
        pass
    
    def predict(self, X):
        if self.model is None:
            print("ERROR: select a model to execute the program")
            return
        X = X.reshape(-1,1)
        predictions = self.model.predict(X)
        return predictions
 
    def evaluate(self):
        return self.predict(self.ds.X_train, train = True)
    
    def save_model(self):
        """
        Save the model into a file in self.save_model directory
        Returns:
            boolean: 1 if saving operating is successful, 0 otherwise
        """
        if self.model is None:
            print("ERROR: The model must be available before saving it.")
            return
        with open(self.model_path + self.name + '_model.pkl', 'wb') as f:
            pickle.dump(self.model, f)
        return 1
    
    def load_model(self):
        try:
            with open(self.model_path + self.name + '_model.pkl', 'rb') as f:
                self.model = pickle.load(f)
            return 1
        except FileNotFoundError:
            print("ERROR: The specified model file does not exist.")
            return 0
        
    def hyperparametrization(self):
        """
        Search the best parameter configuration
        """
        pass
    
    def train(self, p, X_test):
        self.p = p 
        self.create_model()
        train_model = self.fit()
        predictions = self.predict(X_test)
        return  predictions, train_model