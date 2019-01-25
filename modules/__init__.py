##
##
##
##
##

## Imports

from ..core.windows import OptionWindow

##

class MainWindow(OptionWindow):

    @OptionWindow.method_as_option("1. Hang This Window")
    @OptionWindow.hangable_method
    def test1(self, *args, **kwargs):
        self.is_hanging = True

    @OptionWindow.method_as_option("2. Unhang Other Window")
    @OptionWindow.hangable_method
    def test2(self, *args, **kwargs):
        main_menu2.is_hanging = False

    @OptionWindow.method_as_option("3. Is Other Window Hanging?")
    @OptionWindow.hangable_method
    def test3(self, *args, **kwargs):
        print(main_menu2.is_hanging)

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)

        main_menu2.is_hanging = False

class MainWindow2(OptionWindow):

    @OptionWindow.method_as_option("1. Hang This Window")
    @OptionWindow.hangable_method
    def test1(self, *args, **kwargs):
        self.is_hanging = True

    @OptionWindow.method_as_option("2. Unhang Other Window")
    @OptionWindow.hangable_method
    def test2(self, *args, **kwargs):
        main_menu.is_hanging = False

    @OptionWindow.method_as_option("3. Is Other Window Hanging?")
    @OptionWindow.hangable_method
    def test3(self, *args, **kwargs):
        print(main_menu.is_hanging)

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)

        main_menu.is_hanging = False

##

main_menu = MainWindow("SE Toolkit GUI 1", None)
main_menu2 = MainWindow2("SE Toolkit GUI 2", main_menu)