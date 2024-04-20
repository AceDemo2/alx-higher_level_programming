#!/usr/bin/python3
# List all classes in the built-in exceptions module
import builtins

# Filter and print exception classes
exception_classes = [cls for cls in dir(builtins) if cls.endswith("Error") or cls.endswith("Exception")]
print(exception_classes)

