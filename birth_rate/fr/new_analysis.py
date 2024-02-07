{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "30244d64",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/azm/anaconda3/lib/python3.11/site-packages/openpyxl/styles/stylesheet.py:226: UserWarning: Workbook contains no default style, apply openpyxl's default\n",
      "  warn(\"Workbook contains no default style, apply openpyxl's default\")\n"
     ]
    },
    {
     "data": {
      "image/png": "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dPPmzZqZmamlpaWanp6uN954ow4cOFALCgrUsiz95JNP1LIsPXz4sM6YMUOjo6M1IiJC69evr06nU1esWKGqqrm5ufrhhx+qqqplWXrs2DFds2aNulwuHTVqlKd/RESENmnSRBs1aqTTpk3TadOm6dSpU1VE9KabbtJp06bpyJEjNSIiQv/2t795nvdrr72mV111led5f/jhh36f9/jx4zU9PV07duyo9913n1qWFfSs3PMaOXKkNmnSRFXVM6/09HT97LPP9M4779SePXtWOKvf/OY3GhUVpQcPHrzkeUVEROgtt9yi1113nWde5c3KfZz07t1b27dvf0nHSVmzKm++gR5bZc3K/dyXLFmiycnJ2rdv36CPrbJm5XA4NCkpSW+99VadNm2abtu2rcJjq6xZuefVsmVLdTgcIX8e/ny+DRs21BtvvDHoY8vEeeie1zXXXOP3PAzk2OI8rJ7z0M6f8eUdJ+PHj/f789q0WhE+EhISdN++fV61hQsXehJmly5dVEQ0Ly9P8/Ly1OFwaMeOHbVDhw5e36CYmBg9cOCA/utf/9Lo6GhV/elgOXz4sNapU0eXLFmiSUlJqvrTZbKdO3d6DrT9+/drbGysHj16VGfMmOFJyp07d9a6det6ErL7/rt27VLLsnTTpk2e/uvXr9esrCyNiYnRixcveuoiosuXL/d87XK59KuvvvI8771793rWtXDhQo2NjVWHw6GtW7f2et55eXnqdDq1U6dOXs89mFm557VixQrPrNzziomJ0W+//VY///xzTUpKqnBWOTk5KiLavHlzffXVV/Wyyy6rcF7r16/X7OxsffDBBzU5ObnCWbmPkxUrVnhmVdFzL2tW5c030GOrrFm5n/sXX3yhsbGxqqpBH1tlzSoiIkKjo6M9/9hcyrFV1qzc83KHj0uZb3Weh+55rVu3TmNjYzU9PT3oY8vEeeie1y/nG8yxxXlYPeehe152/Iwv7zjJy8vz+/PatFoRPurXr69btmzxqWdkZGhUVJTOmTPH6xvRvn17nTBhgm7fvt2rfuWVV+rf//53nTBhgrZv3163bt2qUVFRWlJSom3atNGpU6dqbGysLlu2TOPj4/U//uM/1OFw6LFjx3TOnDnasmVLz75+97vfaYsWLfSOO+7QyMhI7du3r546dUoty9KdO3fqwIEDNSYmRrdv3+615m3btqnT6dSOHTt6ApWI6NKlSz33yczM1G+//dbzvPfu3atxcXGe7W+99ZZalqXDhg3zOQDdj/nlcw90Vu559enTR9u3b6+q6plXmzZtdPbs2bp37151uVwVzkpV9d5779WUlBStU6eOTp48+ZLmVVhYqL1791aHw1HhrNzPffHixV6zKu+5lzWr8uYb6LFV1qxUVR0Ohz7zzDM+swrm2PI3q4iICE1KStJdu3b5zKusY6usWbnn9eabb/rUQ/E8VP3pH4levXppt27dtEmTJkEfWybOQ/e8/P0fbaDHFudh9Z2Hqvb8jC/vOFFVvz+vTasV4aN79+767LPP+tTvuece7dmzp0ZGRnp9I1avXq2xsbHapEkTFRGdOXOmPv3009q1a1d1OBwaGRmpw4YN04yMDB0xYoSqqi5YsEAdDoe6XC6Njo7Wd955RzMyMlREdMCAARoVFaWzZ8/29CguLtZ+/fpp3bp1tWvXrhodHa116tRREfHcLMvyXIp0W7Jkiebk5Ohrr72maWlp+vLLL6tlWfqnP/2pzOf9/vvv+5wYXbp08byZyt9jduzYoZZlBT2rcePGaVpamoqI3n333fqHP/zBM68FCxao0+nU1NRUtSyrwln9fF5JSUnavXv3gObVoEGDCmflfu7Dhw/3mVVZz72sWZU330CPrbJmdccdd6iIaGRkZJmzCubY+vmsIiMjtV27dvrWW2/5nZW/Y6usWbkfM378eJ9ZheJ56P6/fPebEStzbJk4D93ziomJURHRcePGBX1scR5W/3lY2Z/x5R0nqup3VqbVig+WW7x4saxdu1aef/55r3pBQYEUFxfLhg0b5JVXXpFVq1Z5tn377bcyZ84c2bRpk+dXqdLS0iQ6OlpOnDghIiI333yzPPbYYxIdHS0iIosWLZIdO3bIgAEDpHPnzrJr1y7p16+ftGjRQm699VYZOnSoz9o++ugjef/992X//v1SWloqlmVJy5Yt5aabbpKYmBhJT0+X3Nxcz/1feOEFOX/+vEycOFH27t0r9957r2zevFneeecdue222/w+75ycHCktLZUxY8Z4Pff/+q//ksWLF3s9bztn1blzZ4mLi5MPP/xQiouLvea1fv16+eCDD6RNmzZy9913X9KsKjOvAQMGlDsr93P/y1/+IrfeeqvPrPw997JmVd58y5tXWceWv1k9/fTTsnbtWpk8ebI8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rrhCcnJyKl23s4ep9f58/9WB8AEAAIyqFW84dfvlr0K6lZSUyKFDhypdLy0tlW+//TZserBe1mu6B+sNrEdpaanfx5w8eVLmz59/yfVgHlPTe7Be/z2MqdYXfQwpLCzUQYMGaXR0tDZo0ED/8Ic/aElJiVddRIKuu3v07dtXRSTke7Be1stMQnu9boH+Abtw+qNz1d2D9frvYUqtCB9jx47V3Nxc/fvf/65z587VRo0aae/evXX06NGam5urc+fOVREJul5cXKxjx47V7OxsFZGQ78F6WS8zCe31fvfdd1pYWKh79+5VEdHCwkItLCzU/Px8zc/P148++kgty/LU3dvKqvvbFmg93HqwXv/7Kiws1HXr1hE+TGjYsKGuWrXK8/X333+vnTp10ujoaP344489/3cRbL1Hjx6alZWl//3f/+35hoZyD9bLeplJaK9XRNThcHj+dPjP//vnN3f9l9vKql/KvmpKD9brf18Oh8Pz5+mrU60IH3Xq1NH9+/d71YqKitThcGjnzp11//79nm9EMPXOnTurw+HQNWvWeH1DQ7UH62W9zCS01+t0OjU7O1sXLVqklmXp6tWrdfXq1RobG6sjR47U3/72t15197bbbrvNb93fYwKth1sP1uu/x+rVq3Xu3LnVHj5qxW+7NGvWTJ577jnp1auXVz03N1ecTqe4XC7ZuXOn5y9YBlo/ffq01K9fX9LT0+XgwYNen2cRij1YL+tlJqG93uuvv14OHjwodevW9XpM165dpWfPnnLzzTdLu3btvN5E37VrV2nTpo38+c9/9qn7e0yg9XDrwXr99xD56bOX/NVNqhW/7dKjRw95/fXXfeq33HKLNGvWzOvj5oOpx8XFydChQ6WwsDAserBe1mu6B+sNrMfgwYNl9OjRPo+55557JDo62vNn/X+5rX79+n7r/h4TaD3cerBe/z1EpMy6UdV63cWQH374Qb/66qsy66dOndLVq1cHXXdv++KLL/zWQ60H62W9zCS01+vm7zFATVArXnYBAAChI6K6F2DKmTNnZOHChbJhwwYpKCgQy7IkNTVVOnToIKoqW7durVT92muvlX79+sl7770XFj1YL+tlJqy3pvdgvf573H333RIbG1ut/ybXiisfu3btku7du8uPP/4oN9xwg6Smpoqqyr59+2T16tUi8tMbdJo2bRpU/fjx47Jy5Uo5c+aMxMXFSdeuXUO6B+tlvcyE9db0HqzXf481a9ZIbGysfPLJJ16fjWNarQgfXbt2lbS0NJk3b55ERUV51Rs0aCAiIsePH5dVq1YFVRcRycvLkwMHDsjll18ua9asCekerJf1MhPWW9N7sF7/Pc6fPy/Dhg2To0ePetWN01ogJiZG//nPf5ZZ37lzp8bExARdd29bsmSJ33qo9WC9rJeZsN6a3oP1+u+hqmXWTaoV7/moW7eu7N271+cSk7uuqlK3bt2g6+5tmzZt8lsPtR6sl/UyE9Zb03uwXv89RET27dvnt26UvVkmNE2dOlUTExP12Wef1R07dujRo0e1oKBAR44cqdHR0RoTE6MPPvhg0PUdO3Zo9+7d1bIs7dGjR8j3YL2sl5mw3preg/X67/Hss89q3bp19fHHH6/Wf5drxXs+RESeeeYZeeGFFzzv+hURUVWJi4sTkZ/+2mBl6mlpadK2bVvZsWNHWPRgvayXmbDemt6D9frvMW7cOHnkkUekOtWa8OF24MABKSgoEJGf/spb48aNba2HWw/Wy3qZCeut6T1Yr/8e1anWhQ8AAFC9asVnu4iInD17VtavXy+7du3yqX/66acyc+bMStVFRE6ePCm///3vw6IH62W9pnuwXtZrugfr9d/j3LlzMn/+fJ+6UcG8USTc7N69Wxs1aqSWZanD4dAbbrhBjxw54lUXkaDr7h6ZmZkqIiHfg/WyXmbCemt6D9brv4eqakFBgTocjsr/41oJteLKx6RJk6RVq1Zy/Phx2b17tyQkJMi1114rY8eOlVatWslXX30llmUFXT906JBMmjRJrrzySrEsK+R7sF7Wy0xYb03vwXr99wgZ1Rp9DGnQoIH+4x//8KqNGjVKHQ6HLlu2zCsFBlNv2LCh1qtXT1etWuWVJkO1B+tlvcyE9db0HqzXf49vvvkmJK581IrwER8fr7t27fKpR0ZGampqqq5du9brGxFofcyYMWpZls6fP9/nGxqKPVgv62UmrLem92C9/ntkZmb61KtDrfhtl44dO8pDDz0kgwcP9qknJibKli1bpKioSC5evBhUXUQkNTVVTp8+LefOnfOqh2IP1st6mQnrrek9WK//HmPGjJE333zTp25arXjPx8CBA2XRokV+65GRkXL33XfLzzNYoHURkXHjxklKSopPPRR7sF7Wy0xYb03vwXr995g9e7bfumm14soHAAAIHbXiygcAAAgdhA8AAGAU4QMAABhF+AAAAEYRPgAAgFGEDwAAYBThAwAAGEX4AAAARv0fmKagh7n2n70AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[19.5, 20.1, 20.1, 19.799999999999997, 20.799999999999997, 21.9, 21.7, 21.3, 22.5, 23.1, 21.5, 20.799999999999997, 20.9, 22.4, 22.0, 21.2, 22.2, 23.299999999999997, 22.5, 21.1]\n"
     ]
    }
   ],
   "source": [
    "# FRance birth rate data \n",
    "\n",
    "import pandas as pd \n",
    "import matplotlib.pyplot as mp \n",
    "\n",
    "path = \"/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx\"\n",
    "\n",
    "data = pd.read_excel (path)\n",
    "df  = pd.DataFrame (data)\n",
    "\n",
    "df.rename (columns= {'Label': 'time_period', 'Demography - Rate of birth (number of births per 1,000 inhabitants) - France (including Mayotte since 2014)': 'rate_of_birth'}, inplace =True)\n",
    "\n",
    "tp = df.iloc[3:75, 0].to_list()\n",
    "br = df.iloc[3:75, 1].to_list()\n",
    "\n",
    "#print (tp [0])\n",
    "\n",
    "y_pos = range (len (tp))\n",
    "\n",
    "mp.bar (tp, br)\n",
    "mp.xticks (y_pos, tp, rotation=90)\n",
    "mp.show ()\n",
    "\n",
    "# Quarterwise data\n",
    "\n",
    "qs =[]\n",
    "\n",
    "for i in range (0, 59, 3):\n",
    "    qs.append (sum (br [i:i+2]))\n",
    "\n",
    "print (qs)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7a146fb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/azm/anaconda3/lib/python3.11/site-packages/openpyxl/styles/stylesheet.py:226: UserWarning: Workbook contains no default style, apply openpyxl's default\n",
      "  warn(\"Workbook contains no default style, apply openpyxl's default\")\n"
     ]
    },
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
       "      <th>Label</th>\n",
       "      <th>Demography - Number of live births - Metropolitan France</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>idBank</td>\n",
       "      <td>000436391</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Last update</td>\n",
       "      <td>25/01/2024 12:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Period</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2023-12</td>\n",
       "      <td>52400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2023-11</td>\n",
       "      <td>53400</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Label Demography - Number of live births - Metropolitan France\n",
       "0       idBank                                          000436391      \n",
       "1  Last update                                   25/01/2024 12:00      \n",
       "2       Period                                                NaN      \n",
       "3      2023-12                                              52400      \n",
       "4      2023-11                                              53400      "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "path1 = \"/home/azm/projects/birth_data/birth_rate/fr/live_births_fr.xlsx\"\n",
    "\n",
    "data = pd.read_excel (path1)\n",
    "df  = pd.DataFrame (data)\n",
    "df.head ()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2ff5f431",
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
       "      <th>Label</th>\n",
       "      <th>live_births</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>idBank</td>\n",
       "      <td>000436391</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Last update</td>\n",
       "      <td>25/01/2024 12:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Period</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2023-12</td>\n",
       "      <td>52400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2023-11</td>\n",
       "      <td>53400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>934</th>\n",
       "      <td>1946-05</td>\n",
       "      <td>76636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>935</th>\n",
       "      <td>1946-04</td>\n",
       "      <td>76400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>936</th>\n",
       "      <td>1946-03</td>\n",
       "      <td>78294</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>937</th>\n",
       "      <td>1946-02</td>\n",
       "      <td>65702</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>938</th>\n",
       "      <td>1946-01</td>\n",
       "      <td>64599</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>939 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           Label       live_births\n",
       "0         idBank         000436391\n",
       "1    Last update  25/01/2024 12:00\n",
       "2         Period               NaN\n",
       "3        2023-12             52400\n",
       "4        2023-11             53400\n",
       "..           ...               ...\n",
       "934      1946-05             76636\n",
       "935      1946-04             76400\n",
       "936      1946-03             78294\n",
       "937      1946-02             65702\n",
       "938      1946-01             64599\n",
       "\n",
       "[939 rows x 2 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.rename (columns= {'label' : 'time_period', 'Demography - Number of live births - Metropolitan France': 'live_births'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bf110414",
   "metadata": {},
   "outputs": [],
   "source": [
    "lb = df.iloc[3:75, 1].to_list ()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b85a964a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[52400, 53400, 54900, 52500, 55700, 56100, 54000, 53900, 50500, 52900, 49700, 53700, 55852, 56128, 57402, 56941, 60778, 61415, 58331, 58622, 54233, 56738, 52956, 57168, 61105, 59856, 63639, 61774, 62341, 62690, 57482, 57770, 56886, 57877, 49209, 51190, 55475, 56047, 60873, 59810, 60399, 62593, 58571, 58722, 54317, 57285, 53514, 59058, 59799, 58700, 62636, 61515, 62998, 64579, 59768, 60092, 55652, 56592, 51832, 59866, 59931, 59937, 63588, 61834, 63860, 64823, 60292, 61232, 55364, 56391, 52733, 59752]\n"
     ]
    }
   ],
   "source": [
    "print (lb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0535fad2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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rJecsN7OMQfrZb0tNUdzMsbo3LlzioqKumrbDlvohIaGytPTUyUlJS7xM2fOKDw8vM4+vr6+8vX1dYl169atpZboIigoqM7/8PriTenTGmOxXnLCejvHHKyX9bbUHM3F6XQ2ql2HvRnZx8dHcXFx2r59u0t8+/btSkxMbKNVAQCA9qTDXtGRpLlz5yo9PV3Dhg1TQkKCnnnmGR0/flw/+clP2nppAACgHejQhc5dd92lr776Sk888YSKi4sVGxurN954Q717927rpVl8fX31+OOP13rLrL54U/q0xlisl5yw3s4xB+tlvS01R1txGNOYz2YBAAB0PB32Hh0AAICrodABAAC2RaEDAABsi0IHAADYFoUOAACwLQqddqS6ulqnT5/WmTNnVF1dXSv+5Zdf1tv39OnTtf5KdEMqKyv197//3eVLTq9m586dqqioaHT7lnQtuZLcy1dTciW1n3zVl6vvbuPY+v84DxuP89A9HFtt5Jq/XRMuCgsLzS9/+Uvz29/+1nzxxRcu28rKysyPf/zjWn1+85vfGF9fX+Pj42M8PDyMh4eH8fHxMTfeeKMZNGiQ8fX1teKBgYEmOjraXHfddSYjI8NcunTJzJw50zgcDiPJREdHm4MHD7qM/9xzz5m9e/caY4ypqKgwM2fONJ6ensbhcBhPT08zZ84c880335j33nvP3H777WbQoEFm7Nix5pVXXnEZx9vb2xQVFZl169aZ++67zzz77LPGGGNyc3PNjTfeaKKiosyoUaPc2veXX37ZdOvWrdF9Xn75ZTN06FAj6aq5cjqd5s477zQTJkwwvXr1csmXJONwOMz3vvc98/nnnzd7rmry9cQTTzRbrgoLC01mZqbp3r37NeUqMTHRLFy40PzTP/1To46t+nLVnPlqKFd9+vQxs2fPduu8cjdXDeWL87D9nIceHh7G09PTzJ4923zzzTfGGHNNx1ZrnIfGNM9rfEc8D40xpqioyPTp06dWvDVR6DSjt956y/j4+JibbrrJ9OrVy4SGhpq3337b2l5SUmI8PDxc+vzud78z3t7eRpLZunWr2bNnj/nTn/5kfvaznxlvb2/j6elpJkyYYMLDw82jjz5qEhISTEBAgAkICDC33nqrueOOO8yQIUPM7t27jcPhMF5eXsbhcJjx48ebP/zhD+bixYvmhhtusF5058+fb66//nrz8ssvGw8PD7NhwwbTv39/c9dddxkPDw8zefJkExkZabp162YkmX79+pmhQ4eaoUOHGofDYcLDw60Xr8jISPPkk0+a7t27m+nTp1svRCEhIY3a97feesva98bk63e/+53x8fExd955p3E4HFfN1Zo1a0xERITx9PQ0//7v/25Gjhxp5cvhcBin02kkmaioqCbnatGiRXXmquaHQM08Xl5e15wrHx8f069fPyOpybnaunWrGTNmjJFkxo4dax599NGrHlv15coY02zHVn25evLJJ819991nzd2Y48TdXDXl2OI8bJvz8PDhw8bDw8P07dvXPPzww+add95p8rHVGudhTb6a4zW+o52HNQoLC+uMtyYKnWaUkJBgfv7znxtjjLl8+bJ5+umnTdeuXc2UKVPMQw89ZObMmWMkmYceesh6OJ1OM3z48FoHwo033mhyc3PN+vXrTd++fc3BgwdNz549TWRkpPnTn/5k7rrrLjNx4kTjcDhMfn6+McYYh8NhXnnlFRMSEmImT55svLy8TI8ePYynp6fZsWOHMcaY/v37mzfffNNqf/r0abNr1y7j6+trMjIyjDHGeHl5mQkTJpgf/OAHpnfv3iY7O9s8/vjjxsPDw3Tr1s1MnTrVZGdnmz//+c/Gy8vL/P73v7f2/dlnnzXf+973GrXvkZGRJjY21nh4eDQqX06n0yQlJZl7773XJV/15ery5csmMjLSjB071kyZMsWUlJRY+XI4HObUqVNm8eLFxs/Pr8m5qslX3759rVzV5EuSGTdunMnOzjZz5sy5aq7efPPNBnN16623mnvvvdc4HI4m56omX3PmzDF9+/Y1xpirHlv15WrevHnGx8fHfPbZZ9d8bNWXq5rzatKkSSYuLq5Rx0l9uWoov+4eW5yHbXMefje/vXr1MmPHjm3ysdUa52FzvsZ3tPOw5lHXa1Bro9BpRkFBQebjjz92iW3ZssWqmhMTE40kM2rUKOvh4eFhvch8l7+/vzl27Jg5fPiw8fPzM8Z8e3D6+/ubTz/91Ozfv99069bNeHt7mw8//NAY8+1BfeDAARMQEGCMMaa4uNgsXrzY+u0yISHBBAcHW5V/zUlQVFRkHA6H2bdvnzHGmN27d5t+/fqZn/70pyYkJMRak5eXl/Hz87NOKGOM8fX1NYcOHbL2/ejRo6Zbt26N2ndPT89a+95QHw8PD3PrrbeaYcOGufSpL1enTp0yXbp0Ma+88oq1ppp81ez7J598YgICApqcq5p8RUdHG39/f1NdXW3FJZnt27c3OlcBAQHGw8PDDBkypM5cxcfHu+x7U3JVk68dO3ZYubrasVVfrmJiYowkM2jQILN+/Xpz3XXXNfnYqi9Xxnx7Xu3YscPK1dX2vb5cNZRfd48tzsO2OQ9r8vXee++ZgIAAExkZ2eRjqzXOw+Z8je9o52HNo67XoNZGodOMevToYd5///1a8aioKOPj42PWrFlT6z88Li6uzop34MCB5r//+7/N3LlzTVxcnCkoKDA+Pj7m5ptvNjk5Oebo0aPG19fXBAYGmuXLlxtjjPHw8DC/+tWvTGxsrMtYP//5z81NN91kpk2bZry9vc3kyZPNuXPnjMPhMB9++KGZMmWK8ff3Nx988IHVp6yszEyaNMl4eHhYxZuXl5fp1q2bKSoqstr17NnTfPrpp9a+Hz161HTt2rVR+96jRw+zefPmWvH6+sTFxZm5c+eaDz74wCVeX64uXbpkbr75ZvP444+bgIAA88Ybb1j58vDwMKdPnzZr1qxxyVdTcmWMMX/+85+Np6enufXWW618STKvvvpqo3OVm5trHA6HmTFjRp25ev/992vtu7u5qslXSkqKiYuLM8aYqx5b9eXKGGPuueceExoaarp06WIeffTRJh9b9eWqZt+3bt3qkquG9r2+XDWUX3ePLc7DtjkPjfn2h/dtt91mxowZY/r27dvkY6s1zsOafDXHa3xHOw9r1PUa1NoodJpRUlKSWbp0aa14WlqamThxovH29q71H75z507j7+9vJJmsrCyzZMkS89RTT5nRo0cbDw8P4+3tbWbMmGGioqLMzJkzzaZNm4ynp6cJDw83DofD/OEPfzBRUVFm2rRpRpLx9vY2OTk5LnNUVlaa1NRUExwcbEaPHm38/PxMly5djCTr4XA4rEuUNV555RUTFhZmIiIizNq1a423t7cZOnSoyc3NrXffX3vtNZeTsKF9T0pKMg899JBxOByNytfOnTtNQECA6du3r5F01VwZY8ymTZuMh4eH8fX1NX5+fla+JJk77rjD+Pj4uOTrWnIVExNjnn32WStfDofDLFu2rNG5MsaYxMRE66bEuvoUFha65MvdXGVlZZmIiAgjydx9993mP/7jP656bNWXq+/mq1u3biYpKanJx1Z9uarZ9x//+Me1clXfvteXq4by6+6xxXnYNudhzdWLmpugr+XYao3zsCZfzfEa39HOwxp1nYetjS/1bEZbt27Vu+++q5UrV7rES0pKVFlZqT179uiZZ57RO++847L9008/1Zo1a7Rv3z7r44MRERHy8/PTV199JUkaP368/v3f/11+fn7avXu3tm3bpptvvll33323ioqK9NRTT+ndd9/Vo48+qp/85Cd1ri8vL0+vvfaaPvnkE12+fFkOh0OxsbEaN26c/P39FRkZqf79+1vtf/3rX6uqqkp33HGH7rnnHr3//vt6/vnnFRsbq1tuuaXOfY+JidHly5f1wAMPXHXfm5Ivd3MlSS+++KIKCwt1xx13KCEhQUVFRUpNTdVNN92kqVOnavr06c2Wq4cfflhHjx7VPffco4MHD+oPf/iDfvSjHzUqVzX7/n/+z//R1q1bWyxXCQkJ6tq1q958801VVlZe9di6Wq6uJV81x1Z9uarZ99WrV2vq1Km1clXXvteXq4by21C+OA/bz3kYGRmp0NBQK1eSmnxstdZ52JR82eE8bE8odNAoly9f1rlz5xQUFCSHw9HWy2n3yFfjkavGI1fuIV+NZ+dcebX1AnB1n332mUpKSuRwOBQeHq7evXs3GG9Kn8bGnU5ns8/RGrlqyZw0NEdNvprz/7A18tUWx9zVctXUdbVVrpozv5yH1zYW56F9zsMmadM3zjqZ+v6eQH3xFStWmPDwcOv9VYfDYf3tjG7dulnvUdfEe/bsaW6//XbTs2fPWtvq6+NuvDnn6Nmzp1m5cmWz5Ku+XHXEnNQ3VkP5cvfYmjdvnst9Du1h35tzjqbkyt1jq6PlxC7nYVvntznPQ3ePrfaak6YeW62FQqcV1XdTVl3xJ554wgQFBZmf/exnRpL5/PPPzalTp8xPf/pT64a+jIwMK/7BBx+YpKQkI8kkJSWZDz744Kp93I035xwffPCBeeqpp4zT6TS//OUvrylf9eWqI+akvrGuli93j62uXbsaSS223rbMb1Nz5c6x1dFyYpfzsK3z29znoTvHVnvNybUcW62FQqcZTZkypc5HZGSkiYyMND169DCSam2rK+7v72/i4+PNmDFjXH4T6Nmzp9m6dat5+eWXTVRUlMv8PXv2NI888kid8br6uBtvzjlq8hUfH2/8/Pwala/64vXlqiPmpL6xavb1yny5m6uafA0ePLjOXLXVvjfnHPXlqqHzzd1jq6PlxC7nYVvn193zsDlf49trThrqY4ypN96a+FLPZvTaa6/pm2++kdPpdHmUlJTIw8PD+vTBldsc/+/Gr+/Gq6qqFBkZqa5du7rM8dVXX2nAgAHq37+/SktLa21LTEysM15XH3fjzTlHTb58fHx08eLFRuWrvnh9ueqIOalvrJpjKzIy0iVf7uaqJl+hoaF15qqt9r0556gvVw2db+4eWx0tJ3Y5D9s6v+6eh835Gt9ec9JQH0n1xlsTn7pqRkOGDNHPfvYzzZw5s854XFyc4uLiXL61dsiQIZoyZYqefPJJl/ioUaPUs2dPZWVlKT4+3to2atQoRUVFyRij4uJi7dy50+ozcuRIHT9+XL169dKuXbtcxqqrj7vx5pxDkgYPHqyAgAD5+fm5xOvLV33x+nLVEXNS31hDhgzRAw88oF27dunUqVNWH3dzVTN/QECA3nzzTV2+fLlF1tuW+a0vVzXb6jrf3D22OlpO7HIetnV+3T0Pa7Y1x2t8e81JQ30uXbqk6dOn1zoPWxuFTjP68Y9/rC5duui3v/1tnfEHHnhAt912m44dO+ayrbKyUnv37nWJf/jhh0pOTtY//vEPXbp0Senp6XI4HDpy5Ih1wIwePVoxMTFyOBwqKSnR22+/rfPnz6tr164aM2aMwsPDG+zjbrw55ygpKdEbb7whLy8vHThwQDfddNNV81VfvL5cdcSc1DfWG2+8odOnTyskJETbt2+38uVurmryNWbMGJ09e1apqaktst62zG99uWrofHP32OpoObHLedjW+XX3PGzomHP32GqvOWmoz7vvvitfX99a52Fro9BpRpWVlaqurlaXLl0aFb/atnPnzmnTpk21/sjU0KFDdfnyZf3lL3+p9YfgJk+erFdffbXRfdyNN+ccw4YN05133qmIiIhrzmN9uepoOalvrB49eujWW2/VjBkzFBQUdE25asqx1ZGOufpy1dzHVkfKiZ3Ow7bMr7vnYXMfW+0xJ1frk5aWVus8bG0UOgAAwLa4GbmFTZo0ScXFxY2ON6VPa4zFeskJ6+0cc7Be1ttSc7SZlvo4F77VtWtX8/e//73R8ab0aY2xWC85Yb2dYw7Wy3pbao62whUdAABgWxQ6Lax3797y9vZudLwpfVpjLNZLTlhv55iD9bLelpqjrXAzMgAAsC2+vbwFVFdXy9PT03q+f/9+VVZW6tZbb7X+cuZ34wkJCfLw8HCrT2uM1VrrbU+Vf0d14cIFFRQU6Ic//OE1xdvrWE2Z4y9/+Yv+67/+S06n0/o25cTERMXExOjo0aPas2ePyzctJyYmSlKzxDvaHDExMfrkk0+0e/duFRcXy9PTU3369FFSUpK+/PLLZokHBQU12xzNOZa7c9xyyy06fvy44uLiFBQUpNOnT2vjxo0qLy9Xnz59dOedd7rEL1++rOHDh8sY0+g+7sbb6xyXL1/WpEmTNHjw4Frnbatq0zuEbObzzz83I0aMMJ6enuaHP/yhOXv2rJk0aZKRZD2GDx9uxR0Oh5Fk/Pz8Gt2nNcZqzfUGBweb66+/3nz/+983zz77rDHGmKqqKvPwww+b66+/3khqcrxmW0ZGhpHU7udoaKwaJSUlbn07srvx9jqWO3N8/fXXJjU11TrG+vfvb2JiYky3bt2Mw+EwERERxuFwmG7dulnbnE6ndZw6nc4mxzvaHDVjRUVFuXzrdEREhPHw8DCenp7XHPf09DQBAQFm6NCh7Wqsps6h//dN45GRkeYvf/mL6dmzp7nuuuus4y0kJMSKx8TEmOjoaLf6uBtvr3PExMSYAQMGGF9fX/PWW2/Vee62Ft66akb33Xef/v73v+vRRx/V5s2bdeLECXl6eiosLEyffvqpKioqVFVVpbCwMHl6eurFF19UZmamduzYoR/84AcKDAy8ap/WGKu11rts2TL99re/1fe//32NHj1aOTk5uuuuuxQZGanf/e53mjNnjp544gk5nc4mxdeuXavs7Gz953/+p7744gstXLiwXc/R0Fhr166VJJ0+fVqRkZEuX90gfXv14nvf+57Ln5hvSry9juXOHPfdd58KCwu1YMECTZ8+3aXPbbfdpnfeeUejR4/WG2+8YcXvu+8+7dmzRw6HQ4mJidq4cWOT4h1tDkmaMmWK8vPzNWbMGC1btkwLFy5Uv3799OWXX+rdd9/VyZMn9ctf/lL79u1rUvzxxx/Xbbfdpvfee09PPvmkpk6d2uQ5mnOspszx3nvvyd/fX3v37tWUKVP07rvv6vbbb1dhYaFuueUWeXp66o9//KOqq6t1++23KycnRz/4wQ904cIF+fr66p//+Z/161//usE+7sbb6xw5OTmSpIcfflh79uzRn/70p1rnbqtp0zLLZiIjI83evXuNMcZ89dVXxuFwmB07dljxt99+2/Tu3duK1/TJyckxffv2bVSf1hirtdZ7ww03mEWLFpm+ffsaY4z5+OOPTUxMjAkMDDSvvvqqdfWiqfEZM2aYG264wTz//PPWb/zteY6GxvLx8THBwcGmW7du1pWw4OBg6zdO/b/f1q8Wr9lWX7ytxmruOQIDA01QUFCtq0BOp9P8/ve/N06ns1Z83759Zu/evS7b3I13tDmMMSY0NNQ899xzVvzs2bPGz8/PhIaGmvfff9/k5OSYW265pcnxCxcumNDQULNgwQJzyy23XNMczTlWU+YICgoyH3/8scnJyTE333yz8fLyMh988IEV/9vf/maCgoKsuDHGBAUFmR07dhin02kuXrx41T7uxtvrHDX+9re/1TrmWhufumpGpaWluu666yRJISEh6tKli3r37m3F+/XrpzNnzljxmj5xcXEqLi5uVJ/WGKu11nvq1CmNHDnS+sNS/fr1086dO3X+/HmtX7/e+k28qfGa75bp37+/9X/UnudoaKyLFy8qIiJCjz/+uBwOh1auXKmVK1fK29tb48eP15QpUxoVr9mWmJhYZ7ytxmrOOfz8/PTQQw9p3rx5dZ6nDoej3nhd29yNd7Q5Ll26pICAAOt5165ddenSJV28eFFBQUFKTk7WX//61ybHL1y4oEuXLmncuHH661//ek1zNOdYTZnD29tb33zzjdXn8uXL+uabb+Tj46NvvvlGFRUV8vb2tuKS5OPjo7KyMnl7e6uqquqqfdyNt9c5atTE21Sbllk206tXL7N//37r+SOPPGK++uorK15YWGhCQ0OteE2fF154wYSGhjaqT2uM1Vrr7dOnj1m7dq011nfz2LNnTzNu3DiX38jdjZ86dcp4e3ub733ve7V+s2+PczQ01rBhw0yPHj1q9UlMTDSrVq2qdZ9KffGabQ8//HCd8bYaqznnuPfee82QIUPM5s2ba/WZOHGi8fPzM7fddptL/N577zUxMTGmf//+Jj09vcnxjjaHMcbEx8eb0NBQK7506VITGRlpkpKSzP3332/+/Oc/m9DQ0CbHjTEmKSnJTJs2zTrX28NYTZnj9ttvNykpKebZZ581fn5+ZtiwYWbSpEkmJSXFTJw40YwaNcr07NnTip8/f96kpKSYyMhIEx8fb2bPnn3VPu7G2+sc58+fNxcuXDD//M//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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "mp.bar (tp, lb)\n",
    "mp.xticks (y_pos, tp, rotation=90)\n",
    "mp.show ()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "94bca644",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[160700, 164300, 158400, 156300, 169382, 179134, 171186, 166862, 184600, 186805, 172138, 158276, 172395, 182802, 171610, 169857, 181135, 189092, 175512, 168290, 183456, 190517, 176888, 168876]\n"
     ]
    }
   ],
   "source": [
    "# Quarterwise data for live births\n",
    "\n",
    "qs =[]\n",
    "\n",
    "for i in range (0, 72, 3):\n",
    "    qs.append (sum (lb [i:i+3]))\n",
    "print (qs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4fbc49e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "26"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len (qs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "02ead9fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "72"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len (lb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "6a84504a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2023Q 4', '2023Q 3', '2023Q 2', '2023Q 1', '2022Q 4', '2022Q 3', '2022Q 2', '2022Q 1', '2021Q 4', '2021Q 3', '2021Q 2', '2021Q 1', '2020Q 4', '2020Q 3', '2020Q 2', '2020Q 1', '2019Q 4', '2019Q 3', '2019Q 2', '2019Q 1', '2018Q 4', '2018Q 3', '2018Q 2', '2018Q 1']\n"
     ]
    }
   ],
   "source": [
    "qtr = []\n",
    "for i in range (2023, 2017, -1):\n",
    "    for k in range (4, 0, -1):\n",
    "        qtr.append (str(i) + \"Q \" + str (k))\n",
    "print (qtr)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "39eca1cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['2023Q 4',\n",
       " '2023Q 3',\n",
       " '2023Q 2',\n",
       " '2023Q 1',\n",
       " '2022Q 4',\n",
       " '2022Q 3',\n",
       " '2022Q 2',\n",
       " '2022Q 1',\n",
       " '2021Q 4',\n",
       " '2021Q 3',\n",
       " '2021Q 2',\n",
       " '2021Q 1',\n",
       " '2020Q 4',\n",
       " '2020Q 3',\n",
       " '2020Q 2',\n",
       " '2020Q 1',\n",
       " '2019Q 4',\n",
       " '2019Q 3',\n",
       " '2019Q 2',\n",
       " '2019Q 1',\n",
       " '2018Q 4',\n",
       " '2018Q 3',\n",
       " '2018Q 2',\n",
       " '2018Q 1']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(qtr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "e60ec760",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[160700,\n",
       " 164300,\n",
       " 158400,\n",
       " 156300,\n",
       " 169382,\n",
       " 179134,\n",
       " 171186,\n",
       " 166862,\n",
       " 184600,\n",
       " 186805,\n",
       " 172138,\n",
       " 158276,\n",
       " 172395,\n",
       " 182802,\n",
       " 171610,\n",
       " 169857,\n",
       " 181135,\n",
       " 189092,\n",
       " 175512,\n",
       " 168290,\n",
       " 183456,\n",
       " 190517,\n",
       " 176888,\n",
       " 168876]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "qs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "a4f28375",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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uHHjxN27d7Vijhw5Ip555hmhVCqFk5OTiImJERUVFXrvMwsrIiIi46Pv7+86dR+rJ0FBQQHUajXy8/M534qIiMhI6Pv7u05MXiciIiKqD1hYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcnE9HF3gIiIiB6P5u9veuhtL3wSLGNP6g+OWBERERHJhIUVERERkUx4KpCIiOoNntqix40jVkREREQyYWFFREREJBMWVkREREQy4RwrInrkOA+GiOorjlgRERERyYSFFREREZFMWFgRERERyYRzrIhIL5wXRUT0YByxIiIiIpIJR6yIiIiMCEeP6zYWVkREddg/+SUK8Bcp0aPGU4FEREREMmFhRURERCQTngokIqLHinOGqD7hiBURERGRTFhYEREREcmEhRURERGRTDjHikgGnCNCREQAR6yIiIiIZMPCioiIiEgmLKyIiIiIZPJY51jt3r0bn332GQ4ePIjs7GysW7cOgwcPltoVCkWV282dOxf//ve/AQD+/v7YtWuXVvtLL72E1atXS6/z8vIQFRWFX3/9FQAQGhqK2NhYNGrUSIrJzMzE2LFjsX37dqhUKoSFhWHevHkwNzeXYo4ePYpx48Zh//79sLOzwxtvvIGpU6dW208iIqInBeea/u2xFlZFRUXo2LEjXnvtNTz//PM67dnZ2Vqvf/vtN4waNUonNjIyEjNnzpReq1QqrfawsDBcunQJCQkJAIDRo0cjPDwcGzZsAACUl5cjODgYTZo0QXJyMq5fv44RI0ZACIHY2FgAQEFBAfr374/evXsjLS0Np0+fRkREBKysrDBp0qR/fjCIiIjI6D3WwiooKAhBQUHVtjs5OWm9/u9//4vevXujZcuWWustLS11YiudOHECCQkJSE1NRffu3QEAS5YsgY+PD06dOgUPDw8kJibi+PHjyMrKgkajAQDMnz8fERERmDVrFmxsbBAfH4+7d+8iLi4OSqUSnp6eOH36NBYsWICJEydy1IqIiIiM53YLV69exaZNm7B8+XKdtvj4eKxatQqOjo4ICgrC9OnTYW1tDQBISUmBWq2WiioA6NGjB9RqNfbu3QsPDw+kpKTA09NTKqoAIDAwEMXFxTh48CB69+6NlJQU9OrVC0qlUitm8uTJuHDh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Htu3b8f8+fORlpaGPn36oLi4GACQk5MDc3Nz2NraauVzdHRETk6OFOPg4KDzng4ODloxjo6OWu22trYwNzeXYqoyZ84cad6WWq2Gi4vLwx0AIiIiqvPq9KnAe40bNw5HjhxBcnKy1vqXXnpJ+renpye8vb3h5uaGTZs24bnnnqs2nxACCoVCen3vv/9JzP0mT56MiRMnSq8LCgpYXBEREdVTRjFi9fbbb+PXX3/Fjh070KxZsxpjnZ2d4ebmhjNnzgAAnJycUFJSgry8PK243NxcaQTKyckJV69e1cn1119/acXcPzKVl5eH0tJSnZGseymVStjY2GgtREREVD/V6cJKCIFx48Zh7dq12L59O1q0aPHAba5fv46srCw4OzsDALp27QozMzNs3bpVisnOzkZGRgZ8fX0BAD4+PsjPz8f+/fulmH379iE/P18rJiMjA9nZ2VJMYmIilEolunbtKsv+EhERkXGr06cCx44dix9++AH//e9/YW1tLY0YqdVqqFQqFBYWIiYmBs8//zycnZ1x4cIFfPDBB7C3t8eQIUOk2FGjRmHSpElo3Lgx7OzsEB0dDS8vL+kqwbZt22LAgAGIjIzEt99+CwAYPXo0QkJC4OHhAQAICAhAu3btEB4ejs8++ww3btxAdHQ0IiMjOQpFREREAOr4iNXixYuRn58Pf39/ODs7S8tPP/0EADAxMcHRo0cxaNAguLu7Y8SIEXB3d0dKSgqsra2lPAsXLsTgwYMxdOhQ+Pn5wdLSEhs2bICJiYkUEx8fDy8vLwQEBCAgIAAdOnTAypUrpXYTExNs2rQJFhYW8PPzw9ChQzF48GDMmzfv0R0QIiIiqtPq9IiVEKLGdpVKhS1btjwwj4WFBWJjYxEbG1ttjJ2dHVatWlVjHldXV2zcuPGB70dERERPpjo9YkVERERkTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYEREREcmEhRURERGRTFhYERER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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_pos2 = range (len (qtr))\n",
    "qtr_birth = mp.bar (qtr, qs)\n",
    "mp.xlabel ('Quarters')\n",
    "mp.ylabel ('No. of Births in France')\n",
    "mp.title ('France live births plotted quarterwise 2018-2023')\n",
    "mp.xticks (y_pos2, qtr, rotation=90)\n",
    "mp.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "6088076f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2023Q 4', '2023Q 3', '2023Q 2', '2023Q 1', '2022Q 4', '2022Q 3', '2022Q 2', '2022Q 1', '2021Q 4', '2021Q 3', '2021Q 2', '2021Q 1', '2020Q 4', '2020Q 3', '2020Q 2', '2020Q 1', '2019Q 4', '2019Q 3', '2019Q 2', '2019Q 1', '2018Q 4', '2018Q 3', '2018Q 2', '2018Q 1'] 24\n",
      "[9.833333333333334, 10.1, 9.9, 9.866666666666665, 10.399999999999999, 11.033333333333331, 10.666666666666666, 10.6, 11.366666666666667, 11.533333333333333, 10.766666666666666, 10.066666666666665, 10.699999999999998, 11.299999999999999, 10.799999999999999, 10.700000000000001, 11.233333333333334, 11.733333333333333, 11.066666666666668, 10.733333333333334, 11.4, 11.833333333333334, 11.166666666666666, 10.799999999999999] 24\n"
     ]
    },
    {
     "data": {
      "image/png": "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lA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyKrk5WPr1q3xd3/3dzFixIjo2bNnHHDAAfGjH/0oGhsbS30oAKAMdSt14M033xz/9E//FPfcc0+MHj06nnvuubj00kujpqYmvvOd75T6cABAmSl5+XjmmWdi8uTJMXHixIiI2H///ePee++N5557rtSHAgDKUMlvu3z2s5+N3/72t7FixYqIiHjhhRfi6aefjs9//vM73L9YLEZDQ0OzBQDYc5X8ysc111wT9fX1ccghh0TXrl1j27ZtceONN8b555+/w/1nzZoVM2fOLPU0AIBOquRXPu677774+c9/HvPnz48lS5bEPffcE3//938f99xzzw73nzZtWtTX1zcttbW1pZ4SANCJlPzKxw9+8IO49tpr47zzzouIiMMPPzxWr14ds2bNiksuuWS7/auqqqKqqqrU0wAAOqmSX/l46623okuX5rFdu3b1qC0AEBHtcOXjC1/4Qtx4440xfPjwGD16dDz//PNxyy23xNe//vVSHwoAKEMlLx//+I//GNddd11cddVVsWHDhhg6dGhcfvnlcf3115f6UABAGSp5+ejTp0/MmTMn5syZU+poAGAP4LNdAICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICs2qV8rF27Ni688MIYMGBA9OrVK4466qhYvHhxexwKACgz3UoduHHjxhg3blycfPLJ8Zvf/CYGDhwYf/zjH6Nv376lPhQAUIZKXj5uvvnmGDZsWNx1111N2/bff/+d7l8sFqNYLDatNzQ0lHpKAEAnUvLbLg8++GAce+yxce6558bAgQPj6KOPjjvvvHOn+8+aNStqamqalmHDhpV6SgBAJ1Ly8vHqq6/G7bffHiNHjoyHH344rrjiivj2t78d8+bN2+H+06ZNi/r6+qaltra21FMCADqRkt92aWxsjGOPPTZuuummiIg4+uij4+WXX47bb789Lr744u32r6qqiqqqqlJPAwDopEp+5WPIkCFx6KGHNtv26U9/OtasWVPqQwEAZajk5WPcuHGxfPnyZttWrFgR++23X6kPBQCUoZKXj+9+97vx7LPPxk033RQrV66M+fPnxx133BFTpkwp9aEAgDJU8vJx3HHHxf333x/33ntvHHbYYfHjH/845syZE1/96ldLfSgAoAyV/AWnERFnnXVWnHXWWe0RDQCUOZ/tAgBkpXwAAFkpHwBAVsoHAJCV8gEAZKV8AABZKR8AQFbKBwCQlfIBAGSlfAAAWSkfAEBWygcAkJXyAQBkpXwAAFkpHwBAVsoHAJCV8gEAZKV8AABZKR8AQFbKBwCQlfIBAGSlfAAAWSkfAEBWygcAkJXyAQBkpXwAAFkpHwBAVsoHAJCV8gEAZKV8AABZKR8AQFbKBwCQlfIBAGSlfAAAWSkfAEBWygcAkJXyAQBkpXwAAFkpHwBAVsoHAJCV8gEAZKV8AABZKR8AQFbKBwCQlfIBAGSlfAAAWSkfAEBWygcAkFW7l49Zs2ZFoVCIqVOntvehAIAy0K7lY9GiRXHHHXfEEUcc0Z6HAQDKSLuVj82bN8dXv/rVuPPOO6Nfv37tdRgAoMy0W/mYMmVKTJw4MU499dRd7lcsFqOhoaHZAgDsubq1R+h//Md/xJIlS2LRokWfuO+sWbNi5syZ7TENAKATKvmVj9ra2vjOd74TP//5z6NHjx6fuP+0adOivr6+aamtrS31lACATqTkVz4WL14cGzZsiGOOOaZp27Zt2+LJJ5+MuXPnRrFYjK5duzaNVVVVRVVVVamnAQB0UiUvH5/73Ofi97//fbNtl156aRxyyCFxzTXXNCseAEDlKXn56NOnTxx22GHNtvXu3TsGDBiw3XYAoPJ4h1MAIKt2edrl4xYsWJDjMABAGXDlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDIquTlY9asWXHcccdFnz59YuDAgXH22WfH8uXLS30YAKBMlbx8PPHEEzFlypR49tln49FHH42tW7fGhAkTYsuWLaU+FABQhrqVOvB//ud/mq3fddddMXDgwFi8eHGceOKJ2+1fLBajWCw2rTc0NJR6SgBAJ9Lur/mor6+PiIj+/fvvcHzWrFlRU1PTtAwbNqy9pwQAdKB2LR8ppbj66qvjs5/9bBx22GE73GfatGlRX1/ftNTW1rbnlACADlby2y4f9bd/+7fx4osvxtNPP73TfaqqqqKqqqo9pwEAdCLtVj6+9a1vxYMPPhhPPvlk7Lvvvu11GACgzJS8fKSU4lvf+lbcf//9sWDBghgxYkSpDwEAlLGSl48pU6bE/Pnz44EHHog+ffpEXV1dRETU1NREz549S304AKDMlPwFp7fffnvU19fH+PHjY8iQIU3LfffdV+pDAQBlqF1uuwAA7IzPdgEAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMhK+QAAslI+AICslA8AICvlAwDISvkAALJSPgCArJQPACAr5QMAyEr5AACyUj4AgKyUDwAgK+UDAMiq3crHbbfdFiNGjIgePXrEMcccE0899VR7HQoAKCPtUj7uu+++mDp1akyfPj2ef/75OOGEE+LMM8+MNWvWtMfhAIAy0i7l45ZbbolvfOMb8c1vfjM+/elP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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "qbr =[]\n",
    "\n",
    "y_pos2 = range (len (qtr))\n",
    "\n",
    "for i in range (0, 72, 3):\n",
    "    qbr.append (sum (br [i:i+3]) / 3)\n",
    "\n",
    "print (qtr, len (qtr))\n",
    "print (qbr, len (qbr))\n",
    "bar1 = mp.bar (qtr, qbr)\n",
    "mp.xticks (y_pos2, qtr, rotation=90)\n",
    "mp.show ()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ee01356",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
