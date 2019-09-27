# e911 Provisioning Scripts
gateway provisioning code for VOIP e911 system


#Pre-processing scripts:
merge_by_buildings.py performs a left join between on the Building Number field between 2 sets of data from Facilities. The left set is a list of all buildings with location info, and the right is a list of each room in the building. The result is a list of every room in all buildings, with the full building location information for each. This allows a simpler algorithm to generate the ERLs by room.

split_address.py reformats the addresses to separate columns for the numeric part of the address and the actual name of the street, as these are listed separately in the West e911 gateway provisioning worksheet.


#ERL generation
e911.py reads in the processed building/room information, and outputs a spreadsheet,  "e911 provisioning.xslx" designed to closely mirror the format required on the provisioning worksheets. To ensure no data type mismatch, the data from the output sheet must be copied and pasted BY VALUE in to the provisioning worksheet. 



#Using the scripts

To run the scripts, place the source excel sheets in to the same working directory as the script files. Modify the file name in the script to reflect the name of the file to be processed. Navigate to the folder from the terminal, and run "_script_name_.py". 

NOTES:
-Ensure source data has headers (column names) that are only one row. 
-Ensure column names match between datasets; sometimes corresponding columns may have different names, like "Building Number" and "Building No." - this will cause the script to fail. 
-



