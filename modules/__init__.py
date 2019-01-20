##
##
##
##
##

## Imports

from ..core.options import Section, Option

##

main_menu = Section("SE Toolkit GUI")
main_menu.append(Option("Social-Engineering Attacks", lambda x: print("Hello1")))
main_menu.append(Option("Penetration Testing (Fast-Track)", lambda x: print("Hello2")))
main_menu.append(Option("Third Party Modules", lambda x: print("Hello3")))
main_menu.append(Option("Update the Social-Engineer Toolkit", lambda x: print("Hello4")))
main_menu.append(Option("Update SET configuration", lambda x: print("Hello5")))
main_menu.append(Option("Help, Credits, and About", lambda x: print("Hello6")))