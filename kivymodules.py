"""
import kivy

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Stedap company limited")


if __name__ == "__main__":
    MyApp().run()

"""

import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s version %s" %(i.key, i.version) for i in installed_packages])
for m in installed_packages_list:
    print(m)

