class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """


if __name__ == "__main__":
    # Let's solve LRU Cache:
    # https://leetcode.com/problems/lru-cache
    commands = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    returned_values = [None]
    lru_cache = LRUCache(capacity=args[0][0])
    for i in range(1, len(commands)):
        command = commands[i]
        arg_list = args[i]
        if command == "put":
            returned_values.append(lru_cache.put(*arg_list))
        if command == "get":
            returned_values.append(lru_cache.get(*arg_list))
    assert returned_values == [None, None, None, 1, None, -1, None, -1, 3, 4]
