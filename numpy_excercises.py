{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "8a6e0752",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "fae00ef0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#how many negative numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "9a8a17a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y =a[a<0]\n",
    "len(y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "21c72b6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#how many positive numbers are there?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "9956eaa8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = a[a>0]\n",
    "len(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "5a190e44",
   "metadata": {},
   "outputs": [],
   "source": [
    "#How many even positive numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "20fd45f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ans = a[np.where((a > 0) & (a % 2 ==0))]\n",
    "len(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "09c2fc19",
   "metadata": {},
   "outputs": [],
   "source": [
    "#If you were to add 3 to each data point, how many positive numbers would there be?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "515d9ba0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zz = a + 3\n",
    "wow = zz[zz>0]\n",
    "len(wow)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "6b7aeac5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#If you squared each number, what would the new mean and stddev be?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "88444960",
   "metadata": {},
   "outputs": [],
   "source": [
    "sq = a * a \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "ceab7217",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74.0"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sq.mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "d007e4de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "144.0243035046516"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sq.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "569115a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#center the data set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "3ac55a5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "13554645",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1,   7,   9,  20,  -5,  -4,  -3,  -3,  -3,  -9,   0, -10])"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c = a - 3\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "f721b572",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Find z-score for each datapoint in array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "89e3bf6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,\n",
       "       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,\n",
       "        0.        , -1.24034735])"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z = ((a - 3)/8.06225774829855)\n",
    "z"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "b04b5063",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "# Life w/o numpy to life with numpy\n",
    "\n",
    "## Setup 1\n",
    "a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "96b08645",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list\n",
    "\n",
    "\n",
    "def sum_of_a():\n",
    "    return a.sum()\n",
    "sum_of_a()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "0041ad70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make a variable named min_of_a to hold the minimum of all the numbers in the above list\n",
    "def min_of_a():\n",
    "    return a.min()\n",
    "min_of_a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "cd8a7d8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make a variable named max_of_a to hold the max number of all the numbers in the above list\n",
    "def max_of_a():\n",
    "    return a.max()\n",
    "max_of_a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "b1368762",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#make a variable named mean_of_a to hold the average of all the numbers in the above list\n",
    "def mean_of_a():\n",
    "    return a.mean()\n",
    "mean_of_a()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "bd5d0c1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3628800"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together\n",
    "def product_of_a():\n",
    "    return np.product(a)\n",
    "product_of_a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "00d93fad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1,   4,   9,  16,  25,  36,  49,  64,  81, 100])"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]\n",
    "def squares_of_a():\n",
    "    return np.square(a)\n",
    "squares_of_a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "cd9cf5d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 3, 5, 7, 9])"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make a variable named odds_in_a. It should hold only the odd numbers\n",
    "def odds_in_a():\n",
    "    return a[a % 2 != 0]\n",
    "odds_in_a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "a758b7ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 2,  4,  6,  8, 10])"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make a variable named evens_in_a. It should hold only the evens.\n",
    "def evens_in_a():\n",
    "    return a[a % 2 == 0]\n",
    "evens_in_a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "a32012ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...\n",
    "## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.\n",
    "b = np.array([\n",
    "    [3, 4, 5],\n",
    "    [6, 7, 8]\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "1c5d1000",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the \"b\" variable is a numpy array**\n",
    "def sum_b():\n",
    "    sum_of_b = b.sum()\n",
    "    return sum_of_b\n",
    "sum_b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "584b5105",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - refactor the following to use numpy. \n",
    "def min_b():\n",
    "    b.min()\n",
    "    return min_of_b\n",
    "min_b()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "a5c76614",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.\n",
    "def max_b():\n",
    "    b.max()\n",
    "    return max_of_b\n",
    "max_b()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "fd9a2ddc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 4 - refactor the following using numpy to find the mean of b\n",
    "def mean_b():\n",
    "    b.mean()\n",
    "    return mean_of_b\n",
    "mean_b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "472cce7d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20160"
      ]
     },
     "execution_count": 181,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.\n",
    "def product_b():\n",
    "    product_of_b = np.product(b)\n",
    "    return product_of_b\n",
    "product_b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "6a508795",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 9, 16, 25],\n",
       "       [36, 49, 64]])"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 6 - refactor the following to use numpy to find the list of squares \n",
    "def square_b():\n",
    "    square_of_b = np.square(b)\n",
    "    return square_of_b\n",
    "square_b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "17dbc15e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 5, 7])"
      ]
     },
     "execution_count": 186,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 7 - refactor using numpy to determine the odds_in_b\n",
    "def odds_b():\n",
    "    return b[b % 2 != 0]\n",
    "  \n",
    "odds_b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "827082d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4, 6, 8])"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 8 - refactor the following to use numpy to filter only the even numbers\n",
    "def evens_b():\n",
    "    return b[b % 2 == 0]\n",
    "evens_b()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "863a7fba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 9 - print out the shape of the array b.\n",
    "np.shape(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc62fd07",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 10 - transpose the array b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "c438b189",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., 0., 0., 0.]])"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# # Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)\n",
    "b = np.zeros((1,6))\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "b10b4c22",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use python's built in functionality/operators to determine the following:\n",
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list\n",
    "\n",
    "# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list\n",
    "\n",
    "# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list\n",
    "\n",
    "# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list\n",
    "\n",
    "# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together\n",
    "\n",
    "# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]\n",
    "\n",
    "# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers\n",
    "\n",
    "# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.\n",
    "\n",
    "## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...\n",
    "## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.\n",
    "b = [\n",
    "    [3, 4, 5],\n",
    "    [6, 7, 8]\n",
    "]\n",
    "\n",
    "# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the \"b\" variable is a numpy array**\n",
    "sum_of_b = 0\n",
    "for row in b:\n",
    "    sum_of_b += sum(row)\n",
    "\n",
    "# Exercise 2 - refactor the following to use numpy. \n",
    "min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  \n",
    "\n",
    "# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.\n",
    "max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])\n",
    "\n",
    "\n",
    "# Exercise 4 - refactor the following using numpy to find the mean of b\n",
    "mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))\n",
    "\n",
    "# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.\n",
    "product_of_b = 1\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        product_of_b *= number\n",
    "\n",
    "# Exercise 6 - refactor the following to use numpy to find the list of squares \n",
    "squares_of_b = []\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        squares_of_b.append(number**2)\n",
    "\n",
    "\n",
    "# Exercise 7 - refactor using numpy to determine the odds_in_b\n",
    "odds_in_b = []\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        if(number % 2 != 0):\n",
    "            odds_in_b.append(number)\n",
    "\n",
    "\n",
    "# Exercise 8 - refactor the following to use numpy to filter only the even numbers\n",
    "evens_in_b = []\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        if(number % 2 == 0):\n",
    "            evens_in_b.append(number)\n",
    "\n",
    "# Exercise 9 - print out the shape of the array b.\n",
    "\n",
    "# Exercise 10 - transpose the array b.\n",
    "\n",
    "# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)\n",
    "\n",
    "# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)\n",
    "\n",
    "## Setup 3\n",
    "c = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "# HINT, you'll first need to make sure that the \"c\" variable is a numpy array prior to using numpy array methods.\n",
    "# Exercise 1 - Find the min, max, sum, and product of c.\n",
    "\n",
    "# Exercise 2 - Determine the standard deviation of c.\n",
    "\n",
    "# Exercise 3 - Determine the variance of c.\n",
    "\n",
    "# Exercise 4 - Print out the shape of the array c\n",
    "\n",
    "# Exercise 5 - Transpose c and print out transposed result.\n",
    "\n",
    "# Exercise 6 - Get the dot product of the array c with c. \n",
    "\n",
    "# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261\n",
    "\n",
    "# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.\n",
    "\n",
    "\n",
    "## Setup 4\n",
    "d = [\n",
    "    [90, 30, 45, 0, 120, 180],\n",
    "    [45, -90, -30, 270, 90, 0],\n",
    "    [60, 45, -45, 90, -45, 180]\n",
    "]\n",
    "\n",
    "# Exercise 1 - Find the sine of all the numbers in d\n",
    "\n",
    "# Exercise 2 - Find the cosine of all the numbers in d\n",
    "\n",
    "# Exercise 3 - Find the tangent of all the numbers in d\n",
    "\n",
    "# Exercise 4 - Find all the negative numbers in d\n",
    "\n",
    "# Exercise 5 - Find all the positive numbers in d\n",
    "\n",
    "# Exercise 6 - Return an array of only the unique numbers in d.\n",
    "\n",
    "# Exercise 7 - Determine how many unique numbers there are in d.\n",
    "\n",
    "# Exercise 8 - Print out the shape of d.\n",
    "\n",
    "# Exercise 9 - Transpose and then print out the shape of d.\n",
    "\n",
    "# Exercise 10 - Reshape d into an array of 9 x 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76d79f59",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "709ea5f3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
