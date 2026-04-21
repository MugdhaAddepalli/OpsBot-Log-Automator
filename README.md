# **OpsBot – Log File Security Alert Automator**

## **Overview**

OpsBot is a Python-based automation tool designed to assist IT Operations teams in monitoring server logs efficiently. It processes raw log files, filters out non-essential information, and generates a concise security alert report highlighting critical issues such as failed login attempts and system errors.

This tool eliminates the need for manual log inspection, reducing analysis time and improving response speed to potential security threats.

---

## **Business Problem**

An IT Operations team handles server logs containing thousands of entries daily. Manually scanning these logs for suspicious activities, such as failed login attempts or system errors, is time-consuming and inefficient.

OpsBot automates this process by identifying and extracting only the relevant security-related information.

---

## **Features**

* Reads large log files efficiently line by line
* Filters out non-critical "INFO" messages
* Detects important log entries:

  * CRITICAL
  * ERROR
  * FAILED LOGIN
* Counts occurrences of each error type
* Generates a structured security alert report
* Automatically names output files with the current date
* Displays file size to confirm successful report generation

---

## **Technologies Used**

* Python 3
* Built-in Modules:

  * `re` (Regular Expressions for pattern matching)
  * `os` (File handling and automation)
  * `datetime` (Timestamp-based file naming)

---

## **Project Structure**

```
OpsBot/
│
├── server.log                      # Input log file
├── opsbot.py                       # Main Python script
├── security_alert_YYYY-MM-DD.txt   # Generated output file

```

---

## **How It Works**

1. **File Parsing**
   The script reads the log file line by line to handle large datasets efficiently.

2. **Pattern Matching**
   Each line is checked for specific keywords:

   * CRITICAL
   * ERROR
   * FAILED LOGIN

3. **Data Structuring**
   A dictionary is used to count the frequency of each error type.

4. **Report Generation**
   Filtered log entries are written into a new file along with a summary section.

5. **Automation Check**
   The script uses the `os` module to display the size of the generated report file.

---

## **How to Run**

1. Ensure Python 3 is installed
2. Place `server.log` in the same directory as the script
3. Run the script:

```
python opsbot.py
```

4. The output file will be generated automatically in the same directory

---

## **Use Cases**

* IT infrastructure monitoring
* Security log analysis
* Detecting unauthorized access attempts
* Reducing manual log inspection effort

---

## **Future Enhancements**

* Real-time log monitoring
* Email or SMS alert integration
* Dashboard visualization of log statistics
* Integration with intrusion detection systems
* AI-based anomaly detection

---

## **Conclusion**

OpsBot provides a simple yet effective solution for automating log analysis. By focusing only on critical events, it helps teams respond faster to potential threats while significantly reducing manual workload.
