def collectAnalyticsData():
  # Get the list of apps that are installed on the iPhone.
  appList = getInstalledApps()

  # For each app in the list, collect the following data:
  #   - The name of the app
  #   - The number of times the app has been opened
  #   - The amount of time that the app has been used

  for app in appList:
    name = app.getName()
    opens = app.getOpens()
    time = app.getTimeUsed()

    # Save the data to a file.
    with open("analytics_data.txt", "a") as file:
      file.write(f"{name}, {opens}, {time}\n")

END ALGORITHM
