class AllOne:

    def __init__(self):
        self.key2cnt = {}
        self.cnt2keys = collections.defaultdict(set)
        self.min_cnt = 0
        self.max_cnt = 0

    def inc(self, key: str) -> None:
        if key in self.key2cnt:
            old_cnt = self.key2cnt[key]
            self.cnt2keys[old_cnt].remove(key)
            if not self.cnt2keys[old_cnt]:
                del self.cnt2keys[old_cnt]
                if old_cnt == self.min_cnt:
                    self.min_cnt += 1
        else:
            self.min_cnt = 1

        new_cnt = old_cnt + 1 if key in self.key2cnt else 1
        self.key2cnt[key] = new_cnt
        self.cnt2keys[new_cnt].add(key)
        self.max_cnt = max(self.max_cnt, new_cnt)

    def dec(self, key: str) -> None:
        old_cnt = self.key2cnt[key]
        self.cnt2keys[old_cnt].remove(key)
        if not self.cnt2keys[old_cnt]:
            del self.cnt2keys[old_cnt]
            if old_cnt == self.min_cnt and len(self.cnt2keys) > 0:
                self.min_cnt = min(self.cnt2keys.keys())
        
        new_cnt = old_cnt - 1
        if new_cnt > 0:
            self.key2cnt[key] = new_cnt
            self.cnt2keys[new_cnt].add(key)
        else:
            del self.key2cnt[key]

    def getMaxKey(self) -> str:
        return next(iter(self.cnt2keys[self.max_cnt])) if self.cnt2keys else ""

    def getMinKey(self) -> str:
        return next(iter(self.cnt2keys[self.min_cnt])) if self.cnt2keys else ""