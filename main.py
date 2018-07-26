from Commands.ConfigData import ConfigData
from Commands.Сomposer import Composer

# for get argv use: sys.argv

if __name__ == "__main__":
    composer = Composer()
    data = ConfigData('dt', 'prod')
    cmdList = composer.getCommandsList('get_last_log', data)
    print(cmdList)
    # print(dispatcher.dispatchCommands({}, 'get_last_log'))
