# Law-School-Analyzer
 Analyze Public ABA Disclosure Data. The school defaults to the University of Hawaii but any school(s) can be selected.

 Built by Matthew Stubenberg. If you are interested in helping to maintain/improve the analyzer please let me know.

## Data
Data is obtained from Access Lex at https://analytix.accesslex.org/download-dataset

## Updating Data
Download new CSVs from the link above. Right now Access Lex adds "DataSet" to the front of each filename. Remove this and replace the old CSVs in the data folder. Access Lex will change column names from time to time so make sure to update the column names in the code.

## ToDo
- This could be coded more efficiently. More commenting is needed.
- I keep getting the warning below that needs to be handled.

    `DataFrame is highly fragmented.  This is usually the result of calling frame.insert many times, which has poor performance.  Consider joining all columns at once using pd.concat(axis=1) instead. To get a de-fragmented frame, use newframe = frame.copy()`
- Add the ability to switch between line and bar charts.
- The school names in the dropdown are always cut off. Not sure if there's a way to make the selected schools go onto a new line so the full school name is visible.
- Better labelling of axises.
- Better legend labelling. i.e. JDA should say "JD Advantage" Bar EMP should say "Bar Passage Required Employment"
- Build some models that look at all the schools to determine outliers.
- Add US News Rankings.