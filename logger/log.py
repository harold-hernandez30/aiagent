import traceback

def stacktrace_log(prefix, input):
    print("====================")
    # trace = traceback.format_exc()
    print(f"{prefix}: {input}")

    # if (trace is not None):
    #     print(f'\n\n Stacktrace: \n {trace}')