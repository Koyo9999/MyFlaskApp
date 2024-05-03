import pandas as pd
from flask import (Flask, request, render_template)

app = Flask(__name__)

# get raw_data
raw_data = pd.read_excel(r'b01_01.xlsx',
                         skiprows=9,
                         header=[1, 2, 3, 4, 5])
cl = raw_data.columns
df = pd.DataFrame({'prefecture': raw_data[cl[4]],
                   'city': raw_data[cl[6]],
                   'population_2020': raw_data[cl[7]],
                   'male': raw_data[cl[8]],
                   'female': raw_data[cl[9]],
                   'diff_value': raw_data[cl[11]],
                   'diff_rate': raw_data[cl[12]]})

# fix df
df = df.replace('-', 0)
tmp = df.columns.to_list()
[pd.to_numeric(df[i], errors='coerce') for i in tmp[2:6]]
df['population_2015'] = df['population_2020'] - df['diff_value']
df = df.reindex(columns=['prefecture',
                         'city',
                         'population_2020',
                         'population_2015',
                         'male',
                         'female',
                         'diff_value',
                         'diff_rate'])

unique_prefecture = df.prefecture.unique()


@app.route('/', methods=['GET', 'POST'])
def root():
    global chosen_pref
    chosen_pref = '14_神奈川県'
    if request.form:
        chosen_pref = request.form['prefecture']
        defalt_df = df[df['prefecture'] == chosen_pref].iloc[1:]
    else:
        defalt_df = df[df['prefecture'] == '14_神奈川県']
    c = {
        'labels': defalt_df['city'].tolist(),
        'pop_2015': defalt_df['population_2015'].tolist(),
        'pop_2020': defalt_df['population_2020'].tolist()
    }
    return render_template('graph.html',
                           c=c,
                           defalt_df=defalt_df,
                           chosen_pref=chosen_pref,
                           unique_prefecture=unique_prefecture)


if __name__ == "__main__":
    app.run(
        # debug=True,
        host='0.0.0.0',
        port=5000
    )
