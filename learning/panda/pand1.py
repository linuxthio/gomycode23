{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a8832ecf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b4a5905a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=pd.read_csv('../datas/Mall_Customers.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cb87364c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Annual Income (k$)</th>\n",
       "      <th>Spending Score (1-100)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>100.500000</td>\n",
       "      <td>38.850000</td>\n",
       "      <td>60.560000</td>\n",
       "      <td>50.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>57.879185</td>\n",
       "      <td>13.969007</td>\n",
       "      <td>26.264721</td>\n",
       "      <td>25.823522</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>50.750000</td>\n",
       "      <td>28.750000</td>\n",
       "      <td>41.500000</td>\n",
       "      <td>34.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>100.500000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>61.500000</td>\n",
       "      <td>50.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>150.250000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>78.000000</td>\n",
       "      <td>73.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>200.000000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>137.000000</td>\n",
       "      <td>99.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       CustomerID         Age  Annual Income (k$)  Spending Score (1-100)\n",
       "count  200.000000  200.000000          200.000000              200.000000\n",
       "mean   100.500000   38.850000           60.560000               50.200000\n",
       "std     57.879185   13.969007           26.264721               25.823522\n",
       "min      1.000000   18.000000           15.000000                1.000000\n",
       "25%     50.750000   28.750000           41.500000               34.750000\n",
       "50%    100.500000   36.000000           61.500000               50.000000\n",
       "75%    150.250000   49.000000           78.000000               73.000000\n",
       "max    200.000000   70.000000          137.000000               99.000000"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ef8601f",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
