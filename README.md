# Bug-Analysis-Metrics-Reporting-and-their-Graphical-Representation

This project involves the analysis of multiple datasets to understand bug distributions, module performance and efficiency. We performed various tasks including plotting histograms, Pareto charts, and calculating various metrics. The results are reported in a document containing the code, plots, and insights.


## Tech Stack

- Programming Language: Python 
- Libraries: Pandas, Matplotlib


## Datasets

- **Dataset 1:** Contains information about Task type, severity, urgency and prority.
- **Dataset 2:** Contains information about bugs, their reporting, and resolution times.
- **Dataset 3:** Contains detailed module and bug information, including reporting and resolution times, assignees, status and bug types.

## Tasks Descriptions

- **Task 1: Plot Histograms**
Plot histograms for each dataset and each component/module in dataset 3 to understand the distribution of minor, major, critical bugs, etc.

- **Task 2: Plot Pareto Charts**
For dataset 3, plot Pareto charts to identify which modules have the most reported bugs.

- **Task 3: Calculate Percent Delinquent Fixes (PDF)**
For datasets 2 and 3, calculate the percent delinquent fixes month-wise. A fix is considered delinquent if it is not closed within 4 hours of reporting.

- **Task 4: Plot Time Run Chart for PDF**
Plot a time run chart for the PDF values calculated in Task 3.

- **Task 5: Plot Control Chart for PDF**
Plot a control chart for the PDF values with upper and lower control limits set at (mean + 2SD) and (mean - 2SD) respectively. Highlight points that are out of these limits.

- **Task 6: Calculate Schedule Estimation Accuracy**
Calculate the schedule estimation accuracy for the bugs in dataset 2.

- **Task 7: Calculate Fix Response Time**
Find the fix response time for dataset 2 and 3. For dataset 3, also calculate module-wise values.

- **Task 8: Plot BMI Values**
For datasets 2 and 3, plot the Bug Management Index (BMI) values month-wise.

- **Task 9: Plot Pareto Diagram for Assignees**
For dataset 3, plot a Pareto diagram to identify which assignee has been given the most bugs to resolve.

- **Task 10: Plot Pareto Diagram for Unresolved Bugs**
For dataset 3, plot a Pareto diagram to identify which assignee has been given the most bugs to resolve that are still not closed.

- **Task 11: Calculate Proportion and Percentage of Actual Defects**
Let column B in dataset 3 represent customer reported problems. Identify the actual defects and calculate their proportion and percentage from all reported problems for the whole dataset and module-wise.

- **Task 12: Reporting**
Compile all the metric values, graphs, and insights from tasks 1 to 11 into a Word or PDF document.
## Feedback

If you have any feedback, please reach out to me via my email, javariashabbir2431@gmail.com 

