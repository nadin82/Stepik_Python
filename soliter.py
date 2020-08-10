{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 0 8 5 5 3\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# Poszukiwanie min w liście\n",
    "a = [int(i) for i in input().split()]\n",
    "m = a[0]\n",
    "for x in a:\n",
    "    if m > x:\n",
    "        m = x\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 4 4\n",
      "1 1 \n",
      "2 2\n",
      "3 2\n",
      "4 4\n",
      "*21.\n",
      "3*2.\n",
      "2*31\n",
      "112*\n",
      "..11\n"
     ]
    }
   ],
   "source": [
    "# Saper\n",
    "n, m, k = (int(i) for i in input().split()) # odczytywanie wielkości pól i liczby min\n",
    "a = [[0 for j in range(m)] for i in range(n)]  # wypełnienie pola zerami\n",
    "for i in range(k):\n",
    "    row, col = (int(i) - 1 for i in input().split())\n",
    "    a[row][col] = -1 #umieszczanie min\n",
    "for i in range(n):\n",
    "    for j in range(m):\n",
    "        if a[i][j] == 0: #nie ma miny w tej kratce, więc liczymy liczbę min wokół\n",
    "            for di in range(-1,2):\n",
    "                for dj in range(-1,2):\n",
    "                    ai=i+di\n",
    "                    aj=j+dj\n",
    "                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:\n",
    "                        a[i][j] += 1\n",
    "# wyświetlenie wynników\n",
    "for i in range(n):\n",
    "    for j in range(m):\n",
    "        if a[i][j] == -1:\n",
    "            print('*', end='')\n",
    "        elif a[i][j] == 0:\n",
    "            print('.', end='')\n",
    "        else:\n",
    "            print(a[i][j], end='')   \n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
