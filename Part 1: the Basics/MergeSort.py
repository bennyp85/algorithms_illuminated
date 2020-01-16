if __name__ == '__main__':


    def MergeSort(array):
        n = len(array)
        if n == 0 or n == 1:
            return array
        else:
            array1 = MergeSort(array[:int(n / 2)])
            array2 = MergeSort(array[int(n / 2):])
            return Merge(array1, array2)


    def Merge(array1, array2):
        array3 = []
        i, j = 0, 0

        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                array3.append(array1[i])
                i += 1
            else:
                array3.append(array2[j])
                j += 1

        if i < len(array1):
            array3.extend(array1[i:])
        if j < len(array2):
            array3.extend(array2[j:])
        return array3

print(MergeSort([5, 4, 3, 2, 1]))
