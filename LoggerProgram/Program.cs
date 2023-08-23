using Newtonsoft.Json;

namespace ConsoleLogger
{

  // Log structure with message and time
  class LogEntry
  {
    public DateTime Timestamp { get; set; }
    public required string Message { get; set; }
  }

  // logger program
  class Logger
  {
    // global variables for log list and file path
    private static List<LogEntry> current_logs = new List<LogEntry>();
    private static string file_Path = System.IO.Directory.GetCurrentDirectory() + "/LogsJson.json";

    // main 
    static void Main(string[] args)
    {

      // initial function calls
      LoadLogsFromFile();
      Log_Options();

    }
    
    // fuction to display all program options
    static void Log_Options()
    {
      // while loop to continue operations while the user wises to use the program
      while (true)
      {
        // Options provided to the user
        Console.WriteLine("\nWelcome to a string based logging program!");
        Console.WriteLine("Please make a selection:");
        Console.WriteLine("1.) Add entry.\n" +
                          "2.) List all Logs .\n" +
                          "3.) List saved Logs.\n" +
                          "4.) Get Log(s).\n" +
                          "5.) Save logs to file.\n" +
                          "6.) Exit.");

        // Try/Catch to insure the user only enters the desirable values
        try
        {
          Log_Selection(Convert.ToInt32(Console.ReadLine()));
        }
        catch (FormatException err)
        {
          Console.WriteLine("You have entered something that does not work.\n Error: " + err.Message);
          Console.WriteLine();
        }   
      }
          
      
    }
    
    // switch function to call corresponding function based on users input
    static void Log_Selection(int option_selected)
    {
      switch (option_selected)
      {
        case 1: Add_Log_Entry();
          break;
        case 2: List_All_Logs();
          break;
        case 3: List_Saved_Logs();
          break;
        case 4: Get_Log();
          break;
        case 5: Save_Logs();
          break;
        case 6: Environment.Exit(0);
          break;

        default: 
          Console.WriteLine("Selection not supported.\n");
          break;
      }
    }

    // add log to list function
    static void Add_Log_Entry()
    {
      Console.WriteLine("\nAdd Log.\n" +
                        "Nomerally this would be fed a string from something else, but for this exercise please enter something.");
      var log_message = Console.ReadLine();
      // checks if the user entered something
      if(!string.IsNullOrWhiteSpace(log_message))
      {
        // creates new log and adds to the log list
        LogEntry new_log = new LogEntry
        {
          Timestamp = DateTime.Now,
          Message = log_message
        };
        current_logs.Add(new_log);
      }
    }

    // Funtion Lists all logs currently in the list while program is running
    static void List_All_Logs()
    {
      Console.WriteLine("\nList All Logs.");
      foreach (var log in current_logs)
      {
        Console.WriteLine($"{log.Message} : {log.Timestamp}");
      }   
    }

    // Function lists all logs in the json file only
    static void List_Saved_Logs()
    {
      Console.WriteLine("\nList Saved Logs.");
      string text = File.ReadAllText(file_Path);
      List<LogEntry> output = JsonConvert.DeserializeObject<List<LogEntry>>(text);
      foreach(var log in output)
      {
        Console.WriteLine($"{log.Message} : {log.Timestamp}");
      }
    }

    // fuction requests input from user and searches all current logs saved/unsaved for matches
    static void Get_Log()
    {
      Console.WriteLine($"\nGetting Log(s).\n" +
                        "Enter search criteria");
      
      string search_value = Console.ReadLine();
      // checks that the user has entered something
      if(!string.IsNullOrWhiteSpace(search_value))
      {
        // loops through all logs
        foreach(var log in current_logs)
        {
          if(log.Message.Contains(search_value))
          {
            Console.WriteLine($"Log found: {log.Message} : {log.Timestamp}");
          }
        }
      }
    }

    // function saves all logs as json from the log list overwritting the json file
    static void Save_Logs()
    {
      Console.WriteLine("\nSaving Logs.");
      string json = JsonConvert.SerializeObject(current_logs, Formatting.Indented);
      File.WriteAllText(file_Path, json);
      Console.WriteLine("Save complete.");
    }

    // loads all logs from the json file getting ready to add addtional logs
    static void LoadLogsFromFile()
    {
      // try/catch file check/creation
      try
      {
        if(!File.Exists(file_Path))
        {
          File.Create(file_Path);
        }
      }
      catch (Exception err)
      {
        Console.WriteLine($"File Creation Error : {err.Message}");
      }

      // try/catch file exists and is not empty before coping over logs
      try
      {
        if (File.Exists(file_Path) && !string.IsNullOrEmpty(File.ReadAllText(file_Path)))
        {
          string json = File.ReadAllText(file_Path);
          current_logs = JsonConvert.DeserializeObject<List<LogEntry>>(json);
        }
      }
      catch (NullReferenceException err)
      {
        Console.WriteLine($"File not found! {err.Message}");
      }
    }
  }
}