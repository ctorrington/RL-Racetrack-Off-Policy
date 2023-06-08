class Constants:
    
    class SURFACES:
        TRACK = "TRACK"
        GRAVEL = "GRAVEL"
        
        @staticmethod
        def as_tuple():
            return Constants.SURFACES.TRACK, Constants.SURFACES.GRAVEL