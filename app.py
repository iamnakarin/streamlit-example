from sklearn import tree
model = tree.DecisionTreeClassifier()
feature = [ [60,69,3],
            [61,67,3],
            [62,62,5],
            [63,65,7],
            [64,67,7],
            [67,59,9],
            [67,59,14],
            [65,70,13],
            [62,80,12],
            [61,90,8],
            [64,80,5],
            [71,61,9],
            [38,79,15],
            [39,79,15],
            [39,79,16],
            [38,86,12],
            [40,79,14]
          ]
label = ['Cloudy','Cloudy','Cloudy','Cloudy','Cloudy','Cloudy',
        'Cloudy','Cloudy','Light Rain','Light Rain','Cloudy','Cloudy',
         'Light Rain','Light Rain','Light Rain','Light Rain','Light Rain'
]
txt1 =int(st.input_text('Input here:'))
txt2 =int(st.input_text('Input here:'))
txt3 =int(st.input_text('Input here:'))
model.fit(feature,label)
st.write(model.predict([[txt1,txt2,txt3]]))

