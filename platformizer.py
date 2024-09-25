from platform import platform, machine, system, processor, version, python_version, python_implementation, python_version_tuple

print(machine())
print(version())
print(system())
print(processor())
print(platform(False))
print(python_version())
print(python_implementation())
for i in python_version_tuple():
    print(i)
