# Reading and Grouping

### Creating our Data Dictionary

With Power Query [ready](https://www.excelcampus.com/install-power-query/) we begin by loading the college scorecard data dictionary.

1. First we load the file from workbook

   ![From workbook](img/FromWorkbook.png)

2. Select the dictionary sheet and then `edit`

   ![Select dictionary sheet](img/SelectDicSheet.png)
   
3. When selecting and then removing other columns the order that we select them will become the new order as shown below

   ![Respect ordering](img/RemoveOtherColumns.gif)
   
4. Next we remove `null` values from the `VARIABLE NAME` column by unselecting from the filter dropdown.

    ![Remove null](img/RemoveNull.png)
	
5. We want to `Load To` which allows us to only create a connection to this file and store the steps we just built. It will not load the file into our workbook. This allows us to reference external data without first loading it into our spreadsheet. Note this if choosing to send this workbook to others.

	![Load to](img/LoadTo.png)
	
6. We finalize the `load to` by selecting `Only Create Connection`

	![Only connect](img/CreateConnection.png)
	
### Aggregate 4 Year Graduation Rates by Year

1. Next we need to reference the yearly CSV files so we are going to reference a folder instead of a single file so that we can pull them in simultaneously. Select edit in the next window as we did previously so we can refine our results.

	![Load files](img/2-FromFolder.png)
	
2. We have other files we do not want to reference that we can simply exclude with a filter by extension.

	![Filter CSV](img/2-OnlyCSV.png)

3. Then we combine our files. It is important to note that if you ever add another CSV file Power Query will try to reference this file. You can better future proof this by adding a filter for file name contains "_small" perhaps.

	![Combine files](img/2-CombineFiles.png)
	
4. Sometimes Power Query properly assesses headers. Sometimes you have to tell Power Query to use the first row as a header as shown below.  

	![Ensure headers](img/2-EnsureHeaders.png)
	
5. Remember above when we created our data dictionary? We now want to 'find and replace' all of the current columns with the developer friendly column.  This step is a bit tricky.  It is important that in the previous phase you made sure that `VARIABLE NAME` was the first column followed by `developer-friendly name` as we are finding the first and replacing with the second in this step. Additionally, the query names spelling must be exact since we are referencing it explicitly. Power Query should have simply pulled the sheet name `data_dictionary` as the query name. Though if you renamed the query name be sure to use it in place here.  The quickest way I have found to do this is temporarily change any columns name and then overwrite the relevant portion of the formula as shown below.

	![Batch rename](img/2-BatchRename.gif)

6. If Power Query did not correctly assess headers then you will have all of the other headers from the otehr files. We only promoted the first row of the first file which left all of the other files headers.  While filtering those out be sure to remove blanks, `null` values, and cases of `PrivacySuppressed`

	![Filter stuff](img/2-RemoveBlanksetc.png)
	
7. We can get our years from the file names by extraction. On the Transform tab select Extract > Range

	![Extract](img/2-ExtractRange.png)

8. Range is 0-indexed and we want to extract the 4 letters after `MERGED`

	![set range](img/2-SpecifyRange.png)
	
9. Rename the year column if you would like by double clicking to change.

	![rename year](img/2-RenameYear.gif)
	
10. The text type for our graduation rates is text. We will not be able to average by year until we convert it to a decimal. The boxed icons below show the data type for each column. You can change the type by clicking on these icons and selecting `Decimal Numbers`. If you have a lot to change it is faster to select all of the relevant columns and change the Data Type to decimal on the `Transform` tab. Note: The data type transformation will fail if you left any text such as `PrivacySuppressed` in the data.

	![convert type](img/2-TextType.png)
	
11. Select the newly renamed `year` column and on the Transform tab click `Group By`. In the Group By window select the `Advanced` radio button and mirror the following. Note: Your groupby will fail if you forgot to specify a decimal data type or you did not remove some text rows from the data.

	![group by](img/2-Grouby.png)

12. Let's show the difference of our grouped result by selecting the female and then male columns (in that order) and then on the `Add Column` tab in the `Standard` dropdown select `Subtract`. 
	
13. We can then sort by year and on the Home tab select `Load to` to drop the final produce in our workbook. If a new years data were to come out we can simply add it to this directly and refresh this query to add the average to this table.  Pretty neat!

### Group By Custom Function

What if we wanted to find out how many times Females have a higher graduation rate than Males?

1. Start by duplicating our query.

	![duplicate](img/3-Duplicate.png)

2. In the applied steps start from the bottom up and remove all of the steps until you return the state to where blanks, nulls, and PrivacySuppressed was filtered out. 

	![remove steps](img/3-AppliedSteps.png)
	
3. Add a new column that subtracts Male from Female like we did earlier. 

	![add subtract col](img/3-Subtract.gif)
	
4. On the `Add Column` tab select `Custom Column` the formula we need to use is `if [Subtraction] > 0 then "Female Higher" else if [Subtraction] < 0 then "Male Higher" else "Identical"` Note: If you changed the name of the `Subtraction` column in the previous step be sure to use that name instead.

	![add formula](img/3-CustomFormula.png)
	
5. With only the new `Custom` column selected select `Group By` on the `Transform` tab. Leave the default settings and click `OK`

6. From here `Close and Load` to create your table with counts!
