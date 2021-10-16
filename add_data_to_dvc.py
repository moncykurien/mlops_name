import os
from glob import glob

data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]

for dir in data_dirs:
    files = glob(dir+r"/*.csv")
    for filePath in files:
        print({filePath})
        os.system(f"dvc add {filePath}")
print("\n#### All files added to dvc ####")