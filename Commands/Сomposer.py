from Commands import ConfigData
from Commands.Aliases import *
from Commands.Aliases import aliasForComplexCommands
from Commands.Aliases import aliasForSimpleCommands


class CommandTypes:
    SIMPLE = 0
    COMPLEX = 1


class ParseCommandException(Exception):
    @staticmethod
    def getErrorMsg():
        return "Во время разбора команды произошла ошибка: "


class Composer:
    def __init__(self):
        """ init """

    def getCommandsList(self, unParsedCmd: str, data: ConfigData):
        try:
            cmdInfo = Composer._parseCmd(unParsedCmd)
            if cmdInfo['type'] is CommandTypes.SIMPLE and cmdInfo['cmd'] in aliasForSimpleCommands:
                cmd = aliasForSimpleCommands[cmdInfo['cmd']]
                commandsList = globals()[cmd]().run(data)
            elif cmdInfo['type'] is CommandTypes.COMPLEX and cmdInfo['cmd'] in aliasForComplexCommands:
                cmd = aliasForComplexCommands[cmdInfo['cmd']]
                commandsList = globals()[cmd]().run()
            else:
                commandsList = globals()[cmdInfo['cmd']]().run()
                # print()
                # if cmd in self.simple_command:
                #     self.simple_command[cmd].run()
                # elif cmd in self.complex_command:
                #     self.complex_command[cmd].run()
            return commandsList
        except ParseCommandException:
            print(ParseCommandException.getErrorMsg() + unParsedCmd)
        except KeyError:
            print("Не удалось определить команду: " + unParsedCmd)

    @staticmethod
    def _parseCmd(cmd: str) -> dict:
        if not cmd:
            raise ParseCommandException()

        splitCmd = cmd.split('=')
        if len(splitCmd) == 1:
            return {
                'type': CommandTypes.SIMPLE,
                'cmd': splitCmd[0]
            }
        elif len(splitCmd) == 2:
            return {
                'type': CommandTypes.COMPLEX,
                'cmd': splitCmd[0],
                'values': splitCmd[1].split(',')
            }
        else:
            raise ParseCommandException()
