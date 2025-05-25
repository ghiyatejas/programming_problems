class Solution:
    def generate(self, numRows):
        try:
            # Base cases for numRows = 0, 1 and 2
            if numRows == 0:
                return None

            triangle = []
            if numRows >= 1:
                triangle.append([1])
            if numRows >= 2:
                triangle.append([1, 1])

            for i in range(2, numRows):
                row = [1]
                prev_row = triangle[i - 1]

                # Add adjacent elements from the previous row
                for j in range(1, len(prev_row)):
                    row.append(prev_row[j - 1] + prev_row[j])

                # Add the trailing 1 at the end of the current row
                row.append(1)

                # Append the row to the triangle
                triangle.append(row)

            return triangle

        except Exception as ex:
            print(str(ex))
            return None
