from functions.get_file_contents import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print("")

def test() -> None:
    result = get_file_content("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '../' directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'main.py':")
    print(result)


if __name__ == "__main__":
    test()
