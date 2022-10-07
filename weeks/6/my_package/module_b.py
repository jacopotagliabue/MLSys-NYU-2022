print("you're importing module_b")

from my_package.subpackage.submodule_c import function_c


def function_b():
    print("I'm in module B!")
    print("And now I'm going to call a function from submodule_c")
    function_c()
