import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


df = pd.read_csv("students.csv")
print(df)