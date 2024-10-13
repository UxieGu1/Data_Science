{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNJFrpAHND3GwdwMikChYAi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/UxieGu1/Data_Science/blob/main/games.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 504
        },
        "id": "y34IrVWrskSc",
        "outputId": "62e65a43-1cef-4e30-a196-b1bcc28d5973"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Rank                       Name Platform    Year         Genre Publisher  \\\n",
              "0     1                 Wii Sports      Wii  2006.0        Sports  Nintendo   \n",
              "1     2          Super Mario Bros.      NES  1985.0      Platform  Nintendo   \n",
              "2     3             Mario Kart Wii      Wii  2008.0        Racing  Nintendo   \n",
              "3     4          Wii Sports Resort      Wii  2009.0        Sports  Nintendo   \n",
              "4     5   Pokemon Red/Pokemon Blue       GB  1996.0  Role-Playing  Nintendo   \n",
              "5     6                     Tetris       GB  1989.0        Puzzle  Nintendo   \n",
              "6     7      New Super Mario Bros.       DS  2006.0      Platform  Nintendo   \n",
              "7     8                   Wii Play      Wii  2006.0          Misc  Nintendo   \n",
              "8     9  New Super Mario Bros. Wii      Wii  2009.0      Platform  Nintendo   \n",
              "9    10                  Duck Hunt      NES  1984.0       Shooter  Nintendo   \n",
              "\n",
              "   NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales  \n",
              "0     41.49     29.02      3.77         8.46         82.74  \n",
              "1     29.08      3.58      6.81         0.77         40.24  \n",
              "2     15.85     12.88      3.79         3.31         35.82  \n",
              "3     15.75     11.01      3.28         2.96         33.00  \n",
              "4     11.27      8.89     10.22         1.00         31.37  \n",
              "5     23.20      2.26      4.22         0.58         30.26  \n",
              "6     11.38      9.23      6.50         2.90         30.01  \n",
              "7     14.03      9.20      2.93         2.85         29.02  \n",
              "8     14.59      7.06      4.70         2.26         28.62  \n",
              "9     26.93      0.63      0.28         0.47         28.31  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5d9576f4-e6ec-4962-8493-54dd51619af1\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>Rank</th>\n",
              "      <th>Name</th>\n",
              "      <th>Platform</th>\n",
              "      <th>Year</th>\n",
              "      <th>Genre</th>\n",
              "      <th>Publisher</th>\n",
              "      <th>NA_Sales</th>\n",
              "      <th>EU_Sales</th>\n",
              "      <th>JP_Sales</th>\n",
              "      <th>Other_Sales</th>\n",
              "      <th>Global_Sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Wii Sports</td>\n",
              "      <td>Wii</td>\n",
              "      <td>2006.0</td>\n",
              "      <td>Sports</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>41.49</td>\n",
              "      <td>29.02</td>\n",
              "      <td>3.77</td>\n",
              "      <td>8.46</td>\n",
              "      <td>82.74</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>Super Mario Bros.</td>\n",
              "      <td>NES</td>\n",
              "      <td>1985.0</td>\n",
              "      <td>Platform</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>29.08</td>\n",
              "      <td>3.58</td>\n",
              "      <td>6.81</td>\n",
              "      <td>0.77</td>\n",
              "      <td>40.24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Mario Kart Wii</td>\n",
              "      <td>Wii</td>\n",
              "      <td>2008.0</td>\n",
              "      <td>Racing</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>15.85</td>\n",
              "      <td>12.88</td>\n",
              "      <td>3.79</td>\n",
              "      <td>3.31</td>\n",
              "      <td>35.82</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Wii Sports Resort</td>\n",
              "      <td>Wii</td>\n",
              "      <td>2009.0</td>\n",
              "      <td>Sports</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>15.75</td>\n",
              "      <td>11.01</td>\n",
              "      <td>3.28</td>\n",
              "      <td>2.96</td>\n",
              "      <td>33.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>Pokemon Red/Pokemon Blue</td>\n",
              "      <td>GB</td>\n",
              "      <td>1996.0</td>\n",
              "      <td>Role-Playing</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>11.27</td>\n",
              "      <td>8.89</td>\n",
              "      <td>10.22</td>\n",
              "      <td>1.00</td>\n",
              "      <td>31.37</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>6</td>\n",
              "      <td>Tetris</td>\n",
              "      <td>GB</td>\n",
              "      <td>1989.0</td>\n",
              "      <td>Puzzle</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>23.20</td>\n",
              "      <td>2.26</td>\n",
              "      <td>4.22</td>\n",
              "      <td>0.58</td>\n",
              "      <td>30.26</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>7</td>\n",
              "      <td>New Super Mario Bros.</td>\n",
              "      <td>DS</td>\n",
              "      <td>2006.0</td>\n",
              "      <td>Platform</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>11.38</td>\n",
              "      <td>9.23</td>\n",
              "      <td>6.50</td>\n",
              "      <td>2.90</td>\n",
              "      <td>30.01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8</td>\n",
              "      <td>Wii Play</td>\n",
              "      <td>Wii</td>\n",
              "      <td>2006.0</td>\n",
              "      <td>Misc</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>14.03</td>\n",
              "      <td>9.20</td>\n",
              "      <td>2.93</td>\n",
              "      <td>2.85</td>\n",
              "      <td>29.02</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>9</td>\n",
              "      <td>New Super Mario Bros. Wii</td>\n",
              "      <td>Wii</td>\n",
              "      <td>2009.0</td>\n",
              "      <td>Platform</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>14.59</td>\n",
              "      <td>7.06</td>\n",
              "      <td>4.70</td>\n",
              "      <td>2.26</td>\n",
              "      <td>28.62</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>10</td>\n",
              "      <td>Duck Hunt</td>\n",
              "      <td>NES</td>\n",
              "      <td>1984.0</td>\n",
              "      <td>Shooter</td>\n",
              "      <td>Nintendo</td>\n",
              "      <td>26.93</td>\n",
              "      <td>0.63</td>\n",
              "      <td>0.28</td>\n",
              "      <td>0.47</td>\n",
              "      <td>28.31</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5d9576f4-e6ec-4962-8493-54dd51619af1')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-5d9576f4-e6ec-4962-8493-54dd51619af1 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-5d9576f4-e6ec-4962-8493-54dd51619af1');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-57d7f5df-2182-40b5-a65c-72c621784b77\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-57d7f5df-2182-40b5-a65c-72c621784b77')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-57d7f5df-2182-40b5-a65c-72c621784b77 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 16598,\n  \"fields\": [\n    {\n      \"column\": \"Rank\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 4791,\n        \"min\": 1,\n        \"max\": 16600,\n        \"num_unique_values\": 16598,\n        \"samples\": [\n          8930,\n          4791,\n          15495\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 11493,\n        \"samples\": [\n          \"Close Combat: First to Fight\",\n          \"Rock 'N Roll Racing\",\n          \"Hakuouki\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Platform\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 31,\n        \"samples\": [\n          \"TG16\",\n          \"2600\",\n          \"SAT\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5.828981114712785,\n        \"min\": 1980.0,\n        \"max\": 2020.0,\n        \"num_unique_values\": 39,\n        \"samples\": [\n          1981.0,\n          1983.0,\n          1996.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Genre\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 12,\n        \"samples\": [\n          \"Adventure\",\n          \"Fighting\",\n          \"Sports\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Publisher\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 578,\n        \"samples\": [\n          \"JoWood Productions\",\n          \"Takuyo\",\n          \"Kamui\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NA_Sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.8166830292990428,\n        \"min\": 0.0,\n        \"max\": 41.49,\n        \"num_unique_values\": 409,\n        \"samples\": [\n          1.7,\n          2.97,\n          3.92\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"EU_Sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.5053512312869366,\n        \"min\": 0.0,\n        \"max\": 29.02,\n        \"num_unique_values\": 305,\n        \"samples\": [\n          1.15,\n          0.98,\n          2.25\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"JP_Sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.30929064808213236,\n        \"min\": 0.0,\n        \"max\": 10.22,\n        \"num_unique_values\": 244,\n        \"samples\": [\n          0.47,\n          6.5,\n          2.1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Other_Sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.18858840291278392,\n        \"min\": 0.0,\n        \"max\": 10.57,\n        \"num_unique_values\": 157,\n        \"samples\": [\n          0.38,\n          0.23,\n          0.48\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Global_Sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.5550279355699022,\n        \"min\": 0.01,\n        \"max\": 82.74,\n        \"num_unique_values\": 623,\n        \"samples\": [\n          3.91,\n          0.65,\n          5.11\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 36
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('vgsales.csv')\n",
        "df.head(10)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(f'Total de vendas globais: ')\n",
        "df['Global_Sales'].sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ikva7ef2tM0P",
        "outputId": "89851c7c-b4ed-4991-e645-fb66460d1b6b"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total de vendas globais: \n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "8920.44"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sales_platform = df.groupby('Platform')['Global_Sales'].sum()\n",
        "print(sales_platform)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fsC0imeatq_g",
        "outputId": "57f116b1-1650-440c-d739-a2c658546170"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Platform\n",
            "2600      97.08\n",
            "3DO        0.10\n",
            "3DS      247.46\n",
            "DC        15.97\n",
            "DS       822.49\n",
            "GB       255.45\n",
            "GBA      318.50\n",
            "GC       199.36\n",
            "GEN       28.36\n",
            "GG         0.04\n",
            "N64      218.88\n",
            "NES      251.07\n",
            "NG         1.44\n",
            "PC       258.82\n",
            "PCFX       0.03\n",
            "PS       730.66\n",
            "PS2     1255.64\n",
            "PS3      957.84\n",
            "PS4      278.10\n",
            "PSP      296.28\n",
            "PSV       61.93\n",
            "SAT       33.59\n",
            "SCD        1.87\n",
            "SNES     200.05\n",
            "TG16       0.16\n",
            "WS         1.42\n",
            "Wii      926.71\n",
            "WiiU      81.86\n",
            "X360     979.96\n",
            "XB       258.26\n",
            "XOne     141.06\n",
            "Name: Global_Sales, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "top_games = df.sort_values(by='Global_Sales', ascending=False).head(10)\n",
        "print(top_games[['Name', 'Global_Sales']])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "COuX53jRvvhZ",
        "outputId": "72e2486d-6fbe-4309-d5b5-618e06789146"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                        Name  Global_Sales\n",
            "0                 Wii Sports         82.74\n",
            "1          Super Mario Bros.         40.24\n",
            "2             Mario Kart Wii         35.82\n",
            "3          Wii Sports Resort         33.00\n",
            "4   Pokemon Red/Pokemon Blue         31.37\n",
            "5                     Tetris         30.26\n",
            "6      New Super Mario Bros.         30.01\n",
            "7                   Wii Play         29.02\n",
            "8  New Super Mario Bros. Wii         28.62\n",
            "9                  Duck Hunt         28.31\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Média de vendas globais por ano \")\n",
        "mean_for_year = df.groupby('Year')['Global_Sales'].mean().round(2)\n",
        "mean_for_year.head(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 446
        },
        "id": "tuwkzHbTxbqv",
        "outputId": "51548558-596a-4c2b-e2d0-da5f25ef1487"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Média de vendas globais por ano \n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Year\n",
              "1980.0    1.26\n",
              "1981.0    0.78\n",
              "1982.0    0.80\n",
              "1983.0    0.99\n",
              "1984.0    3.60\n",
              "1985.0    3.85\n",
              "1986.0    1.77\n",
              "1987.0    1.36\n",
              "1988.0    3.15\n",
              "1989.0    4.32\n",
              "Name: Global_Sales, dtype: float64"
            ],
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
              "      <th>Global_Sales</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Year</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1980.0</th>\n",
              "      <td>1.26</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1981.0</th>\n",
              "      <td>0.78</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1982.0</th>\n",
              "      <td>0.80</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1983.0</th>\n",
              "      <td>0.99</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1984.0</th>\n",
              "      <td>3.60</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1985.0</th>\n",
              "      <td>3.85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1986.0</th>\n",
              "      <td>1.77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1987.0</th>\n",
              "      <td>1.36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1988.0</th>\n",
              "      <td>3.15</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1989.0</th>\n",
              "      <td>4.32</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> float64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "games_per_platform = df['Platform'].value_counts()\n",
        "top_platform = games_per_platform.idxmax()\n",
        "top_platform_count = games_per_platform.max()\n",
        "print(f\"Plataforma com mais jogos: {top_platform} ({top_platform_count} jogos)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hnoyoKwIygKP",
        "outputId": "7b83164e-60d0-4d4d-f50e-35714465facb"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Plataforma com mais jogos: DS (2163 jogos)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "u4i6kc110_fN"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sum_sales = df.groupby('Genre')['Global_Sales'].sum()\n",
        "sum_sales.plot(kind='bar', color='skyblue')\n",
        "\n",
        "plt.title('Soma das Vendas Globais por Gênero de Jogo')\n",
        "plt.xlabel('Gênero')\n",
        "plt.ylabel('Vendas Globais (milhões)')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 544
        },
        "id": "nOlYp5WEz2u-",
        "outputId": "c77c93a8-0794-4806-8335-a252f1d84f39"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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l5cXDAwM0LVrV4wfPx6GhobfdF/jx4/H6NGj/1NeIiIiyjlyxCmzo0eP4saNG+jUqdNX9y1btiySkpJw7949AB/6IUVGRsr2Sb3+uX5HQUFBiI6Oli4PHz78bw+AiIiINFqOKIgWL14MHx8flChR4qv7hoWFQUdHB7a2tgCAcuXK4ciRI0hMTJT22bt3L4oUKZLm6TIAMDQ0hIWFhexCRERE3y9FC6K3b98iLCwMYWFhAIDw8HCEhYXhwYMH0j4xMTHYuHFjmkeHQkNDMW3aNFy4cAF3797F6tWr0b9/f7Rp00Yqdlq1agUDAwMEBgbiypUrWL9+PaZPny471UZERETaTdE+RGfOnEHVqlWl66lFSkBAAJYtWwYAWLduHYQQaNmypdrPGxoaYt26dQgODkZ8fDwKFiyI/v37y4odS0tL7NmzBz179oSPjw9y586NkSNHcsg9ERERSVRCCKF0CE0XExMDS0tLREdHp+v0GUeZERERKS8jn985og8RERERUVZiQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPRZEREREpPVYEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPRZEREREpPVYEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPRZEREREpPVYEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT1FC6IjR46gfv36cHBwgEqlwtatW2Xb27dvD5VKJbvUrl1btk9UVBRat24NCwsLWFlZITAwEG/fvpXtc/HiRVSsWBFGRkZwdHTExIkTs/qhERERUQ6iaEEUGxuLEiVKYPbs2Z/dp3bt2nj69Kl0Wbt2rWx769atceXKFezduxc7duzAkSNH0KVLF2l7TEwMatWqBScnJ5w9exaTJk1CcHAwFixYkGWPi4iIiHIWPSXvvE6dOqhTp84X9zE0NIS9vX2a265du4Zdu3bh9OnT8PX1BQDMnDkTdevWxR9//AEHBwesXr0aCQkJWLJkCQwMDFCsWDGEhYVhypQpssKJiIiItJfG9yE6dOgQbG1tUaRIEXTv3h0vX76UtoWGhsLKykoqhgCgRo0a0NHRwf/+9z9pn0qVKsHAwEDax8/PDzdu3MCrV6+y74EQERGRxlL0CNHX1K5dG40aNULBggVx584dDBs2DHXq1EFoaCh0dXUREREBW1tb2c/o6ekhV65ciIiIAABERESgYMGCsn3s7OykbdbW1mr3Gx8fj/j4eOl6TExMZj80IiIi0iAaXRC1aNFC+r+npye8vLzg6uqKQ4cOoXr16ll2v+PHj8fo0aOz7PaJiIhIs2j8KbOPubi4IHfu3Lh9+zYAwN7eHs+ePZPtk5SUhKioKKnfkb29PSIjI2X7pF7/XN+koKAgREdHS5eHDx9m9kMhIiIiDZKjCqJHjx7h5cuXyJs3LwCgXLlyeP36Nc6ePSvtc+DAAaSkpKBs2bLSPkeOHEFiYqK0z969e1GkSJE0T5cBHzpyW1hYyC5ERET0/VK0IHr79i3CwsIQFhYGAAgPD0dYWBgePHiAt2/fYtCgQTh58iTu3buH/fv34+eff4abmxv8/PwAAEWLFkXt2rXRuXNnnDp1CsePH0evXr3QokULODg4AABatWoFAwMDBAYG4sqVK1i/fj2mT5+OAQMGKPWwiYiISMMoWhCdOXMG3t7e8Pb2BgAMGDAA3t7eGDlyJHR1dXHx4kX4+/ujcOHCCAwMhI+PD44ePQpDQ0PpNlavXg13d3dUr14ddevWRYUKFWRzDFlaWmLPnj0IDw+Hj48PBg4ciJEjR3LIPREREUlUQgihdAhNFxMTA0tLS0RHR6fr9FnI+ReZev9DvXNn6u0RERFpg4x8fueoPkREREREWYEFEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPRZEREREpPVYEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPRZEREREpPVYEBEREZHW08voD8THx+N///sf7t+/j7i4OOTJkwfe3t4oWLBgVuQjIiIiynLpLoiOHz+O6dOnY/v27UhMTISlpSWMjY0RFRWF+Ph4uLi4oEuXLujWrRvM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6HvDgoiIiIi0HgsiIiIi0nosiIiIiEjraXSnatJuIedfZPptDvXOnem3SUREOR+PEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPa5lRkRE9BmZvaYi11PUXDxCRERERFqPBRERERFpPRZEREREpPVYEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1WBARERGR1mNBRERERFqPBRERERFpPRZEREREpPVYEBEREZHWY0FEREREWo8FEREREWk9FkRERESk9VgQERERkdZjQURERERajwURERERaT0WRERERKT1NLogGj9+PEqXLg1zc3PY2tqiQYMGuHHjhmyfKlWqQKVSyS7dunWT7fPgwQPUq1cPJiYmsLW1xaBBg5CUlJSdD4WIiIg0mJ7SAb7k8OHD6NmzJ0qXLo2kpCQMGzYMtWrVwtWrV2Fqairt17lzZ4wZM0a6bmJiIv0/OTkZ9erVg729PU6cOIGnT5+iXbt20NfXx7hx47L18RAREZFm0uiCaNeuXbLry5Ytg62tLc6ePYtKlSpJ7SYmJrC3t0/zNvbs2YOrV69i3759sLOzQ8mSJTF27FgMGTIEwcHBMDAwyNLHQERERJpPo0+ZfSo6OhoAkCtXLln76tWrkTt3bhQvXhxBQUGIi4uTtoWGhsLT0xN2dnZSm5+fH2JiYnDlypU07yc+Ph4xMTGyCxEREX2/NPoI0cdSUlLQr18/lC9fHsWLF5faW7VqBScnJzg4OODixYsYMmQIbty4gS1btgAAIiIiZMUQAOl6REREmvc1fvx4jB49OoseCREREWmaHFMQ9ezZE5cvX8axY8dk7V26dJH+7+npibx586J69eq4c+cOXF1dv+m+goKCMGDAAOl6TEwMHB0dvy04EaVLyPkXmX6bQ71zZ/ptEtH3KUcURL169cKOHTtw5MgR5M+f/4v7li1bFgBw+/ZtuLq6wt7eHqdOnZLtExkZCQCf7XdkaGgIQ0PDTEiuufjhQ0RE9C+N7kMkhECvXr3w559/4sCBAyhYsOBXfyYsLAwAkDdvXgBAuXLlcOnSJTx79kzaZ+/evbCwsICHh0eW5CYiIqKc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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "top_year = df['Year'].value_counts().idxmax()\n",
        "top_year_count = df['Year'].value_counts().max()\n",
        "print(f\"O ano com o maior número de jogos lançados foi: {top_year} ({top_year_count} jogos)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5f5tGk1P2tjm",
        "outputId": "62142208-f62e-48ce-fb34-2fded5f25c05"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O ano com o maior número de jogos lançados foi: 2009.0 (1431 jogos)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "global_sales_1M = df[df['Global_Sales'] > 1.0]\n",
        "print(global_sales_1M)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKb1Xkps37du",
        "outputId": "86e413a8-269c-4ba6-e772-d8f84e444b91"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "      Rank                                       Name Platform    Year  \\\n",
            "0        1                                 Wii Sports      Wii  2006.0   \n",
            "1        2                          Super Mario Bros.      NES  1985.0   \n",
            "2        3                             Mario Kart Wii      Wii  2008.0   \n",
            "3        4                          Wii Sports Resort      Wii  2009.0   \n",
            "4        5                   Pokemon Red/Pokemon Blue       GB  1996.0   \n",
            "...    ...                                        ...      ...     ...   \n",
            "2049  2051  Oshare Majo Love and Berry: DS Collection       DS  2006.0   \n",
            "2050  2052                            Monster Rancher       PS  1997.0   \n",
            "2051  2053                   The LEGO Movie Videogame      PS3  2014.0   \n",
            "2052  2054                                     DiRT 2      PS3  2009.0   \n",
            "2053  2055                             Rayman Legends      PS4  2014.0   \n",
            "\n",
            "             Genre                               Publisher  NA_Sales  \\\n",
            "0           Sports                                Nintendo     41.49   \n",
            "1         Platform                                Nintendo     29.08   \n",
            "2           Racing                                Nintendo     15.85   \n",
            "3           Sports                                Nintendo     15.75   \n",
            "4     Role-Playing                                Nintendo     11.27   \n",
            "...            ...                                     ...       ...   \n",
            "2049          Misc                                    Sega      0.00   \n",
            "2050    Simulation                              Tecmo Koei      0.12   \n",
            "2051        Action  Warner Bros. Interactive Entertainment      0.33   \n",
            "2052        Racing                             Codemasters      0.27   \n",
            "2053      Platform                                 Ubisoft      0.21   \n",
            "\n",
            "      EU_Sales  JP_Sales  Other_Sales  Global_Sales  \n",
            "0        29.02      3.77         8.46         82.74  \n",
            "1         3.58      6.81         0.77         40.24  \n",
            "2        12.88      3.79         3.31         35.82  \n",
            "3        11.01      3.28         2.96         33.00  \n",
            "4         8.89     10.22         1.00         31.37  \n",
            "...        ...       ...          ...           ...  \n",
            "2049      0.00      1.01         0.00          1.01  \n",
            "2050      0.08      0.74         0.07          1.01  \n",
            "2051      0.48      0.02         0.18          1.01  \n",
            "2052      0.53      0.00         0.20          1.01  \n",
            "2053      0.61      0.00         0.18          1.01  \n",
            "\n",
            "[2054 rows x 11 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "total_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum()\n",
        "total_sales.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 178
        },
        "id": "xX-YwtSx68ho",
        "outputId": "7a72b6c3-8fa9-4c82-910d-5aba6764abf0"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "NA_Sales    4392.95\n",
              "EU_Sales    2434.13\n",
              "JP_Sales    1291.02\n",
              "dtype: float64"
            ],
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
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>NA_Sales</th>\n",
              "      <td>4392.95</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>EU_Sales</th>\n",
              "      <td>2434.13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>JP_Sales</th>\n",
              "      <td>1291.02</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> float64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "p1rPiSQY7WIu"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}