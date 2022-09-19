# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if query.ind in self.elems.keys():
                for e in reversed(self.elems[query.ind]):
                    print(e, end=' ')
            print()
        else:
            elem_hash = self._hash_func(query.s)
            hash_exists = self.elems.get(elem_hash) != None
            if query.type == 'find':
                if hash_exists:
                    self.write_search_result(query.s in self.elems[elem_hash])
                else:
                    self.write_search_result(False)
            elif query.type == 'add':
                if hash_exists:
                    if query.s not in self.elems[elem_hash]:
                        self.elems[elem_hash].append(query.s)
                else:
                    self.elems[elem_hash] = [query.s]
            else:
                if hash_exists:
                    for i in range(0, len(self.elems[elem_hash])):
                        if self.elems[elem_hash][i] == query.s:
                            self.elems[elem_hash].pop(i)
                            break
                    if len(self.elems[elem_hash]) == 0:
                        del self.elems[elem_hash]

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
