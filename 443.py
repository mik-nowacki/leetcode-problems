class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 1
            read += 1
            while read < n and char == chars[read]:
                count += 1
                read += 1
            
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return len(chars[:write])
    