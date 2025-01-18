# create a program whch reads data from an excel file and publish the data to Azure Purview
# first create a function which reads the Fully qualified name nfrom Azure Purview and writ it to the excel file
# second add a column for the Asset description to the excel file
# third create a function to load back the excel fille with the newly added descriptions 
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.purview.scanning import PurviewScanningClient

# Function to read Fully Qualified Name from Azure Purview and write it to the excel file
def write_fqn_to_excel(excel_file_path, sheet_name):
    # Set up the client and credentials
    credential = DefaultAzureCredential()
    client = PurviewScanningClient(endpoint="https://<your-purview-account-name>.scan.purview.azure.com", credential=credential)

    # Read the excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Assuming the excel has a column 'DataSource' with names to match in Purview
    fqn_list = []
    for data_source in df['DataSource']:
        # Get the asset from Purview (replace with actual method to retrieve FQN)
        fqn = client.get_asset_fully_qualified_name(data_source)
        fqn_list.append(fqn)

    # Add the FQN list as a new column to the dataframe
    df['FullyQualifiedName'] = fqn_list

    # Write the updated dataframe back to the excel file
    df.to_excel(excel_file_path, sheet_name=sheet_name, index=False)

# Function to add a column for the Asset description to the excel file
def add_description_column(excel_file_path, sheet_name):
    # Read the excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Add a new column for Asset Description with empty values
    df['AssetDescription'] = ''

    # Write the updated dataframe back to the excel file
    df.to_excel(excel_file_path, sheet_name=sheet_name, index=False)

# Function to load back the excel file with the newly added descriptions
def load_updated_excel(excel_file_path, sheet_name):
    # Read the updated excel file
    updated_df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    
    # Process the updated dataframe as needed
    # For example, publish the updated descriptions back to Azure Purview
    # (This part of the code will depend on how you want to use the updated data)

# Example usage - please create a main function here to call the functions above.
def main():
    # Assuming the functions above are defined in the same script
    # Call the functions here as per their definitions
    excel_file = './/Excel2Purview.xlsx'
    sheet = 'Input'
    write_fqn_to_excel(excel_file, sheet)
    add_description_column(excel_file, sheet)
    load_updated_excel(excel_file, sheet)

if __name__ == "__main__":
    main()
