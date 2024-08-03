def func(dictionary: dict = {}, b_path, c_path, d_path):
    response = {}
    response.update({
        ...
    }) # 写入b,c,d键值对
    return response

print(func({"a": {"d": 123}, "b": 456, "c": 789},b_path = None,c_path = None,d_path = None))