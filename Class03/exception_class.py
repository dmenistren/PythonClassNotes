def div():
    try:
        a = int(input("number 01: "))
        b = int(input("number 02: "))
        print(f"output is {str(a/b)}")
        return str(a/b)
    except ZeroDivisionError:
        print("value is infinity")

    except Exception as err:
        import traceback
        print(traceback.format_exc())
        print(err)

    else:
        print("hello")

    finally:
        print("Completed")


print(div())
