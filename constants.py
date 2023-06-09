class Constants:
    
    class SURFACES:
        TRACK = "TRACK"
        GRAVEL = "GRAVEL"
        
        @staticmethod
        def as_tuple():
            return Constants.SURFACES.TRACK, Constants.SURFACES.GRAVEL
        
    class ACTIONS:
        X_UP_Y_UP = "X_UP_Y_UP"
        X_UP_Y_DOWN = "X_UP_Y_DOWN"
        X_UP_Y_STAY = "X_UP_Y_STAY"
        X_DOWN_Y_UP = "X_DOWN_Y_UP"
        X_DOWN_Y_DOWN = "X_DOWN_Y_DOWN"
        X_DOWN_Y_STAY = "X_DOWN_Y_STAY"
        X_STAY_Y_UP = "X_STAY_Y_UP"
        X_STAY_Y_DOWN = "X_STAY_Y_DOWN"
        X_STAY_Y_STAY = "X_STAY_Y_STAY"
        
        @staticmethod
        def as_tuple():
            return Constants.ACTIONS.X_UP_Y_UP, Constants.ACTIONS.X_UP_Y_DOWN, Constants.ACTIONS.X_UP_Y_STAY, Constants.ACTIONS.X_DOWN_Y_UP, Constants.ACTIONS.X_DOWN_Y_DOWN, Constants.ACTIONS.X_DOWN_Y_STAY, Constants.ACTIONS.X_STAY_Y_UP, Constants.ACTIONS.X_STAY_Y_DOWN, Constants.ACTIONS.X_STAY_Y_STAY