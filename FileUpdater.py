import DataSaver


def fileupdater():

    # Startup Task
    DataSaver.savevatstatusdata()
    # Task to run every two minutes
    DataSaver.savelocalvatdata()


if __name__ == "__main__":
    fileupdater()


