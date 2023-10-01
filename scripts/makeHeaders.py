import os
import pandas as pd
import sys
sys.path.append('Users/soiledboy/dev/ncuaData/') 
import globalvariables
parent_directory = globalvariables.source_directory 

def makeHeadersData():
    # Specify the source directory path
    source_directory = parent_directory + 'data/merged'

    # Specify the destination directory path
    destination_directory = parent_directory + 'data/mergedHeaders'

    ignored_directory = '.ipynb_checkpoints'
    descriptions = pd.read_csv(parent_directory + "data/AcctDesc/AcctDesc.csv")
    descriptions = descriptions.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

    # Iterate over files in the source directory
    for filename in os.listdir(source_directory):
        # Construct the full file paths
        source_file_path = os.path.join(source_directory, filename)
        if os.path.isdir(source_file_path):
            if filename == ignored_directory:
                continue
        print(source_file_path)
        destination_file_path = os.path.join(destination_directory, f"head{filename}")
        data = pd.read_csv(source_file_path)
        data.columns = data.columns.str.upper()


        # Step 1: Initialize an empty dictionary
        column_mapping = {}

        # Step 2: Iterate over column names
        for column_name in data.columns:
            # Step 3: Search for column name in 'account' column of 'descriptions'
            matching_row = descriptions[descriptions['Account'] == column_name]

            # Step 4: Retrieve corresponding 'AcctName'
            if not matching_row.empty:
                acct_name = matching_row['AcctName'].iloc[0]

                # Step 5: Add column name mapping to dictionary
                column_mapping[column_name] = acct_name

        # Step 6: Rename columns of 'data' dataframe using the dictionary
        data.rename(columns=column_mapping, inplace=True)

        # Step 7: Create a new dataframe with the renamed columns
        new_dataframe = pd.DataFrame(data)

        # Save the modified content to the destination file
        new_dataframe.to_csv(destination_file_path, index=False)
    print("Done!")


