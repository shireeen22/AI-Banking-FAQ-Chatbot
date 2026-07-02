import pandas as pd
import numpy as np



def get_analysis():
    try:
        # define df...
        df = pd.read_csv("feedback.csv")
        # total no. of questions...
        queries = len(df) # total rows
        # extract total no. of helpful feedbacks...
        helpful = len(df[df["feedback"] == "Helpful"])

        # extract total no. of not helful feedbacks...
        not_helpful = len(df[df["feedback"] == "Not Helpful"])

        return {
            "Total queries": queries,
            "Helpful Feedbacks": helpful,
            "Not helpful Feedbacks": not_helpful
        }

    except:
        # if df is empty...
        return {
            "Total queries":0,
            "Helpful Feedbacks":0,
            "Not helpful Feedbacks":0
        }
    
