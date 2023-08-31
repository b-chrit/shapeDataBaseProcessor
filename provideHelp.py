def showHelp():
    print("LOAD <FILENAME>: loads a database of shapes; the database is a multi-set; the <FILENAME> represents a <FILE> in the file system.")
    print("TOSET: converts the current multi-set in memory to a set (removes duplicates).")
    print("SAVE <FILENAME> : saves the current in-memory database to a <FILE>.")
    print("PRINT: prints the current in-memory database to the standard output.")
    print("SUMMARY: prints the summary of the in-memory database to the standard output.")
    print("DETAILS: prints the detailed information of the in-memory database objects to the standard output.")
    print("QUIT: terminate the program.")